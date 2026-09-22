## Maintenance Instructions bug-fix version 1.0.1

This folder contains the bug-fix release of the submodel template artifacts.
The specification PDF is carried over from version 1.0 unchanged.

### Artifacts in this directory

- AASX: IDTA_02018-1-0-1_Template_MaintenanceInstructions.aasx
- JSON: IDTA_02018-1-0-1_Template_MaintenanceInstructions.json
- PDF: IDTA_02018_Submodel_MaintenanceInstructions.pdf (unchanged from version 1.0)

### Bug fixes applied

- [#245](https://github.com/admin-shell-io/submodel-templates/issues/245) -
  Constraint violations in template IDTA_02018_Submodel_MaintenanceInstructions.
  The template could not be parsed by a conformant BaSyx workflow. All reported
  constraint violations are corrected:

  - Invalid KeyType `Identifiable` replaced with `GlobalReference`, and the
    enclosing reference changed from `ModelReference` to `ExternalReference`
    (a reference whose key is a GlobalReference must be an ExternalReference,
    AASd-123).
  - AASd-120: idShort removed from SubmodelElements that are direct children of a
    SubmodelElementList (3 elements).
  - Duplicate `ReferenceNameOfMaintenance` idShorts within the same collection
    resolved. Three collections each contained two sibling ReferenceElements with
    the same idShort. In each case the element whose description reads
    "Referenz zur ID eines spezifischen Wartungsintervals" / "Reference to ID of
    specific maintenance interval" was renamed to `ReferenceToMaintenanceID`, as
    the issue proposes, and its semanticId retargeted to
    `.../referencetomaintenanceid/1/0`. One sibling in the tool collection had the
    opposite mislabeling and was aligned to its own semanticId.

### Additional corrections

- Non-unique language entries in `description` sets. Three sets carried two
  entries both tagged `de`, where the second held the ENGLISH text. Rather than
  dropping an entry (which would lose the translation), the mislabeled entry was
  retagged `en`.

### Verification

- The JSON artifact deserializes and passes `aas-core3` constraint verification
  with 0 violations (7 before this release).
- The AASX package opens as a valid OPC package with a well-formed XML payload.
  All non-payload package entries are byte-identical to version 1.0.

### Issues reviewed but not changed

- [#279](https://github.com/admin-shell-io/submodel-templates/issues/279) -
  Maintenance Instructions: typos in cardinalities. The reported invalid
  multiplicity literals (`ZerotoMany`, `ZerotToOne`) are not present in version
  1.0; only valid `ZeroToOne`, `ZeroToMany` and `One` values occur, and the
  `SparePart` spelling is consistent throughout. This issue appears to have been
  fixed already and can be confirmed and closed.
