## Predictive Maintenance bug-fix version 1.0.1

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02048_Template_PredictiveMaintenance.json
- AASX: IDTA 02048_Template_PredictiveMaintenance.aasx (AAS metamodel V3.0)
- AASX: IDTA 02048_Template_PredictiveMaintenance_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02048_Submodel_PredictiveMaintenance.pdf](../IDTA%2002048_Submodel_PredictiveMaintenance.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
