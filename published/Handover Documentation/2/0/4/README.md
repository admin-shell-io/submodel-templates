## Handover Documentation bug-fix version 2.0.4

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 2.0.3, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02004-2-0-4_Template_HandoverDocumentation.json
- JSON: IDTA 02004-2-0-4_Template_HandoverDocumentation__forAASMetamodelV3.1.json
- AASX: IDTA 02004-2-0-4_Template_HandoverDocumentation.aasx (AAS metamodel V3.0)
- AASX: IDTA 02004-2-0-4_Template_HandoverDocumentation__forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- AASX: IDTA 02004-2-0-4_Template_sample_HandoverDocumentation_forAASMetamodelV3.1.aasx (no JSON source; copied unchanged)
- AASX: IDTA 02004-2-0_Template_sample_HandoverDocumentation.aasx (no JSON source; copied unchanged)
- PDF: [IDTA 02004-2-0_Submodel_Handover Documentation.pdf](../IDTA%2002004-2-0_Submodel_Handover%20Documentation.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)
- AllowedIdShort qualifier is a valid regular expression: PreviewFile\d{2,3} (#151)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
- [#151](https://github.com/admin-shell-io/submodel-templates/issues/151)
