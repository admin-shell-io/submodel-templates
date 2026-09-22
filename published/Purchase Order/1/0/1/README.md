# Purchase Order (Version 1.0.1)

This is a Submodel template specification for the Asset Administration Shell.

## About this version

This version 1.0.1 is a bug fix release that addresses GitHub issues identified in
version 1.0 of the Purchase Order submodel template. Only the machine-readable
artifacts (JSON and AASX) were corrected; the specification PDF is carried over
from version 1.0 unchanged.

## Artifacts in this directory

- AASX: IDTA-02050-1-0-1_Template_PurchaseOrder.aasx (AAS metamodel V3.0)
- AASX: IDTA-02050-1-0-1_Template_PurchaseOrder_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- JSON: IDTA-02050-1-0-1_Template_PurchaseOrder.json
- JSON: IDTA-02050-1-0-1_Template_PurchaseOrder_forAASMetamodelV3.1.json
- PDF: IDTA-02050_Submodel_PurchaseOrder.pdf (unchanged from version 1.0)

## Changes in Version 1.0.1

### Bug Fixes

- [#223](https://github.com/admin-shell-io/submodel-templates/issues/223) -
  [Purchase Order 1.0] PurchaseRequestResponseReferene typo.
  The misspelled idShort `PurchaseRequestResponseReferene` was corrected to
  `PurchaseRequestResponseReference` (4 occurrences in each artifact).

### Additional corrections

The following defects were found while fixing the above and are corrected here.
They were not raised as separate GitHub issues.

- Whitespace embedded in semantic identifier URIs. 37 `ConceptDescription`
  identifiers and the references pointing at them contained spaces or an escaped
  newline inside the URI (for example
  `https://admin-shell.io/idta/PurchaseOrder/TaxRate /1/0`), which prevents exact
  identifier matching. Identifiers and their references were corrected together so
  that they continue to resolve.

## Verification

- All four machine-readable artifacts deserialize and pass `aas-core3`
  constraint verification with 0 violations.
- Both AASX packages open as valid OPC packages and their XML payloads are
  well-formed. Non-payload package entries are byte-identical to version 1.0.
- Unresolved semantic references within the Purchase Order namespace were reduced
  from 7 to 2.

## Known remaining issues

- [#274](https://github.com/admin-shell-io/submodel-templates/issues/274) -
  [Purchase Order 1.0] SpecialTreatmentClass definition missing/inconsistent.
  Not fixed in this release. Investigation showed the `SpecialTreatmentClassList`
  SubmodelElementList and the `SpecialTreatmentClass` SubmodelElementCollection
  are both present and carry the correct semantic identifiers, but the collection
  has no child elements. The `SpecialTreatmentClass` ConceptDescription exists and
  describes a short designation for the special treatment regulation. Populating
  the collection requires confirmation of the intended child properties against
  the specification and is left to a content decision.

- Two semantic references do not resolve to any ConceptDescription:
  `.../ScanCodeType_Barcode/1/0` and `.../ScanCodeType_QRcode/1/0`.
  The available ConceptDescriptions are named `ScanCodeType_Bar-code` and
  `ScanCodeType_QR-code` (with hyphens). Aligning these requires deciding which
  spelling is normative, so the references were left unchanged.
