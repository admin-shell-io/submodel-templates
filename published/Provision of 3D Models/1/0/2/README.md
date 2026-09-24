## Provision of 3D Models bug-fix version 1.0.2

This folder contains the bug-fix release of the submodel template artifacts.
It builds on version 1.0.1; the artifacts of 1.0.1 are unchanged.

### Artifacts in this directory

- AASX: IDTA 02026-1-0-2_Template_ProvisionOf3DModels_forAASMetamodelV3.1.aasx (this is the SMT updated to the latest version of the AAS metamodel, V3.1)
- AASX: IDTA 02026-1-0-2_Template_ProvisionOf3DModels.aasx (this is the bug-fixed version of the SMT that uses the AAS metamodel V3.0)
- JSON: IDTA 02026-1-0-2_Template_ProvisionOf3DModels.json
- JSON: IDTA 02026-1-0-2_Template_ProvisionOf3DModels_forAASMetamodelV3.1.json

### Bug fixes applied in 1.0.2

- Qualifier kind corrected: `ConceptQualifier` -> `TemplateQualifier`
  (117 occurrences per JSON artifact). A qualifier that constrains the template
  itself, rather than the concept, must carry kind `TemplateQualifier`.

### Deliberately not fixed in this release

- [#272](https://github.com/admin-shell-io/submodel-templates/issues/272) -
  [Provision of 3D Models] one-character X/Y/Z idShorts.
  The idShort values `X`, `Y` and `Z` violate AAS constraint AASd-002, which
  requires an idShort of at least two characters. Renaming them would be a
  breaking change for any consumer that addresses these elements by idShort
  path, which is out of scope for a patch release. The issue is left open for
  the working group to schedule into a minor version.

### Known remaining issues

- One constraint violation remains in each JSON artifact: "The value must
  represent a valid file URI scheme according to RFC 8089." This is present
  identically in versions 1.0 and 1.0.1 and is not addressed by this release, as
  correcting it requires deciding the intended file reference value.
