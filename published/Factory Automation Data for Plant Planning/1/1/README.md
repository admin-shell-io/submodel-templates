## Factory Automation Data for Plant Planning bug-fix version 1.1

This folder contains a bug-fix release of the submodel template artifacts.
It was produced from version 1 and contains only corrections to the
machine-readable artifacts (JSON and AASX). The specification PDF, where present,
is carried over unchanged.

### Artifacts in this directory

- PDF: IDTA 02075_Submodel_FactoryAutomationDataForPlantPlanning.pdf (unchanged)
- AASX: IDTA 02075_Template_FactoryAutomationDataForPlantPlanning.aasx
- JSON: IDTA 02075_Template_FactoryAutomationDataForPlantPlanning.json

### Issues fixed in this release

- [#187](https://github.com/admin-shell-io/submodel-templates/issues/187)
- [#207](https://github.com/admin-shell-io/submodel-templates/issues/207)
- [#208](https://github.com/admin-shell-io/submodel-templates/issues/208)
- [#210](https://github.com/admin-shell-io/submodel-templates/issues/210)

### Known remaining issues

These were not corrected here, because the correct value is not determinable from the template alone.

- **The value must represent a valid file URI scheme according t** (2): File elements reference packaged files as `/aasx/files/...`. This is the convention used across this repository (84 occurrences) and is how AASX Package Explorer addresses files inside the package, but `aas-core3` expects an RFC 8089 `file:` URI. This was left unchanged deliberately: rewriting it would break the packaged-file references that real tooling resolves today. It needs a repository-wide decision, not a per-template fix.
- **AASd-128** (1): A SubmodelElementList index reference does not match the expected form. Correcting it requires knowing the intended target element.
