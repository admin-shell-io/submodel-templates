#! /usr/bin/env python3
"""Pull-request checks for released SMT artifacts.

    python tools/check_release.py --base origin/main

Compares the working tree with the merge base of --base and fails if:

1. a released file under published/ or deprecated/ was changed or deleted.
   Released artifacts are immutable; a correction is a new bug-fix folder.
   Allowed: editing a README.md, and moving a file unchanged from published/
   to deprecated/ (the deprecation step).
2. an AASX in an added or changed release folder does not match its template
   JSON (see tools/build_aasx.py).
3. a relative link in an added or changed README.md does not resolve, or any
   README still links to a file this change moved or deleted.

Warnings (do not fail): a new release folder carrying a
``_forAASMetamodelVx.y.json`` copy or a copy of an already published PDF.
"""

import argparse
import hashlib
import pathlib
import re
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_aasx  # noqa: E402
import repo  # noqa: E402

RELEASED = ("published/", "deprecated/")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def name_status(base: str) -> list:
    """(status, old path, new path) for every change since ``base``, working tree included."""
    rows = []
    for line in repo.git("diff", "--name-status", "-M", base).splitlines():
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("R"):
            rows.append((status, parts[1], parts[2]))
        else:
            rows.append((status, parts[1], parts[1]))
    for n in repo.git("ls-files", "--others", "--exclude-standard").splitlines():
        rows.append(("A", n, n))
    return rows


def check_immutable(rows: list) -> list:
    errors = []
    for status, old, new in rows:
        if not old.startswith(RELEASED) or status == "A":
            continue
        if status.startswith("R"):
            moved_to_deprecated = old.startswith("published/") and new == "deprecated/" + old[len("published/"):]
            if status == "R100" and moved_to_deprecated:
                continue
            errors.append(f"{old}: released file renamed/moved to {new} (only an unchanged move to deprecated/ is allowed)")
        elif pathlib.PurePosixPath(old).name == "README.md" and status == "M":
            continue
        elif status == "M":
            errors.append(f"{old}: released file was changed. Put the corrected file in a new bug-fix folder instead")
        elif status == "D":
            errors.append(f"{old}: released file was deleted")
        else:
            errors.append(f"{old}: unexpected change '{status}' to a released file")
    return errors


def readme_links(readme: pathlib.Path) -> list:
    out = []
    for target in LINK_RE.findall(readme.read_text(encoding="utf-8", errors="replace")):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        out.append(target)
    return out


def check_links(rows: list) -> list:
    errors = []
    readmes = {repo.ROOT / new for s, _, new in rows
               if new.startswith(RELEASED) and new.endswith("README.md") and s != "D" and (repo.ROOT / new).exists()}
    for readme in sorted(readmes):
        for target in readme_links(readme):
            path = (readme.parent / urllib.parse.unquote(target.split("#")[0])).resolve()
            if not path.exists():
                errors.append(f"{readme.relative_to(repo.ROOT).as_posix()}: link target missing: {target}")

    gone = {(repo.ROOT / old).resolve() for s, old, new in rows if s == "D" or s.startswith("R")}
    if gone:
        for readme in sorted((repo.ROOT / "published").rglob("README.md")):
            for target in readme_links(readme):
                path = (readme.parent / urllib.parse.unquote(target.split("#")[0])).resolve()
                if path in gone:
                    errors.append(f"{readme.relative_to(repo.ROOT).as_posix()}: links to {target}, which this change moved or deleted")
    return errors


def new_folder_warnings(rows: list) -> list:
    warnings = []
    added = {(repo.ROOT / new).parent for s, _, new in rows if s == "A" and new.startswith("published/")}
    known_pdfs = None
    for folder in sorted(added):
        if not folder.is_dir():
            continue
        for j in folder.glob("*.json"):
            if repo.is_twin_json(j):
                warnings.append(f"{j.relative_to(repo.ROOT).as_posix()}: identical copy of the plain JSON; not needed in new releases")
        pdfs = list(folder.glob("*.pdf"))
        if pdfs and known_pdfs is None:
            known_pdfs = {}
            for p in (repo.ROOT / "published").rglob("*.pdf"):
                if p.parent not in added:
                    known_pdfs.setdefault(hashlib.sha1(p.read_bytes()).hexdigest(), p)
        for p in pdfs:
            same = known_pdfs.get(hashlib.sha1(p.read_bytes()).hexdigest())
            if same:
                warnings.append(f"{p.relative_to(repo.ROOT).as_posix()}: same bytes as {same.relative_to(repo.ROOT).as_posix()}; link it from the README instead of copying")
    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="origin/main")
    args = ap.parse_args()

    merge_base = repo.git("merge-base", args.base, "HEAD").strip()
    rows = name_status(merge_base)

    print("1. Released files are unchanged")
    errors = check_immutable(rows)
    print("   ok" if not errors else f"   {len(errors)} problem(s)")

    print("2. AASX packages match their template JSON")
    folders = build_aasx.changed_folders(args.base)
    aasx_errors = []
    for folder in folders:
        aasx_errors += build_aasx.build_folder(folder, check=True)
    print(f"   {len(folders)} folder(s) checked, " + ("ok" if not aasx_errors else f"{len(aasx_errors)} problem(s)"))
    errors += aasx_errors

    print("3. README links resolve")
    link_errors = check_links(rows)
    print("   ok" if not link_errors else f"   {len(link_errors)} problem(s)")
    errors += link_errors

    for w in new_folder_warnings(rows):
        print(f"::warning::{w}")
    for e in errors:
        print(f"::error::{e}")
    print(f"\nResult: {'FAIL' if errors else 'PASS'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
