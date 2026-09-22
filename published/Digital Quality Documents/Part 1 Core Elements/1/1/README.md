## Digital Quality Documents - Part 1 Core Elements bug-fix version 1.1

This folder contains a bug-fix release of the submodel template artifacts.
It was produced from version 1 and contains only corrections to the
machine-readable artifacts (JSON and AASX). The specification PDF, where present,
is carried over unchanged.

### Artifacts in this directory

- PDF: IDTA 02065-1_Submodel_DigitalQualityDocuments-part-1.pdf (unchanged)
- AASX: IDTA 02065-1_Template_DigitalQualityDocuments-part-1.aasx
- JSON: IDTA 02065-1_Template_DigitalQualityDocuments-part-1.json

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
- Constraint violations in this folder: **2**.

### Known remaining issues

These were not corrected here, because the correct value is not determinable from the template alone.

- **The value must represent a valid file URI scheme according t** (1): File elements reference packaged files as `/aasx/files/...`. This is the convention used across this repository (84 occurrences) and is how AASX Package Explorer addresses files inside the package, but `aas-core3` expects an RFC 8089 `file:` URI. This was left unchanged deliberately: rewriting it would break the packaged-file references that real tooling resolves today. It needs a repository-wide decision, not a per-template fix.
- **AASd-021** (1): Qualifiers with the same type appear more than once on one element. Which qualifier is authoritative is a content decision.

### Issue-specific fixes in this release

- [#277](https://github.com/admin-shell-io/submodel-templates/issues/277) -
  Qualifiers on Conformity. The `Conformity` Property carried TWO qualifiers both
  typed `SMT/Value`, with values "pass" and "fail". That is invalid twice over: a
  qualifier type may appear only once on an element, and `SMT/Value` is not the
  qualifier for expressing a restricted set of permitted values.

  This repository's convention for an enumerated value set is a single
  `SMT/AllowedValue` qualifier holding the values separated by `;` -- 69 uses
  across the templates, against only 4 uses of `SMT/Value`, which are these
  defects. The pair was merged into one `SMT/AllowedValue` qualifier with value
  `pass;fail` and its semanticId retargeted to
  `https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0`. Both permitted
  values are preserved in their original order.

### Issues reviewed but not changed

- [#275](https://github.com/admin-shell-io/submodel-templates/issues/275) -
  Invalid SemanticId. The issue reports a semanticId that "appears to be a
  copy/paste artifact" but does not identify which one. No syntactically invalid
  identifier was found in these artifacts after the whitespace corrections in
  this release. This needs the reporter to name the affected element before it
  can be closed.
