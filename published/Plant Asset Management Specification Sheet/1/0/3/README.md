## Plant Asset Management Specification Sheet bug-fix version 1.0.3

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.2, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02019-1-0-3_Template_PlantAssetManagement.json
- AASX: IDTA 02019-1-0-3_Template_PlantAssetManagement.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02019-1-0_Submodel_PlantAssetManagement.pdf](../IDTA%2002019-1-0_Submodel_PlantAssetManagement.pdf) (unchanged, not copied)

### Corrections

- MethodHeader: duplicate FormInfo qualifier (AASd-021) - the first is the FormTitle

### Issues fixed in this release

- [#207](https://github.com/admin-shell-io/submodel-templates/issues/207) (same defect as reported there for Handover Documentation (AASd-021); fixed here as well)
