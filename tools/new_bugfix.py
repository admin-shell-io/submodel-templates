#! /usr/bin/env python3
"""Create (or extend) the bug-fix release folder for an SMT version.

    python tools/new_bugfix.py --labels "bugfix,IDTA 02002,v1.0" --issue 206
    python tools/new_bugfix.py --smt "IDTA 02002" --version 1.0 --issue 206 --issue 210

The newest release under published/<SMT>/<major>/<minor>/ is the starting point.

* If that newest folder is already released (it exists on --base-ref, default
  origin/main), the next bug-fix folder is created: the template JSON is copied
  with the version in its file name bumped, the AASX packages are copied and
  rebuilt from the JSON, and a README is written that links to the unchanged PDF
  instead of copying it.
* If it is not released yet (an open bug-fix branch), no new folder is made; the
  issue is only added to that folder's README. Several issues for one SMT
  version therefore end up in one bug-fix release.

AASX packages follow tools/smt-config.yml ``aas_versions``: a version the
previous release had but the config no longer lists is dropped; a configured
version newer than all of the previous release's is added. No older metamodel
version is ever added back.
"""

import argparse
import os
import pathlib
import re
import shutil
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import aas_io  # noqa: E402
import build_aasx  # noqa: E402
import repo  # noqa: E402

ISSUES_HEADING = "### Issues fixed in this release"


class UserError(Exception):
    """A problem the issue author or maintainer has to fix (bad labels etc.)."""


class Incomplete(UserError):
    """Not all three labels are on the issue yet; nothing to do so far."""


def parse_labels(labels: list, cfg: dict) -> tuple:
    smts = [l for l in labels if l in cfg["smts"]]
    prefix = cfg["version_label_prefix"]
    versions = [l[len(prefix):] for l in labels if re.fullmatch(re.escape(prefix) + r"\d+\.\d+", l)]
    if cfg["bugfix_label"] not in labels:
        raise Incomplete(f"the issue has no '{cfg['bugfix_label']}' label")
    if not smts:
        raise Incomplete("expected exactly one SMT label (e.g. 'IDTA 02006'), found none")
    if not versions:
        raise Incomplete(f"expected exactly one version label (e.g. '{prefix}3.0'), found none")
    if len(smts) > 1:
        raise UserError(f"expected exactly one SMT label, found {smts}; open one issue per SMT")
    if len(versions) > 1:
        raise UserError(f"expected exactly one version label, found {[prefix + v for v in versions]}")
    return smts[0], versions[0]


def token(release: tuple) -> str:
    """Version as used in file names: (1, 0, 2) -> '1-0-2', (1, 0, 0) -> '1-0'."""
    return "-".join(str(n) for n in (release if release[2] else release[:2]))


def bump_name(name: str, old: tuple, new: tuple) -> str:
    """Replace the release version in a file name, if the name carries one.

    'IDTA 02002-1-0-1_Template_X.json' -> 'IDTA 02002-1-0-2_Template_X.json'.
    Names without a version (e.g. 'IDTA 02035-4_DBP-Part-4_TechnicalData.json')
    are kept, as earlier bug-fix releases of those SMTs did.
    """
    return re.sub(rf"(?<!\d){re.escape(token(old))}(?![\d]|-\d)", token(new), name, count=1)


def find_pdf(src: pathlib.Path, vfolder: pathlib.Path):
    """The specification PDF of ``src``, as its oldest identical copy.

    Bug-fix folders used to carry a copy of the PDF; linking the oldest folder
    that holds the same bytes (normally the base x/y folder) keeps the link
    working when newer bug-fix folders are later moved to deprecated/.
    """
    pdfs = sorted(src.glob("*.pdf")) or sorted(vfolder.glob("*.pdf"))
    if not pdfs:
        return None
    data = pdfs[0].read_bytes()
    for folder in [vfolder, *repo.patch_folders(vfolder)]:
        for p in sorted(folder.glob("*.pdf")):
            if p.stat().st_size == len(data) and p.read_bytes() == data:
                return p
    return pdfs[0]


def md_link(target: pathlib.Path, start: pathlib.Path) -> str:
    rel = os.path.relpath(target, start).replace(os.sep, "/")
    return f"[{target.name}]({urllib.parse.quote(rel)})"


def issue_line(n: int) -> str:
    return f"- [#{n}](https://github.com/{repo.repo_slug()}/issues/{n})"


def add_issues_to_readme(readme: pathlib.Path, issues: list) -> list:
    text = readme.read_text(encoding="utf-8")
    added = [n for n in issues if f"/issues/{n})" not in text]
    if not added:
        return []
    lines = "\n".join(issue_line(n) for n in added)
    if ISSUES_HEADING in text:
        text = text.rstrip("\n") + "\n" + lines + "\n"
    else:
        text = text.rstrip("\n") + f"\n\n{ISSUES_HEADING}\n\n{lines}\n"
    readme.write_text(text, encoding="utf-8")
    return added


def plan_packages(src: pathlib.Path, aas_versions: list) -> list:
    """(source AASX, AAS version) pairs the new release gets, per template JSON."""
    wanted = set(aas_versions)
    plan = []
    groups = {}
    for aasx in sorted(src.glob("*.aasx")):
        j = repo.source_json(aasx)
        if j is None:
            plan.append((aasx, None))  # no JSON source: copied as it is
            continue
        groups.setdefault(j, []).append((aasx, aas_io.aasx_version(aasx)))
    for j, pkgs in groups.items():
        have = {v for _, v in pkgs}
        newest = max(have, key=lambda v: tuple(map(int, v.split("."))))
        shell = next(a for a, v in pkgs if v == newest)
        for aasx, v in pkgs:
            if v in wanted:
                plan.append((aasx, v))
        for v in sorted(wanted - have):
            if tuple(map(int, v.split("."))) > tuple(map(int, newest.split("."))):
                plan.append((shell, v))  # new metamodel: built on the newest package
    return plan


