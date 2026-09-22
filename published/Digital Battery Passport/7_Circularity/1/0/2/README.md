## Digital Battery Passport - 7_Circularity bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It was produced from version 1.0 and contains only corrections to the
machine-readable artifacts (JSON and AASX). The specification PDF, where present,
is carried over unchanged.

### Artifacts in this directory

- AASX: IDTA 02035-7_DBP-Part-7_Circularity.aasx
- JSON: IDTA 02035-7_DBP-Part-7_Circularity.json
- PDF: IDTA 02035-7_DBP-Part-7_Circularity.pdf (unchanged)
- JSON: IDTA 02035-7_DBP-Part-7_Circularity_without_examplevalues.json

### Corrections applied

These are defect classes reported against the submodel templates. Each was
applied to every JSON and AASX artifact in this folder.

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

