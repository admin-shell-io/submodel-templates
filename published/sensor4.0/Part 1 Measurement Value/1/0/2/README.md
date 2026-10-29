## sensor4.0 - Part 1 Measurement Value bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.1, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02029-1-0-2_Template_Sensor4.0_MeasurementValue.json
- AASX: IDTA 02029-1-0-2_Template_Sensor4.0_MeasurementValue.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02029-1_Template_Sensor4.0_MeasurementValue.pdf](../IDTA%2002029-1_Template_Sensor4.0_MeasurementValue.pdf) (unchanged, not copied)

### Corrections

- Quality: SMT/AllowedValue is a TemplateQualifier with the regex 'good|bad|uncertain|others' (#303)
- administration (version 1, revision 0) added

### Issues fixed in this release

- [#303](https://github.com/admin-shell-io/submodel-templates/issues/303)
