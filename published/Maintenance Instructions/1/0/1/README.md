## Maintenance Instructions bug-fix version 1.0.1

This folder contains the bug-fix release of the submodel template artifacts.
The specification PDF is carried over from version 1.0 unchanged.

### Artifacts in this directory

- AASX: IDTA_02018-1-0-1_Template_MaintenanceInstructions.aasx
- JSON: IDTA_02018-1-0-1_Template_MaintenanceInstructions.json
- PDF: IDTA_02018_Submodel_MaintenanceInstructions.pdf (unchanged from version 1.0)

### Issues fixed in this release

- [#245](https://github.com/admin-shell-io/submodel-templates/issues/245)

### Issues reviewed but not changed

- [#279](https://github.com/admin-shell-io/submodel-templates/issues/279) -
  Maintenance Instructions: typos in cardinalities. The reported invalid
  multiplicity literals (`ZerotoMany`, `ZerotToOne`) are not present in version
  1.0; only valid `ZeroToOne`, `ZeroToMany` and `One` values occur, and the
  `SparePart` spelling is consistent throughout. This issue appears to have been
  fixed already and can be confirmed and closed.
