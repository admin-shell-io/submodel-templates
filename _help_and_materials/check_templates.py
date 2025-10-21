#! /usr/bin/env python3

import os
import pathlib
import sys
from typing import Iterator, List
from aas_test_engines import file as aas_file


def print_red(msg: str):
    print(f"\033[91m{msg}\033[0m")


def print_green(msg: str):
    print(f"\033[92m{msg}\033[0m")


def find_one(path: pathlib.Path, pattern: str):
    files = list(path.glob(pattern))
    if len(files) != 1:
        raise ValueError(f"Expected exactly one file matching {pattern}, found {len(files)}")
    return files[0]


def find_folders_without_subfolders(base_path) -> Iterator[str]:
    for root, dirs, files in os.walk(base_path):
        if not dirs:
            yield root


def check_template(path: pathlib.Path, root: pathlib.Path) -> bool:
    print(f"Checking {path.relative_to(root)}:")
    try:
        readme = find_one(path, "*.md")
        pdf = find_one(path, '*.pdf')
        json_files = list(path.glob("*.json"))
        aasx_files = list(path.glob("*.aasx"))
    except ValueError as e:
        print_red(f"!!! {e}")
        return False
    ok = True
    for i in json_files:
        result = aas_file.check_json_file(open(i))
        if result.ok():
            print_green(f"- {i.relative_to(root)} is ok")
        else:
            print_red(f"- {i.relative_to(root)} is invalid")
            ok = False
    for i in aasx_files:
        result = aas_file.check_aasx_file(open(i))
        if result.ok():
            print_green(f"- {i.relative_to(root)} is ok")
        else:
            print_red(f"- {i.relative_to(root)} is invalid")
            ok = False
    return ok


def main() -> int:
    script_dir = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
    root_dir = script_dir.parent / 'published'
    ok = True
    for i in find_folders_without_subfolders(root_dir):
        path = pathlib.Path(i)
        if not check_template(path, root_dir):
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
