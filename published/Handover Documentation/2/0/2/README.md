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

### Issues fixed in this release

- [#187](https://github.com/admin-shell-io/submodel-templates/issues/187)
- [#207](https://github.com/admin-shell-io/submodel-templates/issues/207)
- [#208](https://github.com/admin-shell-io/submodel-templates/issues/208)
- [#210](https://github.com/admin-shell-io/submodel-templates/issues/210)
- [#235](https://github.com/admin-shell-io/submodel-templates/issues/235)
- [#236](https://github.com/admin-shell-io/submodel-templates/issues/236)
- [#238](https://github.com/admin-shell-io/submodel-templates/issues/238)
- [#251](https://github.com/admin-shell-io/submodel-templates/issues/251)

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
