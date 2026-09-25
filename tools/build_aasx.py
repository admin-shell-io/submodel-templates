#! /usr/bin/env python3
"""Build every AASX of a release folder from its template JSON.

    python tools/build_aasx.py "published/Contact Information/1/0/2"
    python tools/build_aasx.py --check "published/Contact Information/1/0/2"
    python tools/build_aasx.py --check --changed-since origin/main

The JSON is the source. Each AASX keeps its package (images, relationships) and
its AAS metamodel version (the XML namespace it already has); only the model XML
inside is regenerated. An AASX that already matches its JSON is left byte-for-
byte untouched. A ``_forAASMetamodelVx.y.json`` copy is kept identical to the
plain JSON.

--check writes nothing and exits 1 if any AASX (or JSON copy) differs from the
JSON, i.e. if someone edited one without the other.
"""

import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import aas_io  # noqa: E402
import repo  # noqa: E402


def build_folder(folder: pathlib.Path, check: bool) -> list:
    """Returns a list of problems (in --check mode: every out-of-date file)."""
    problems = []
    rel = lambda p: p.relative_to(repo.ROOT).as_posix()  # noqa: E731

    for twin in sorted(folder.glob("*.json")):
        if not repo.is_twin_json(twin):
            continue
        base = twin.with_name(repo.V_SUFFIX_RE.sub("", twin.stem) + ".json")
        if aas_io.load_json(twin) != aas_io.load_json(base):
            if check:
                problems.append(f"{rel(twin)}: differs from {base.name}")
            else:
                twin.write_bytes(base.read_bytes())
                print(f"  synced {twin.name} <- {base.name}")

    for aasx in sorted(folder.glob("*.aasx")):
        src = repo.source_json(aasx)
        if src is None:
            continue  # no JSON source (e.g. a sample package): not managed here
        try:
            version = aas_io.aasx_version(aasx)
            published = aas_io.jsonable_from_aasx(aasx, version)
            model = aas_io.with_package_thumbnails(aas_io.load_json(src), published)
            want = aas_io.normalized(model, version)
        except Exception as e:  # unreadable package or JSON aas-core cannot parse
            problems.append(f"{rel(aasx)}: cannot build from {src.name}: {e}")
            continue
        if published == want:
            print(f"  up to date  {aasx.name} (AAS {version})")
            continue
        if check:
            diffs = aas_io.diff_paths(want, published, limit=3)
            detail = "; ".join(f"{p}: JSON {a!r} vs AASX {b!r}" for p, a, b in diffs)
            problems.append(f"{rel(aasx)}: does not match {src.name} ({detail})")
            continue
        aas_io.write_aasx(aasx, aasx, aas_io.xml_from_json(model, version))
        if aas_io.jsonable_from_aasx(aasx, version) != want:
            problems.append(f"{rel(aasx)}: rebuilt package still differs from {src.name}")
        else:
            print(f"  rebuilt     {aasx.name} (AAS {version}) from {src.name}")
    return problems


def changed_folders(ref: str) -> list:
    """Release folders with a JSON/AASX added or changed since ``ref``."""
    base = repo.git("merge-base", ref, "HEAD").strip()
    names = repo.git("diff", "--name-only", "--diff-filter=AMR", base).splitlines()
    names += repo.git("ls-files", "--others", "--exclude-standard").splitlines()
    folders = set()
    for n in names:
        p = repo.ROOT / n
        if n.startswith("published/") and p.suffix.lower() in (".json", ".aasx") and p.exists():
            folders.add(p.parent)
    return sorted(folders)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folders", nargs="*", type=pathlib.Path)
    ap.add_argument("--check", action="store_true", help="only report, write nothing")
    ap.add_argument("--changed-since", metavar="REF", help="also take every release folder changed since REF")
    args = ap.parse_args()

    folders = [f.resolve() for f in args.folders]
    if args.changed_since:
        folders += changed_folders(args.changed_since)
    if not folders:
        print("No release folders to build.")
        return 0

    problems = []
    for folder in sorted(set(folders)):
        print(f"{folder.relative_to(repo.ROOT).as_posix()}:")
        problems += build_folder(folder, args.check)
    for p in problems:
        print(f"::error::{p}")
    if problems:
        hint = " Run: python tools/build_aasx.py <folder>" if args.check else ""
        print(f"\n{len(problems)} problem(s).{hint}")
        return 1
    print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
