#! /usr/bin/env python3

import os
import pathlib
import sys
from typing import Iterator

try:
    from aas_test_engines_exclusive import file as aas_file
except ImportError:
    from aas_test_engines import file as aas_file


def print_red(msg: str):
    print(f"\033[91m{msg}\033[0m")


def print_green(msg: str):
    print(f"\033[92m{msg}\033[0m")


def is_bug_fix_folder(path: pathlib.Path, root: pathlib.Path) -> bool:
    try:
        rel = path.relative_to(root)
    except ValueError:
        return False
    parts = rel.parts
    if len(parts) < 4:
        return False
    maj, min_ver, patch = parts[-3], parts[-2], parts[-1]
    if not (maj.isdigit() and min_ver.isdigit() and patch.isdigit()):
        return False
    return int(patch) > 0


def find_bug_fix_leaf_folders(base_path: pathlib.Path, root: pathlib.Path) -> Iterator[pathlib.Path]:
    for root_dir, dirs, files in os.walk(base_path):
        if dirs:
            continue
        path = pathlib.Path(root_dir)
        if is_bug_fix_folder(path, root):
            yield path


def check_template(path: pathlib.Path, root: pathlib.Path) -> bool:
    print(f"Checking {path.relative_to(root)}:")
    json_files = list(path.glob("*.json"))
    if not json_files:
        print_green("- (no JSON files)")
        return True
    ok = True
    for i in json_files:
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
    ok = True
    for path in find_bug_fix_leaf_folders(root_dir, root_dir):
        if not check_template(path, root_dir):
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
