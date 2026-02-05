#! /usr/bin/env python3

import os
import pathlib
import sys
from typing import Iterator, Tuple

try:
    from aas_test_engines_exclusive import file as aas_file
except ImportError:
    from aas_test_engines import file as aas_file


EXCLUDED_JSON = frozenset({
    "IDTA 02011-1-1-1 _Template_BoM_ExtensionbasedonIEC81346.json",
    "IDTA 02011-1-1-1 _Template_BoM_ExtensionbasedonIEC81346_forAASMetamodelV3.1.json",
})


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
        if i.name in EXCLUDED_JSON:
            continue
        try:
            with open(i, "rb") as f:
                result = aas_file.check_json_file(f)
            if result.ok():
                print_green(f"- {i.relative_to(root)} is ok")
            else:
                print_red(f"- {i.relative_to(root)} is invalid")
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
    print(f"Checking latest version of {len(folders)} submodel(s) under published/\n")
    ok = True
    for path in folders:
        if not check_template(path, root_dir):
            ok = False
    print(f"\nChecked latest version of {len(folders)} submodel(s). Result: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
