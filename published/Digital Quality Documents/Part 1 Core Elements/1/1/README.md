## Digital Quality Documents - Part 1 Core Elements bug-fix version 1.1

This folder contains a bug-fix release of the submodel template artifacts.
It was produced from version 1 and contains only corrections to the
machine-readable artifacts (JSON and AASX). The specification PDF, where present,
is carried over unchanged.

### Artifacts in this directory

- PDF: IDTA 02065-1_Submodel_DigitalQualityDocuments-part-1.pdf (unchanged)
- AASX: IDTA 02065-1_Template_DigitalQualityDocuments-part-1.aasx
- JSON: IDTA 02065-1_Template_DigitalQualityDocuments-part-1.json

### Issues fixed in this release

- [#187](https://github.com/admin-shell-io/submodel-templates/issues/187)
- [#207](https://github.com/admin-shell-io/submodel-templates/issues/207)
- [#208](https://github.com/admin-shell-io/submodel-templates/issues/208)
- [#210](https://github.com/admin-shell-io/submodel-templates/issues/210)
- [#275](https://github.com/admin-shell-io/submodel-templates/issues/275)
- [#277](https://github.com/admin-shell-io/submodel-templates/issues/277)

### Known remaining issues

These were not corrected here, because the correct value is not determinable from the template alone.

- **The value must represent a valid file URI scheme according t** (1): File elements reference packaged files as `/aasx/files/...`. This is the convention used across this repository (84 occurrences) and is how AASX Package Explorer addresses files inside the package, but `aas-core3` expects an RFC 8089 `file:` URI. This was left unchanged deliberately: rewriting it would break the packaged-file references that real tooling resolves today. It needs a repository-wide decision, not a per-template fix.
- **AASd-021** (1): Qualifiers with the same type appear more than once on one element. Which qualifier is authoritative is a content decision.

### Issues reviewed but not changed

- [#275](https://github.com/admin-shell-io/submodel-templates/issues/275) -
  Invalid SemanticId. The issue reports a semanticId that "appears to be a
  copy/paste artifact" but does not identify which one. No syntactically invalid
  identifier was found in these artifacts after the whitespace corrections in
  this release. This needs the reporter to name the affected element before it
  can be closed.
