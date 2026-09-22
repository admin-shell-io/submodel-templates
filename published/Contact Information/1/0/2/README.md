## Contact Information bug-fix version 1.0.2

This folder contains the bug-fix release of the submodel template artifacts.
It builds on version 1.0.1; the artifacts of 1.0.1 are unchanged.

### Artifacts in this directory

- AASX: IDTA 02002-1-0-2_Template_ContactInformation.aasx (AAS metamodel V3.0)
- AASX: IDTA 02002-1-0-2_Template_ContactInformation_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- JSON: IDTA 02002-1-0-2_Template_ContactInformation.json
- JSON: IDTA 02002-1-0-2_Template_ContactInformation_forAASMetamodelV3.1.json
- PDF: IDTA 02002-1-0_Submodel_ContactInformation.pdf (unchanged)

### Bug fixes applied in 1.0.2

- [#206](https://github.com/admin-shell-io/submodel-templates/issues/206) -
  ContactInformations v1.0.1 wrong semanticId for SMC IPCommunication.
  The `IPCommunication__00__` collection referenced
  `.../ContactInformations/IPCommunication/`, which omits the
  `ContactInformation` path segment. It now references
  `.../ContactInformations/ContactInformation/IPCommunication/`, consistent with
  the namespace used by the template's own ConceptDescriptions (for example
  `.../ContactInformations/ContactInformation/IPCommunication/TypeOfCommunication`).

- [#210](https://github.com/admin-shell-io/submodel-templates/issues/210) -
  [ContactInformation 1.0.1] Several Issues.
  The whitespace embedded inside semanticId values
  (`https://admin-shell.io/zvei/nameplate/1/0/ ContactInformations/...`), which
  prevented exact identifier matching, has been removed. Identifier values and the
  references pointing at them were corrected together so that they continue to
  resolve.

  Note: the issue also reports missing administration/version information on the
  submodel. That part is not addressed here, as it requires deciding the version
  and revision values to publish.

### Verification

- Both JSON artifacts deserialize and pass `aas-core3` constraint verification
  with 0 violations.
- Both AASX packages open as valid OPC packages with well-formed XML payloads.
  All non-payload package entries are byte-identical to version 1.0.1.
- Whitespace-bearing identifier URIs: 4 before, 0 after.
