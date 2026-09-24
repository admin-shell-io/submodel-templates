## MTP bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It was produced from version 1.0.1 and contains only corrections to the
machine-readable artifacts (JSON and AASX). The artifacts of 1.0.1 are
unchanged. The specification PDF, where present, is carried over unchanged.

### Artifacts in this directory

- AASX: IDTA_02001-1-0-2_Submodel_MTPv1.0-rc2-with-documentation1_en.aasx
- JSON: IDTA_02001-1-0-2_Submodel_MTPv1.0-rc2-with-documentation1_en.json
- AASX: IDTA_02001-1-0-2_Submodel_MTPv1.0-rc2-with-documentation1_en_forAASMetamodelV3.1.aasx
- JSON: IDTA_02001-1-0-2_Submodel_MTPv1.0-rc2-with-documentation1_en_forAASMetamodelV3.1.json

### Corrections applied

- **Qualifier kind** ([#159](https://github.com/admin-shell-io/submodel-templates/issues/159)).
  Qualifiers constraining the submodel template itself carried
  `kind: ConceptQualifier`. A qualifier that restricts the template rather than
  the concept it is based on must carry `kind: TemplateQualifier`. Corrected in
  every JSON and AASX artifact in this folder (13 occurrences per JSON
  artifact).
