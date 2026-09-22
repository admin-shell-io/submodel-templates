## Provision of Company Data bug-fix version 1.0.1

This folder contains a bug-fix release of the submodel template artifacts.
Only the machine-readable artifacts (JSON and AASX) were corrected; the
specification PDF is carried over from version 1.0 unchanged.

### Artifacts in this directory

- AASX: IDTA 02068_Template_Provision Of Company Data.aasx
- AASX: IDTA 02068_Template_Provision Of Company Data_forAASMetamodelV3.1.aasx
- JSON: IDTA 02068_Template_Provision Of Company Data.json
- JSON: IDTA 02068_Template_Provision Of Company Data_forAASMetamodelV3.1.json
- PDF: IDTA 02068_Submodel Provision of Company Data.pdf (unchanged)

### Bug fixes applied

- [#267](https://github.com/admin-shell-io/submodel-templates/issues/267) -
  [CompanyData 1.0] BankAccount in BankAccounts is a SML.
  `BankAccounts` was a SubmodelElementCollection containing a single member
  `BankAccount__00__`. The `__00__` suffix is this repository's own naming
  convention for a repeated list member, so the intended structure is a list of
  bank accounts rather than a collection holding exactly one.

  `BankAccounts` is now a `SubmodelElementList` with
  `typeValueListElement: SubmodelElementCollection` and a `semanticIdListElement`
  taken from the member. The member keeps all of its properties
  (`AccountHolder`, `BankAccountType`, `IBAN`, `BIC`, ...) and loses its
  `idShort`, which AASd-120 forbids on a direct child of a list.

  `MainAccount`, a ReferenceElement that is not a repeated member, was moved out
  of the list and kept as a sibling so it is not swept into the list structure.

  Note for implementers: this is a breaking change for any consumer addressing
  `BankAccounts.BankAccount__00__` by idShort path. List members are addressed by
  index.

### Additional corrections

- Whitespace inside semantic identifier URIs (for example
  `https://admin-shell.io/idta/CompanyData/DocumentationURI /1/0`) was removed
  from identifier and reference values so exact identifier matching succeeds.
- AASd-120: idShort removed from SubmodelElements that are direct children of a
  SubmodelElementList.

### Verification

- Both JSON artifacts deserialize and pass `aas-core3` constraint verification
  with **0 violations** (18 before this release).
- Both AASX packages open as valid OPC packages with well-formed XML payloads.
  All non-payload package entries are byte-identical to version 1.0.
- `MainAccount` is preserved in every artifact.
