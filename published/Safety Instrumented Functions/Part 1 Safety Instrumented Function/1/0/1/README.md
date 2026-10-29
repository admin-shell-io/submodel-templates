## Safety Instrumented Functions - Part 1 Safety Instrumented Function bug-fix version 1.0.1

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02064_Example_SafetyInstrumentedFunction.json
- JSON: IDTA 02064_Template_SafetyInstrumentedFunction.json
- AASX: IDTA 02064_Example_SafetyInstrumentedFunction.aasx (AAS metamodel V3.0)
- AASX: IDTA 02064_Example_SafetyInstrumentedFunction_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- AASX: IDTA 02064_Template_SafetyInstrumentedFunction.aasx (AAS metamodel V3.0)
- AASX: IDTA 02064_Template_SafetyInstrumentedFunction_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02064_Submodel_SafetyInstrumentedFunction.pdf](../IDTA%2002064_Submodel_SafetyInstrumentedFunction.pdf) (unchanged, not copied)

### Corrections

- cardinality qualifiers get kind TemplateQualifier (2 places) (#159)

### Issues fixed in this release

- [#159](https://github.com/admin-shell-io/submodel-templates/issues/159)
