## DEXPI bug-fix version 1.0.1

This folder contains a bug-fix release of the submodel template artifacts.
Only the machine-readable artifacts (JSON and AASX) were corrected; the
specification PDF is carried over from version 1.0 unchanged.

### Artifacts in this directory

- AASX: IDTA 02012-1-0-1_Template_DEXPI.aasx
- JSON: IDTA 02012-1-0-1_Template_DEXPI.json
- PDF: IDTA 02012-1-0_Submodel_DEXPI.pdf (unchanged from version 1.0)

### Issues fixed in this release

- [#79](https://github.com/admin-shell-io/submodel-templates/issues/79)
- [#93](https://github.com/admin-shell-io/submodel-templates/issues/93)
- [#94](https://github.com/admin-shell-io/submodel-templates/issues/94)

### Known remaining issues

- [#281](https://github.com/admin-shell-io/submodel-templates/issues/281) -
  DEXPI: missing semantic IDs. 47 elements (for example `ManufacturerName`,
  `DateOfManufacture`, and the `ProcessInstrumentationFunction_*_rel`
  relationship elements) carry no semanticId. Minting new semantic identifiers
  requires authority over the DEXPI namespace, so no identifiers were invented
  here. This needs the DEXPI working group.

- 2 remaining constraint violations: one file-URI form (`/aasx/...` rather than
  an RFC 8089 `file:` URI, the convention used throughout this repository) and
  one related reference. Both predate this release.
