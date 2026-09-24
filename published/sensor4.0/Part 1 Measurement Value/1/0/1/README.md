## Sensor 4.0 Part 1 (Measurement Value) bug-fix version 1.0.1

This folder contains a bug-fix release of the submodel template artifacts.
Only the machine-readable artifacts (JSON and AASX) were corrected; the
specification PDF is carried over from version 1.0 unchanged.

### Artifacts in this directory

- AASX: IDTA 02029-1-0-1_Template_Sensor4.0_MeasurementValue.aasx
- JSON: IDTA 02029-1-0-1_Template_Sensor4.0_MeasurementValue.json
- PDF: IDTA 02029-1_Template_Sensor4.0_MeasurementValue.pdf (unchanged)

### Bug fixes applied

- [#303](https://github.com/admin-shell-io/submodel-templates/issues/303) -
  Sensor 4.0: invalid AllowedValue qualifier.
  The `SMT/AllowedValue` qualifier on `MeasurementQualifier.Quality` held its
  permitted values pipe-delimited with spaces: `good | bad | uncertain | others`.

  The convention used everywhere else in this repository is a semicolon-separated
  list with no surrounding spaces -- 69 `SMT/AllowedValue` qualifiers across the
  templates follow it (for example `low;medium;high;critical` and
  `failure;function check;out of specification;maintenance request` in Plant Asset
  Management). The value is now `good;bad;uncertain;others`, so the permitted
  values can be split reliably by a consumer. All four values are preserved in
  their original order.

### Known remaining issues

- 1 constraint violation remains, a file-URI form (`/aasx/...` rather than an
  RFC 8089 `file:` URI). This is the convention used throughout this repository
  and predates this release.
