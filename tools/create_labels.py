#! /usr/bin/env python3
"""Create the GitHub issue labels the bug-fix automation reads.

    python tools/create_labels.py            # dry run: list what would be created
    python tools/create_labels.py --apply    # create/update them with the gh CLI

Labels: the bugfix label, one per SMT in tools/smt-config.yml, and one per
published version (v1.0, v3.0, ...). Rerun after adding an SMT to the config.
"""

import argparse
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import repo  # noqa: E402


def wanted_labels(cfg: dict) -> list:
    labels = [(cfg["bugfix_label"], "d73a4a", "Approved bug fix: creates the bug-fix PR once SMT and version labels are set")]
    versions = set()
    for label, folder in cfg["smts"].items():
        if len(label) > 50:
            raise SystemExit(f"label too long for GitHub (max 50): {label}")
        labels.append((label, "0e8a16", f"SMT: {folder}"[:100]))
        smt_dir = repo.PUBLISHED / folder
        for major in (d for d in smt_dir.iterdir() if d.is_dir() and d.name.isdigit()):
            for minor in (d for d in major.iterdir() if d.is_dir() and d.name.isdigit()):
                versions.add((int(major.name), int(minor.name)))
    prefix = cfg["version_label_prefix"]
    labels += [(f"{prefix}{a}.{b}", "1d76db", "SMT version") for a, b in sorted(versions)]
    return labels


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="create the labels (needs gh, logged in)")
    ap.add_argument("--repo", default=repo.repo_slug())
    args = ap.parse_args()

    labels = wanted_labels(repo.load_config())
    for name, color, desc in labels:
        if not args.apply:
            print(f"would create  {name!r:28}  #{color}  {desc}")
            continue
        r = subprocess.run(["gh", "label", "create", name, "--color", color, "--description", desc,
                            "--force", "--repo", args.repo], capture_output=True, text=True)
        print(f"{'ok    ' if r.returncode == 0 else 'FAILED'}  {name}  {r.stderr.strip()}")
    print(f"\n{len(labels)} labels{'' if args.apply else ' (dry run; add --apply to create them)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
