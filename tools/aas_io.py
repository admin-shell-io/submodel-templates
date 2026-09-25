"""Shared helpers: read a template JSON, write it into an AASX, compare the two.

The JSON file is the single source of a release. An AASX is a zip package whose
only model-bearing part is one ``*.aas.xml`` file; everything else in it
(relationships, content types, supplementary images) is carried over unchanged
from the package the AASX is built on. The XML is produced from the JSON with
aas-core, one library per AAS metamodel version, so a 3.0 and a 3.1 package
differ only in what that metamodel's serializer emits.
"""

import importlib
import io
import json
import pathlib
import re
import xml.etree.ElementTree as ET
import zipfile

# AAS metamodel version -> (pip package, importable module names). The
# aas-core3.0 package (up to at least 1.1.4) installs its module as ``aas_core3``.
_AAS_CORE = {
    "3.0": ("aas-core3.0", ("aas_core3_0", "aas_core3")),
    "3.1": ("aas-core3.1", ("aas_core3_1",)),
}

_NS_RE = re.compile(rb'xmlns(?::\w+)?="https://admin-shell\.io/aas/(\d+)/(\d+)"')
_V_SUFFIX_RE = re.compile(r"_forAASMetamodelV(\d+\.\d+)$")
_REL_TARGET_RE = re.compile(r'Target="([^"]+)"')


def supported_versions() -> list:
    return sorted(_AAS_CORE)


def _lib(version: str):
    if version not in _AAS_CORE:
        raise ValueError(
            f"AAS metamodel {version} is not supported; known: {', '.join(supported_versions())}"
        )
    package, modules = _AAS_CORE[version]
    for name in modules:
        try:
            return (
                importlib.import_module(f"{name}.jsonization"),
                importlib.import_module(f"{name}.xmlization"),
            )
        except ImportError:
            continue
    raise RuntimeError(f"AAS metamodel {version} needs the Python package {package}")


def load_json(path: pathlib.Path) -> dict:
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


def env_from_json(jsonable: dict, version: str):
    jsonization, _ = _lib(version)
    return jsonization.environment_from_jsonable(jsonable)


def xml_from_json(jsonable: dict, version: str) -> bytes:
    """Serialize the environment in ``jsonable`` as AAS XML of ``version``."""
    _, xmlization = _lib(version)
    text = xmlization.to_str(env_from_json(jsonable, version))
    root = ET.fromstring(text)
    ET.indent(root, space="  ")
    ET.register_namespace("", f"https://admin-shell.io/aas/{version.replace('.', '/')}")
    body = ET.tostring(root, encoding="unicode")
    return ('<?xml version="1.0" encoding="utf-8"?>\n' + body + "\n").encode("utf-8")


def aasx_xml_member(z: zipfile.ZipFile) -> str:
    """Name of the AAS XML part inside an AASX package.

    Found the way the AASX format defines it: the package's aasx-origin
    relationships point at the aas-spec part, whatever it is called
    (``*.aas.xml`` in most packages, ``data.xml`` in some).
    """
    names = z.namelist()
    rels = [n for n in names if n.lower().endswith("aasx-origin.rels")]
    specs = []
    if rels:
        specs = [t.lstrip("/") for t in _REL_TARGET_RE.findall(z.read(rels[0]).decode("utf-8-sig"))]
        specs = [s for s in specs if s in names and s.lower().endswith(".xml")]
    if not specs:
        specs = [n for n in names if n.lower().endswith(".aas.xml")]
    if len(specs) != 1:
        raise ValueError(f"expected exactly one AAS XML part, found {len(specs)}")
    return specs[0]


def aasx_version(path: pathlib.Path) -> str:
    """Metamodel version of an AASX, read from the XML namespace inside it."""
    with zipfile.ZipFile(path) as z:
        head = z.read(aasx_xml_member(z))[:2000]
    m = _NS_RE.search(head)
    if not m:
        raise ValueError(f"{path.name}: no AAS XML namespace found")
    return f"{int(m.group(1))}.{int(m.group(2))}"


def version_from_name(path: pathlib.Path, default: str = "3.0") -> str:
    """Metamodel version an AASX *should* have, by the repo naming convention.

    ``..._forAASMetamodelV3.1.aasx`` targets 3.1; a name without the suffix is the
    3.0 package.
    """
    m = _V_SUFFIX_RE.search(path.stem)
    return m.group(1) if m else default


def jsonable_from_aasx(path: pathlib.Path, version: str = None) -> dict:
    """Parse the AAS XML inside an AASX and return it in JSON form (normalized)."""
    version = version or aasx_version(path)
    jsonization, xmlization = _lib(version)
    with zipfile.ZipFile(path) as z:
        data = z.read(aasx_xml_member(z))
    env = xmlization.environment_from_str(data.decode("utf-8-sig"))
    return jsonization.to_jsonable(env)


def with_package_thumbnails(jsonable: dict, package: dict) -> dict:
    """Carry the package's AAS thumbnails over to a JSON that lacks them.

    ``assetInformation.defaultThumbnail`` points at an image inside the AASX. Many
    template JSONs are exported without it, while the package has one; building
    the package from the JSON alone would silently drop the cover image. A
    thumbnail the JSON does define always wins.
    """
    by_id = {
        aas.get("id"): aas.get("assetInformation", {}).get("defaultThumbnail")
        for aas in package.get("assetAdministrationShells", [])
    }
    out = json.loads(json.dumps(jsonable))
    for aas in out.get("assetAdministrationShells", []):
        info = aas.get("assetInformation")
        thumb = by_id.get(aas.get("id"))
        if info is not None and thumb and "defaultThumbnail" not in info:
            info["defaultThumbnail"] = thumb
    return out


def normalized(jsonable: dict, version: str) -> dict:
    """Round-trip through aas-core so that two equal models compare equal."""
    jsonization, _ = _lib(version)
    return jsonization.to_jsonable(env_from_json(jsonable, version))


def write_aasx(shell: pathlib.Path, out: pathlib.Path, xml: bytes) -> None:
    """Write ``out`` as a copy of the ``shell`` package with its AAS XML replaced.

    Every other part keeps its bytes, name, order, timestamp and compression, so
    rebuilding from an unchanged JSON reproduces the same package.
    """
    buf = io.BytesIO()
    with zipfile.ZipFile(shell) as src, zipfile.ZipFile(buf, "w") as dst:
        target = aasx_xml_member(src)
        for info in src.infolist():
            data = xml if info.filename == target else src.read(info)
            dst.writestr(info, data, compress_type=info.compress_type)
    out.write_bytes(buf.getvalue())


def diff_paths(a, b, path="", out=None, limit=20):
    """List the first ``limit`` leaf paths where two JSON values differ."""
    out = [] if out is None else out
    if len(out) >= limit:
        return out
    if type(a) is not type(b):
        out.append((path or "/", a, b))
    elif isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append((f"{path}/{k}", a.get(k, "<missing>"), b.get(k, "<missing>")))
            else:
                diff_paths(a[k], b[k], f"{path}/{k}", out, limit)
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append((path, f"{len(a)} items", f"{len(b)} items"))
        for i, (x, y) in enumerate(zip(a, b)):
            diff_paths(x, y, f"{path}[{i}]", out, limit)
    elif a != b:
        out.append((path, a, b))
    return out[:limit]
