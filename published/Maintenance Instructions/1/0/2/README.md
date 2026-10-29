## Maintenance Instructions bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.1, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA_02018-1-0-2_Template_MaintenanceInstructions.json
- AASX: IDTA_02018-1-0-2_Template_MaintenanceInstructions.aasx (AAS metamodel V3.1)
- PDF: [IDTA_02018_Submodel_MaintenanceInstructions.pdf](../IDTA_02018_Submodel_MaintenanceInstructions.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
