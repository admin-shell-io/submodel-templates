## Handover Documentation bug-fix version 2.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It was produced from version 2.0 and contains only corrections to the
machine-readable artifacts (JSON and AASX). The specification PDF, where present,
is carried over unchanged.

### Artifacts in this directory

- PDF: IDTA 02004-2-0-1_Submodel_Handover Documentation.pdf (unchanged)
- AASX: IDTA 02004-2-0-2_Template_HandoverDocumentation.aasx
- JSON: IDTA 02004-2-0-2_Template_HandoverDocumentation.json
- AASX: IDTA 02004-2-0-2_Template_HandoverDocumentation__forAASMetamodelV3.1.aasx
- JSON: IDTA 02004-2-0-2_Template_HandoverDocumentation__forAASMetamodelV3.1.json
- AASX: IDTA 02004-2-0-2_Template_sample_HandoverDocumentation_forAASMetamodelV3.1.aasx
- AASX: IDTA 02004-2-0_Template_sample_HandoverDocumentation.aasx

### Corrections applied

These are defect classes reported against the submodel templates. Each was
applied to every JSON and AASX artifact in this folder.

- **Misspelled display text** ([#236](https://github.com/admin-shell-io/submodel-templates/issues/236)). The `DocumentIds` English `displayName` read "Document identifyers"; corrected to "identifiers". Display text only, so no identifier or reference changed.

- **Whitespace and stray prefixes inside identifier URIs** ([#208](https://github.com/admin-shell-io/submodel-templates/issues/208), [#210](https://github.com/admin-shell-io/submodel-templates/issues/210)). Identifier values such as `https://admin-shell.io/idta/X /1/0`, values carrying an `[IRI]` or `]` prefix, and identifiers with an escaped newline prevent exact identifier matching. Identifier values and the references pointing at them were corrected together so that they continue to resolve.

- **AASd-120**: a SubmodelElement that is a direct child of a SubmodelElementList must not carry an `idShort`. The offending `idShort` values were removed.

- **Non-unique language entries** ([#187](https://github.com/admin-shell-io/submodel-templates/issues/187), [#207](https://github.com/admin-shell-io/submodel-templates/issues/207)). A language-string set may hold only one text per language. Three distinct shapes were found and handled without discarding any content: exact repeats were collapsed; entries whose text was in the other language were **retagged** (for example German text tagged `en`) rather than deleted, so no translation is lost; and several separate notes sharing one language tag were **merged into a single entry**, joined in their original order.

- **AASd-118**: elements carrying `supplementalSemanticIds` without a main `semanticId`. The single supplemental identifier was promoted to be the main semantic identifier.

- **Missing `contentType` on a File element**, which is required by the metamodel and caused the template to fail deserialization entirely. Set to `application/octet-stream`, the neutral default for a template placeholder with no value.

### Verification

- Every JSON artifact deserializes under `aas-core3` and was re-verified after
  the changes.
- Every AASX package opens as a valid OPC package and its XML payload is
  well-formed. All non-payload package entries (relationships, content types,
  embedded files) are byte-identical to the previous release.
- Constraint violations in this folder: **0** (all constraint violations resolved).


### Issue-specific fixes in this release

- [#235](https://github.com/admin-shell-io/submodel-templates/issues/235) -
  syntactically wrong supplementalSemanticId. Four supplemental references each
  carried TWO GlobalReference keys: an ECLASS IRDI
  (`0173-1#02-ABI500#003~0/0173-1#01-AHF579#003`) and the same concept as a URL
  (`https://api.eclass-cdp.com/...`). A Reference's keys form a path to ONE
  referent, not a list of alternative identifiers, so each was split into two
  separate single-key supplemental references. Both identifiers are preserved.
  8 references split in JSON, 30 in the AASX payloads.

- [#238](https://github.com/admin-shell-io/submodel-templates/issues/238) -
  ConceptDescription DigitalFile is not an enumeration. The `DigitalFile`
  ConceptDescription carried a `valueList` with a single entry ("File"), which
  wrongly presents it as an enumeration. The single-entry value list was removed;
  the ConceptDescription and its `dataType: STRING` are otherwise unchanged.

- [#251](https://github.com/admin-shell-io/submodel-templates/issues/251) -
  Invalid Example Value for VDI 2770 Classification System. The
  ClassificationSystem example value `VDI2770:2020` was replaced with the
  standardized wording `VDI 2770 Blatt 1:2020`. No `VDI2770:2018` references
  remain in these artifacts.

### Issues reviewed but not fixable in these artifacts

- [#319](https://github.com/admin-shell-io/submodel-templates/issues/319) -
  English ClassNames do not match German for 02-03 and 03-01. The `ClassId` and
  `ClassName` properties in the template carry no values (they are placeholders);
  the VDI 2770 class table lives in the specification PDF. Correcting it requires
  editing the PDF against the authoritative VDI 2770 mapping.

- [#151](https://github.com/admin-shell-io/submodel-templates/issues/151) -
  Malformed regular expressions for ValidIdShorts. No regular-expression
  constraint values are present in the machine-readable artifacts; this is
  specification text.

- [#120](https://github.com/admin-shell-io/submodel-templates/issues/120) -
  Clarification on submodel idShort uniqueness constraint. Specification wording.

- [#237](https://github.com/admin-shell-io/submodel-templates/issues/237) -
  HandoverDocumentation 2.0 SML Language. The `Language` SubmodelElementList and
  its member were checked: the member correctly carries no idShort (AASd-120), so
  the structural part of this issue does not reproduce in the current artifacts.
