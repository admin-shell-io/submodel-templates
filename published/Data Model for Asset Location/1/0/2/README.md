## Data Model for Asset Location bug-fix version 1.0.2

This folder contains the bug-fix release of the submodel template artifacts.
It builds on version 1.0.1; the artifacts of 1.0.1 are unchanged.

### Artifacts in this directory

- AASX: IDTA 02045-1-0-2_Template_DataModelForAssetLocation_forAASMetamodelV3.1.aasx (this is the SMT updated to the latest version of the AAS metamodel, V3.1)
- AASX: IDTA 02045-1-0-2_Template_DataModelForAssetLocation.aasx (this is the bug-fixed version of the SMT that uses the AAS metamodel V3.0)
- JSON: IDTA 02045-1-0-2_Template_DataModelForAssetLocation.json
- JSON: IDTA 02045-1-0-2_Template_DataModelForAssetLocation_forAASMetamodelV3.1.json

### Bug fixes applied in 1.0.2

- [#273](https://github.com/admin-shell-io/submodel-templates/issues/273) -
  [Data Model for Asset Location] one-character X/Y/Z idShorts.
  The idShort values `X`, `Y` and `Z` violate AAS constraint AASd-002, which
  requires an idShort of at least two characters. They were renamed to
  `XCoordinate`, `YCoordinate` and `ZCoordinate` (40 occurrences across the four
  artifacts).

  The renamed elements are bound to their ConceptDescriptions by semanticId URI
  (for example `https://admin-shell.io/idta/prop/x/1/0`), not by idShort, so the
  rename does not affect semantic resolution. The `displayName` entries
  ("X-coordinate" / "X-Koordinate") are unchanged, so the elements still present
  the same labels to users.

  Note for implementers: this is a breaking change for any consumer that
  addresses these elements by idShort path.

  This issue shares its root cause with
  [#272](https://github.com/admin-shell-io/submodel-templates/issues/272) in
  Provision of 3D Models, which is fixed the same way in that template's version
  1.0.2.

### Verification

- Both JSON artifacts deserialize and pass `aas-core3` constraint verification
  with 0 violations.
- Both AASX packages open as valid OPC packages with well-formed XML payloads.
  All non-payload package entries are byte-identical to version 1.0.1.
- No one-character idShort remains in any artifact (40 before, 0 after).
