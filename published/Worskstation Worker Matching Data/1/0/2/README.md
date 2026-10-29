## Worskstation Worker Matching Data bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.1, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02046-1-0-2_Template_WWMD.json
- AASX: IDTA 02046-1-0-2_Template_WWMD.aasx (AAS metamodel V3.0)
- AASX: IDTA 02046-1-0-2_Template_WWMD_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02046-1-0_Submodel_WorkstationWorkerMatchingData.pdf](../IDTA%2002046-1-0_Submodel_WorkstationWorkerMatchingData.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)
- submodel semanticId set to the value of the specification (#224)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
