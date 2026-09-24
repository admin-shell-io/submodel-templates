## Asset Interfaces Description bug-fix version 1.2

This folder contains a bug-fix release of the submodel template artifacts.
It was produced from version 1 and contains only corrections to the
machine-readable artifacts (JSON and AASX). The specification PDF, where present,
is carried over unchanged.

### Artifacts in this directory

- PDF: IDTA 02017-1-1_Submodel_Asset Interfaces Description.pdf (unchanged)
- AASX: IDTA 02017-1-1_Template_Asset Interfaces Description.aasx
- JSON: IDTA 02017-1-1_Template_Asset Interfaces Description.json

### Corrections applied

These are defect classes reported against the submodel templates. Each was
applied to every JSON and AASX artifact in this folder.

- **Whitespace and stray prefixes inside identifier URIs** ([#208](https://github.com/admin-shell-io/submodel-templates/issues/208), [#210](https://github.com/admin-shell-io/submodel-templates/issues/210)). Identifier values such as `https://admin-shell.io/idta/X /1/0`, values carrying an `[IRI]` or `]` prefix, and identifiers with an escaped newline prevent exact identifier matching. Identifier values and the references pointing at them were corrected together so that they continue to resolve.

- **AASd-120**: a SubmodelElement that is a direct child of a SubmodelElementList must not carry an `idShort`. The offending `idShort` values were removed.

- **Non-unique language entries** ([#187](https://github.com/admin-shell-io/submodel-templates/issues/187), [#207](https://github.com/admin-shell-io/submodel-templates/issues/207)). A language-string set may hold only one text per language. Three distinct shapes were found and handled without discarding any content: exact repeats were collapsed; entries whose text was in the other language were **retagged** (for example German text tagged `en`) rather than deleted, so no translation is lost; and several separate notes sharing one language tag were **merged into a single entry**, joined in their original order.

- **AASd-118**: elements carrying `supplementalSemanticIds` without a main `semanticId`. The single supplemental identifier was promoted to be the main semantic identifier.

- **Missing `contentType` on a File element**, which is required by the metamodel and caused the template to fail deserialization entirely. Set to `application/octet-stream`, the neutral default for a template placeholder with no value.

### Known remaining issues

These were not corrected here, because the correct value is not determinable from the template alone.

- **The value must represent a valid file URI scheme according t** (1): File elements reference packaged files as `/aasx/files/...`. This is the convention used across this repository (84 occurrences) and is how AASX Package Explorer addresses files inside the package, but `aas-core3` expects an RFC 8089 `file:` URI. This was left unchanged deliberately: rewriting it would break the packaged-file references that real tooling resolves today. It needs a repository-wide decision, not a per-template fix.
