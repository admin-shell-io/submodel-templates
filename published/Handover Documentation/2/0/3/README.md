## Handover Documentation bug-fix version 2.0.3

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 2.0.2, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02004-2-0-3_Template_HandoverDocumentation.json
- JSON: IDTA 02004-2-0-3_Template_HandoverDocumentation__forAASMetamodelV3.1.json
- AASX: IDTA 02004-2-0-3_Template_HandoverDocumentation.aasx (AAS metamodel V3.0)
- AASX: IDTA 02004-2-0-3_Template_HandoverDocumentation__forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- AASX: IDTA 02004-2-0-3_Template_sample_HandoverDocumentation_forAASMetamodelV3.1.aasx (no JSON source; copied unchanged)
- AASX: IDTA 02004-2-0_Template_sample_HandoverDocumentation.aasx (no JSON source; copied unchanged)
- PDF: [IDTA 02004-2-0-1_Submodel_Handover Documentation.pdf](../1/IDTA%2002004-2-0-1_Submodel_Handover%20Documentation.pdf) (unchanged, not copied)

### Corrections

- trailing spaces removed from language strings (8 places) (#207)
- DocumentVersion: 'az' entry and English German text replaced by 'Dokumentenversion' (2 places) (#207)
- 'identifyer' corrected to 'identifier' (3 places) (#236)
- deprecated 'category' attribute removed (21 places) (#207)

### Issues fixed in this release

- [#207](https://github.com/admin-shell-io/submodel-templates/issues/207)
- [#236](https://github.com/admin-shell-io/submodel-templates/issues/236)
