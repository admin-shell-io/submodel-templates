## Software Nameplate bug-fix version 1.0.2

This folder contains the bug-fix release of the submodel template artifacts.
It builds on version 1.0.1; the artifacts of 1.0.1 are unchanged.

### Artifacts in this directory

- AASX: IDTA 02007-1-0-2_Template_Software Nameplate_forAASMetamodelV3.1.aasx (this is the SMT updated to the latest version of the AAS metamodel, V3.1)
- AASX: IDTA 02007-1-0-2_Template_Software Nameplate.aasx (this is the bug-fixed version of the SMT that uses the AAS metamodel V3.0)
- JSON: IDTA 02007-1-0-2_Template_Software Nameplate.json
- JSON: IDTA 02007-1-0-2_Template_Software Nameplate_forAASMetamodelV3.1.json

### Issues fixed in this release

- [#305](https://github.com/admin-shell-io/submodel-templates/issues/305)

### Issues reviewed but not changed

- [#306](https://github.com/admin-shell-io/submodel-templates/issues/306) -
  Software Nameplate: ConfigurationType value-type mismatch.
  The issue reports that the JSON template types `ConfigurationType` as
  `xs:integer` while the specification defines it as a string. In the artifacts of
  versions 1.0, 1.0.1 and 1.0.2 this element is already typed `xs:string`, so no
  change was applied. This issue appears to be resolved, or to refer to a
  different artifact; it should be confirmed against the specification PDF before
  being closed.
