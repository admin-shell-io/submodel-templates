"""Repository layout helpers shared by the bug-fix tools.

Layout: published/<SMT folder>/<major>/<minor>/[<patch>]/ holds one release.
A bug-fix release is the next <patch> folder under its <major>/<minor> folder.
"""

import os
import pathlib
import re
import subprocess

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUBLISHED = ROOT / "published"
CONFIG = pathlib.Path(__file__).resolve().parent / "smt-config.yml"
V_SUFFIX_RE = re.compile(r"_forAASMetamodelV(\d+\.\d+)$")


def load_config() -> dict:
    with open(CONFIG, encoding="utf-8") as f:
        return yaml.safe_load(f)


def version_folder(smt_folder: str, version: str) -> pathlib.Path:
    major, minor = version.split(".")
    return PUBLISHED / smt_folder / major / minor


def patch_folders(vfolder: pathlib.Path) -> list:
    """Bug-fix folders of a version folder, oldest first."""
    return sorted(
        (p for p in vfolder.iterdir() if p.is_dir() and p.name.isdigit()),
        key=lambda p: int(p.name),
    )


def release_of(folder: pathlib.Path) -> tuple:
    """(major, minor, patch) of a release folder; patch 0 for the base folder."""
    parts = folder.relative_to(PUBLISHED).parts
    nums = []
    for p in reversed(parts):
        if not p.isdigit():
            break
        nums.insert(0, int(p))
    if len(nums) == 2:
        nums.append(0)
    if len(nums) != 3:
        raise ValueError(f"not a release folder: {folder}")
    return tuple(nums)


def is_twin_json(path: pathlib.Path) -> bool:
    """A ``*_forAASMetamodelVx.y.json`` copy of a plain JSON in the same folder."""
    if path.suffix.lower() != ".json" or not V_SUFFIX_RE.search(path.stem):
        return False
    return path.with_name(V_SUFFIX_RE.sub("", path.stem) + ".json").exists()


def source_json(aasx: pathlib.Path):
    """The JSON an AASX is built from: same name, or same name without the
    ``_forAASMetamodelVx.y`` suffix. None if the package has no JSON source."""
    for stem in (aasx.stem, V_SUFFIX_RE.sub("", aasx.stem)):
        j = aasx.with_name(stem + ".json")
        if j.exists() and not is_twin_json(j):
            return j
    return None


def git(*args, check=True) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout


def exists_in(ref: str, path: pathlib.Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return bool(git("ls-tree", "--name-only", ref, "--", rel, check=False).strip())


def repo_slug() -> str:
    return os.environ.get("GITHUB_REPOSITORY", "admin-shell-io/submodel-templates")


def set_output(**values) -> None:
    """Expose values to later GitHub Actions steps (no-op outside Actions)."""
    out = os.environ.get("GITHUB_OUTPUT")
    if not out:
        return
    with open(out, "a", encoding="utf-8") as f:
        for k, v in values.items():
            f.write(f"{k}={v}\n")
