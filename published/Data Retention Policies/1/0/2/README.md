## Data Retention Policies bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It was produced from version 1.0.1 and contains only corrections to the
machine-readable artifacts (JSON and AASX). The artifacts of 1.0.1 are
unchanged. The specification PDF, where present, is carried over unchanged.

### Artifacts in this directory

- AASX: IDTA 02056-1-0-2_Template_Data Retention Policies.aasx
- JSON: IDTA 02056-1-0-2_Template_Data Retention Policies.json
- AASX: IDTA 02056-1-0-2_Template_Data Retention Policies_forAASMetamodelV3.1.aasx
- JSON: IDTA 02056-1-0-2_Template_Data Retention Policies_forAASMetamodelV3.1.json

### Corrections applied

- **Qualifier kind** ([#159](https://github.com/admin-shell-io/submodel-templates/issues/159)).
  Qualifiers constraining the submodel template itself carried
  `kind: ConceptQualifier`. A qualifier that restricts the template rather than
  the concept it is based on must carry `kind: TemplateQualifier`. Corrected in
  every JSON and AASX artifact in this folder (25 occurrences per JSON
  artifact).

### Verification

- Every JSON artifact deserializes and was re-verified with `aas-core3`.
- Every AASX package opens as a valid OPC package with a well-formed XML
  payload; all non-payload package entries are byte-identical to version 1.0.1.
