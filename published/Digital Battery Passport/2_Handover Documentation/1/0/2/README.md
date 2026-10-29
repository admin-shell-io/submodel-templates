## Digital Battery Passport - 2_Handover Documentation bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.1, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02035-2_DBP-Part-2_HandoverDocumentation.json
- JSON: IDTA 02035-2_DBP-Part-2_HandoverDocumentation_without_examplevalues.json
- AASX: IDTA 02035-2_DBP-Part-2_HandoverDocumentation.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02035-2_DBP-Part-2_HandoverDocumentation.pdf](../IDTA%2002035-2_DBP-Part-2_HandoverDocumentation.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
