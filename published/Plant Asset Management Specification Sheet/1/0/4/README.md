## Plant Asset Management Specification Sheet bug-fix version 1.0.4

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.3, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02019-1-0-4_Template_PlantAssetManagement.json
- AASX: IDTA 02019-1-0-4_Template_PlantAssetManagement.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02019-1-0_Submodel_PlantAssetManagement.pdf](../IDTA%2002019-1-0_Submodel_PlantAssetManagement.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
