## Technical_Data bug-fix version 2.0.4

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 2.0.3, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02003_2-0-4_Template_TechnicalData.json
- AASX: IDTA 02003_2-0-4_Template_TechnicalData.aasx (AAS metamodel V3.0)
- AASX: IDTA 02003_2-0-4_Template_TechnicalData_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- AASX: IDTA 02003_Sample_TechnicalData.aasx (no JSON source; copied unchanged)
- AASX: IDTA 02003_Sample_TechnicalData_forAASMetamodelV3.1.aasx (no JSON source; copied unchanged)
- PDF: [IDTA 02003_Template_TechnicalData.pdf](../IDTA%2002003_Template_TechnicalData.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
