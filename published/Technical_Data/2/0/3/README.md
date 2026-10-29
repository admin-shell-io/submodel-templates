## Technical_Data bug-fix version 2.0.3

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 2.0.2, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02003_2-0-3_Template_TechnicalData.json
- AASX: IDTA 02003_2-0-3_Template_TechnicalData.aasx (AAS metamodel V3.0)
- AASX: IDTA 02003_2-0-3_Template_TechnicalData_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- AASX: IDTA 02003_Sample_TechnicalData.aasx (no JSON source; copied unchanged)
- AASX: IDTA 02003_Sample_TechnicalData_forAASMetamodelV3.1.aasx (no JSON source; copied unchanged)
- PDF: [IDTA 02003_2-0-1_Template_TechnicalData.pdf](../1/IDTA%2002003_2-0-1_Template_TechnicalData.pdf) (unchanged, not copied)

### Corrections

- 'Technsiche' corrected to 'Technische' (2 places) (#208)
- ClassificationSystem: four SMT/ExampleValue/<choice> qualifiers merged into one SMT/ExampleValue with the ExampleValue semanticId (#208)
- deprecated 'category' attribute removed (28 places) (#208)

### Issues fixed in this release

- [#208](https://github.com/admin-shell-io/submodel-templates/issues/208)