def package_name(src_aasx: pathlib.Path, json_stem: str, version: str) -> str:
    """Keep the source package's name for its own version; name an added
    version ``<json stem>_forAASMetamodelV<version>.aasx``."""
    if src_aasx.stem in (json_stem, f"{json_stem}_forAASMetamodelV{version}"):
        return None
    return f"{json_stem}_forAASMetamodelV{version}.aasx"


def create_release(vfolder: pathlib.Path, src: pathlib.Path, cfg: dict, smt_label: str, issues: list) -> pathlib.Path:
    old = repo.release_of(src)
    new = (old[0], old[1], old[2] + 1)
    dst = vfolder / str(new[2])
    if dst.exists():
        raise UserError(f"{dst.relative_to(repo.ROOT).as_posix()} already exists")
    dst.mkdir()
    artifacts = []

    for j in sorted(src.glob("*.json")):
        if repo.is_twin_json(j):
            continue  # identical copy of the plain JSON; not carried forward
        target = dst / bump_name(j.name, old, new)
        shutil.copyfile(j, target)
        artifacts.append(f"- JSON: {target.name}")

    for aasx, version in plan_packages(src, cfg["aas_versions"]):
        name = bump_name(aasx.name, old, new)
        if version is not None:
            j = repo.source_json(aasx)
            renamed = package_name(aasx, j.stem, version)
            if renamed:
                name = bump_name(renamed, old, new)
        target = dst / name
        shutil.copyfile(aasx, target)
        if version is not None and aas_io.aasx_version(target) != version:
            # new metamodel version: rewrite the model part in that version
            model = aas_io.load_json(dst / bump_name(repo.source_json(aasx).name, old, new))
            aas_io.write_aasx(target, target, aas_io.xml_from_json(model, version))
        suffix = f" (AAS metamodel V{version})" if version else " (no JSON source; copied unchanged)"
        artifacts.append(f"- AASX: {target.name}{suffix}")

    problems = build_aasx.build_folder(dst, check=False)
    if problems:
        raise RuntimeError("; ".join(problems))

    pdf = find_pdf(src, vfolder)
    if pdf:
        artifacts.append(f"- PDF: {md_link(pdf, dst)} (unchanged, not copied)")

    name = cfg["smts"][smt_label].replace("/", " - ")
    readme = [
        f"## {name} bug-fix version {'.'.join(map(str, new))}",
        "",
        "This folder contains a bug-fix release of the submodel template artifacts.",
        f"It builds on version {'.'.join(map(str, old[:2] if not old[2] else old))}, whose artifacts are unchanged.",
        "The AASX packages are generated from the template JSON (tools/build_aasx.py).",
        "",
        "### Artifacts in this directory",
        "",
        *artifacts,
        "",
        ISSUES_HEADING,
        "",
        *(issue_line(n) for n in issues),
        "",
    ]
    (dst / "README.md").write_text("\n".join(readme), encoding="utf-8")
    return dst


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--labels", help="comma-separated issue labels")
    ap.add_argument("--smt", help="SMT label, e.g. 'IDTA 02002' (instead of --labels)")
    ap.add_argument("--version", help="SMT version, e.g. 1.0 (instead of --labels)")
    ap.add_argument("--issue", type=int, action="append", default=[], required=True)
    ap.add_argument("--base-ref", default="origin/main", help="what counts as released (default origin/main)")
    ap.add_argument("--resolve-only", action="store_true",
                    help="only validate the labels and print the branch name; change nothing")
    args = ap.parse_args()
    cfg = repo.load_config()

    try:
        if args.labels:
            smt, version = parse_labels([l.strip() for l in args.labels.split(",") if l.strip()], cfg)
        elif args.smt and args.version:
            if args.smt not in cfg["smts"]:
                raise UserError(f"unknown SMT label '{args.smt}' (see tools/smt-config.yml)")
            smt, version = args.smt, args.version
        else:
            raise UserError("give --labels, or --smt and --version")

        vfolder = repo.version_folder(cfg["smts"][smt], version)
        if not vfolder.is_dir():
            raise UserError(f"no folder for {smt} v{version}: {vfolder.relative_to(repo.ROOT).as_posix()}")
        branch = f"bugfix/{smt.replace(' ', '-')}-v{version}"
        if args.resolve_only:
            repo.set_output(branch=branch, smt=smt, version=version)
            print(f"branch={branch}")
            return 0
        patches = repo.patch_folders(vfolder)
        newest = patches[-1] if patches else vfolder

        if patches and not repo.exists_in(args.base_ref, newest):
            added = add_issues_to_readme(newest / "README.md", args.issue)
            folder, created, changed = newest, False, bool(added)
            print(f"{newest.relative_to(repo.ROOT).as_posix()} is not released yet; "
                  f"added issue(s) {added or '(already listed)'} to its README")
        else:
            folder, created, changed = create_release(vfolder, newest, cfg, smt, args.issue), True, True
            print(f"created {folder.relative_to(repo.ROOT).as_posix()}")
    except Incomplete as e:
        print(f"waiting for labels: {e}")
        return 3
    except UserError as e:
        print(f"::error::{e}")
        repo.set_output(error=str(e))
        return 2

    release = ".".join(map(str, repo.release_of(folder)))
    repo.set_output(folder=folder.relative_to(repo.ROOT).as_posix(), release=release,
                    branch=branch, created=str(created).lower(), changed=str(changed).lower(),
                    smt=smt, version=version)
    print(f"release={release} branch={branch}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
