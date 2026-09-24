## Digital Battery Passport Part 4 (Technical Data) bug-fix version 1.0.2

This folder contains the bug-fix release of the submodel template artifacts.
It builds on version 1.0.1; the artifacts of 1.0.1 are unchanged.

### Artifacts in this directory

- AASX: IDTA 02035-4_DBP-Part-4_TechnicalData.aasx
- JSON: IDTA 02035-4_DBP-Part-4_TechnicalData.json
- JSON: IDTA 02035-4_DBP-Part-4_TechnicalData_without_examplevalues.json
- PDF: IDTA 02035-4_DBP-Part-4_TechnicalData.pdf (unchanged)

### Issues fixed in this release

- [#263](https://github.com/admin-shell-io/submodel-templates/issues/263)

### Known remaining issues

- One constraint violation remains per JSON artifact: "The value must represent a
  valid file URI scheme according to RFC 8089." This was present in versions 1.0
  and 1.0.1 and is not addressed here, as correcting it requires deciding the
  intended file reference value.
