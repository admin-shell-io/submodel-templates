## Service Request Notification bug-fix version 1.0.2

This folder contains the bug-fix release of the submodel template artifacts.
It builds on version 1.0.1; the artifacts of 1.0.1 are unchanged.

### Artifacts in this directory

- AASX: IDTA 02010-1-0-2_Template_ServiceRequestNotification.aasx (AAS metamodel V3.0)
- AASX: IDTA 02010-1-0-2_Template_ServiceRequestNotification_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- JSON: IDTA 02010-1-0-2_Template_ServiceRequestNotification.json
- JSON: IDTA 02010-1-0-2_Template_ServiceRequestNotification_forAASMetamodelV3.1.json
- PDF: IDTA 02010-1-0_Submodel_ServiceRequestNotification.pdf (unchanged)

### Bug fixes applied in 1.0.2

- [#58](https://github.com/admin-shell-io/submodel-templates/issues/58) -
  Deprecated category fields in Service Request Notification.
  The deprecated `category` field (value `PARAMETER`) was populated on
  ConceptDescriptions and SubmodelElements, which causes schema-conformant APIs to
  reject the template. All 27 occurrences per artifact were removed, from both the
  JSON and the AASX XML payload (54 removals per format across the two variants).

### Additional corrections

- Whitespace embedded in semantic identifier URIs (for example
  `https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation `)
  was removed so that exact identifier matching succeeds. 8 occurrences before, 0 after.
