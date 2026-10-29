## Time Series Data bug-fix version 1.1.3

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.1.2, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02008-1-1-3_Template_TimeSeriesData.json
- JSON: IDTA 02008-1-1-3_Template_withOperations_TimeSeriesData.json
- AASX: IDTA 02008-1-1-3_Template_TimeSeriesData.aasx (AAS metamodel V3.0)
- AASX: IDTA 02008-1-1-3_Template_TimeSeriesData_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- AASX: IDTA 02008-1-1-3_Template_withOperations_TimeSeriesData.aasx (AAS metamodel V3.0)
- AASX: IDTA 02008-1-1-3_Template_withOperations_TimeSeriesData_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- PDF: IDTA 02008-1-1_Submodel_TimeSeriesData.pdf (corrected: Table 3 no longer gives ordered/allowDuplicated for the SMC Record)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)
- specification PDF: Table 3 no longer states "ordered = true" and "allowDuplicated = true" for the SubmodelElementCollection Record; these attributes exist only for SubmodelElementLists (#246)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
- [#246](https://github.com/admin-shell-io/submodel-templates/issues/246)
