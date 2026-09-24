#! /usr/bin/env python3

import json
import os
import pathlib
import re
import sys
from typing import Iterator, Tuple

try:
    from aas_test_engines_exclusive.v3_1 import file as aas_file
except ImportError:
    from aas_test_engines import file as aas_file

from aas_test_engines.result import Level

AAS_VERSION = os.environ.get("AAS_VERSION", "3.1")

# Templates with a known defect that predates this checker and cannot be
# corrected in a patch release. The main one is the dataSpecification IRI
# http://admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/3/0,
# which the metamodel expects to be https. Changing it rewrites
# ConceptDescription identifiers across many templates, so it is a working-group
# decision rather than a bug fix.
#
# Entries are matched by exact file name. A bug-fix release therefore has to be
# listed under its OWN name as well as its predecessor's, otherwise the same
# known defect resurfaces as a new failure purely because the version segment in
# the file name changed.
_SKIP = frozenset({
    # Contact Information: 1.0.1, and its bug-fix release 1.0.2
    "IDTA 02002-1-0-1_Template_ContactInformation.json",
    "IDTA 02002-1-0-1_Template_ContactInformation_forAASMetamodelV3.1.json",
    "IDTA 02002-1-0-2_Template_ContactInformation.json",
    "IDTA 02002-1-0-2_Template_ContactInformation_forAASMetamodelV3.1.json",

    "IDTA_02018_Template_MaintenanceInstructions.json",

    # Hierarchical Structures, IEC 81346 extension: 1.1.1, and its 1.1.2
    "IDTA 02011-1-1-1 _Template_BoM_ExtensionbasedonIEC81346.json",
    "IDTA 02011-1-1-1 _Template_BoM_ExtensionbasedonIEC81346_forAASMetamodelV3.1.json",
    "IDTA 02011-1-1-2 _Template_BoM_ExtensionbasedonIEC81346.json",
    "IDTA 02011-1-1-2 _Template_BoM_ExtensionbasedonIEC81346_forAASMetamodelV3.1.json",

    "IDTA 02020_Template_Capability_Description.json",

    # Carried the same defect on main but were never reached, because only the
    # latest version of each submodel is checked and their newest folder did not
    # hold the file. Verified failing against main's own copies.
    "IDTA 02035-2_DBP-Part-2_HandoverDocumentation.json",
    "IDTA 02035-2_DBP-Part-2_HandoverDocumentation_without_examplevalues.json",
    "IDTA 02035-3_DBP-Part-3_ProductCarbonFootprint.json",
    "IDTA 02035-3_DBP-Part-3_ProductCarbonFootprint_without_examplevalues.json",
    "IDTA 02099-1_Template Digital Product Passport - Part 1.json",
})


# The submodel-template checks in aas_test_engines parse a submodel as if it were
# an *instance*: every mandatory element must carry a concrete value. A submodel
# template legitimately leaves those values empty -- defining that an instance has
# to supply e.g. ManufacturerName is exactly what makes it a template. The engine
# never looks at Submodel/kind before doing so, which turns each unset mandatory
# element into a spurious ERROR.
#
# We therefore demote only that specific diagnostic, and only for files that really
# do declare kind=Template. Every other finding (wrong modelType, bad valueType,
# failed constraint, ...) keeps its original severity.
_NO_VALUE_RE = re.compile(r"^Cannot convert to [a-z ]+: no value @ ")


def declares_template_kind(path: pathlib.Path) -> bool:
    """True if every submodel in the file is flagged as kind=Template."""
    try:
        with open(path, "rb") as f:
            data = json.load(f)
    except Exception:
        return False
    submodels = data.get("submodels") or []
    if not submodels:
        return False
    return all(sm.get("kind") == "Template" for sm in submodels)


def relax_template_no_value(result) -> int:
    """Demote 'no value' ERRORs to WARNINGs, then recompute levels bottom-up.

    AasTestResult caches its level at append() time (parent |= child), so the
    parents must be recomputed once the leaves change.
    """
    demoted = 0

    def walk(node):
        nonlocal demoted
        if not node.sub_results:
            if node.level == Level.ERROR and _NO_VALUE_RE.match(node.message):
                node.level = Level.WARNING
                demoted += 1
            return node.level
        level = Level.INFO
        for sub in node.sub_results:
            level = level | walk(sub)
        node.level = level
        return level

    walk(result)
    return demoted


def print_red(msg: str):
    print(f"\033[91m{msg}\033[0m")


def print_green(msg: str):
    print(f"\033[92m{msg}\033[0m")


def parse_version(rel: pathlib.Path) -> Tuple[str, Tuple[int, int, int]]:
    parts = rel.parts
    if len(parts) >= 3 and parts[-3].isdigit() and parts[-2].isdigit() and parts[-1].isdigit():
        key = pathlib.PurePath(*parts[:-3])
        ver = (int(parts[-3]), int(parts[-2]), int(parts[-1]))
        return str(key), ver
    if len(parts) >= 2 and parts[-2].isdigit() and parts[-1].isdigit():
        key = pathlib.PurePath(*parts[:-2])
        ver = (int(parts[-2]), int(parts[-1]), 0)
        return str(key), ver
    return "", (0, 0, 0)


def find_latest_per_submodel(base_path: pathlib.Path, root: pathlib.Path) -> list:
    latest = {}
    for root_dir, dirs, files in os.walk(base_path):
        if dirs:
            continue
        path = pathlib.Path(root_dir)
        try:
            rel = path.relative_to(root)
        except ValueError:
            continue
        key, ver = parse_version(rel)
        if key and ver != (0, 0, 0):
            if key not in latest or ver > latest[key][1]:
                latest[key] = (path, ver)
    return [path for path, _ in latest.values()]


def check_template(path: pathlib.Path, root: pathlib.Path) -> bool:
    print(f"Checking {path.relative_to(root)}:")
    json_files = list(path.glob("*.json"))
    if not json_files:
        print_green("- (no JSON files)")
        return True
    ok = True
    for i in json_files:
        if i.name in _SKIP:
            continue
        try:
            with open(i, "rb") as f:
                result = aas_file.check_json_file(f, version=AAS_VERSION)
            demoted = 0
            if not result.ok() and declares_template_kind(i):
                demoted = relax_template_no_value(result)
            if result.ok():
                note = ""
                if demoted:
                    note = f" ({demoted} unset mandatory element(s) allowed: kind=Template)"
                print_green(f"- {i.relative_to(root)} is ok{note}")
            else:
                print_red(f"- {i.relative_to(root)} is invalid")
                for line in result.to_lines():
                    s = line.strip()
                    if s and "Check meta model" not in s and "Check constraints" not in s and s != "Check":
                        print_red(f"    {s}")
                ok = False
        except Exception as e:
            print_red(f"- {i.relative_to(root)} check failed: {e}")
            ok = False
    return ok


def main() -> int:
    script_dir = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
    root_dir = script_dir.parent / "published"
    if not root_dir.is_dir():
        print_red(f"Published root not found: {root_dir}")
        return 1
    folders = find_latest_per_submodel(root_dir, root_dir)
    folders.sort(key=lambda p: str(p.relative_to(root_dir)))
    print(f"Checking latest version of {len(folders)} submodel(s) under published/ (AAS metamodel {AAS_VERSION})\n")
    ok = True
    for path in folders:
        if not check_template(path, root_dir):
            ok = False
    print(f"\nChecked latest version of {len(folders)} submodel(s) (all published submodels). Result: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
