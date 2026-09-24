## Hierarchical Structures enabling Bills of Material - Extension based on IEC 81346 bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It was produced from version 1.0 and contains only corrections to the
machine-readable artifacts (JSON and AASX). The specification PDF, where present,
is carried over unchanged.

### Artifacts in this directory

- AASX: IDTA 02011-1-1-2 _Template_BoM_ExtensionbasedonIEC81346.aasx
- JSON: IDTA 02011-1-1-2 _Template_BoM_ExtensionbasedonIEC81346.json
- AASX: IDTA 02011-1-1-2 _Template_BoM_ExtensionbasedonIEC81346_forAASMetamodelV3.1.aasx
- JSON: IDTA 02011-1-1-2 _Template_BoM_ExtensionbasedonIEC81346_forAASMetamodelV3.1.json

### Issues fixed in this release

- [#187](https://github.com/admin-shell-io/submodel-templates/issues/187)
- [#207](https://github.com/admin-shell-io/submodel-templates/issues/207)
- [#208](https://github.com/admin-shell-io/submodel-templates/issues/208)
- [#210](https://github.com/admin-shell-io/submodel-templates/issues/210)

### Known remaining issues

These were not corrected here, because the correct value is not determinable from the template alone.

- **AASd-014** (16): `SelfManagedEntity` elements have no `globalAssetId` or `specificAssetIds`. In a template these are placeholders to be filled by an instance, so supplying a value here would invent data. Left for a content decision.
- **The value must represent a valid file URI scheme according t** (2): File elements reference packaged files as `/aasx/files/...`. This is the convention used across this repository (84 occurrences) and is how AASX Package Explorer addresses files inside the package, but `aas-core3` expects an RFC 8089 `file:` URI. This was left unchanged deliberately: rewriting it would break the packaged-file references that real tooling resolves today. It needs a repository-wide decision, not a per-template fix.
