## DEXPI bug-fix version 1.0.1

This folder contains a bug-fix release of the submodel template artifacts.
Only the machine-readable artifacts (JSON and AASX) were corrected; the
specification PDF is carried over from version 1.0 unchanged.

### Artifacts in this directory

- AASX: IDTA 02012-1-0-1_Template_DEXPI.aasx
- JSON: IDTA 02012-1-0-1_Template_DEXPI.json
- PDF: IDTA 02012-1-0_Submodel_DEXPI.pdf (unchanged from version 1.0)

### Bug fixes applied

- [#79](https://github.com/admin-shell-io/submodel-templates/issues/79) -
  AASConstraintViolation when reading the DEXPI template in basyx-python-sdk.
  Two distinct invalid reference shapes were the cause, both corrected:

  - **AASd-127 (43 occurrences)**: a ModelReference key path
    `Submodel / SubmodelElementCollection / SubmodelElement / FragmentReference`.
    A FragmentReference must be preceded by a `File` or `Blob` key. The element
    being referenced is `ModelFile`, which is a File in this template, so the
    generic `SubmodelElement` key type was wrong and is now `File`.
  - **AASd-121 and AASd-123 (5 occurrences)**: a ModelReference whose only key
    was of type `Entity` pointing at `http://example.com/id/...`. A reference to
    an external identifier is an ExternalReference with a GlobalReference key,
    not a ModelReference into the AAS, and is now modelled as such.

- [#93](https://github.com/admin-shell-io/submodel-templates/issues/93),
  [#94](https://github.com/admin-shell-io/submodel-templates/issues/94) -
  DEXPI template IRIs not following specification IRIs / semanticId deviation.
  The admin-shell DEXPI namespace was spelled two ways in the same template:
  `http://admin-shell.io/dexpi/...` (199 occurrences) and
  `http://admin-shell.io/DEXPI/...` (12 occurrences, all
  `.../DEXPI/1/0/TagMapping`). Since exact string matching is what resolves a
  semantic identifier, the minority spelling was normalised to the dominant
  lowercase form.

  Note: the `http://sandbox.dexpi.org/...` identifiers are external DEXPI
  identifiers and are deliberately left as they are.

### Known remaining issues

- [#281](https://github.com/admin-shell-io/submodel-templates/issues/281) -
  DEXPI: missing semantic IDs. 47 elements (for example `ManufacturerName`,
  `DateOfManufacture`, and the `ProcessInstrumentationFunction_*_rel`
  relationship elements) carry no semanticId. Minting new semantic identifiers
  requires authority over the DEXPI namespace, so no identifiers were invented
  here. This needs the DEXPI working group.

- 2 remaining constraint violations: one file-URI form (`/aasx/...` rather than
  an RFC 8089 `file:` URI, the convention used throughout this repository) and
  one related reference. Both predate this release.
