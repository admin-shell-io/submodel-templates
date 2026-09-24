## Provision of Simulation Models bug-fix version 1.2

This folder contains a bug-fix release of the submodel template artifacts.
It was produced from version 1.1 and contains only corrections to the
machine-readable artifacts (JSON and AASX). The artifacts of 1.1 are
unchanged. The specification PDF, where present, is carried over unchanged.

### Artifacts in this directory

- AASX: IDTA 02005_Template_ProvisionOfSimulationModel.aasx
- JSON: IDTA 02005_Template_ProvisionOfSimulationModel.json

### Corrections applied

- **Qualifier kind** ([#159](https://github.com/admin-shell-io/submodel-templates/issues/159)).
  Qualifiers constraining the submodel template itself carried
  `kind: ConceptQualifier`. A qualifier that restricts the template rather than
  the concept it is based on must carry `kind: TemplateQualifier`. Corrected in
  every JSON and AASX artifact in this folder (75 occurrences per JSON
  artifact).

### Verification

- Every JSON artifact deserializes and was re-verified with `aas-core3`.
- Every AASX package opens as a valid OPC package with a well-formed XML
  payload; all non-payload package entries are byte-identical to version 1.1.
