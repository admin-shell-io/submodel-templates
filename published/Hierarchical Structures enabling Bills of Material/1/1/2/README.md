## Hierarchical Structures enabling Bills of Material bug-fix version 1.1.2

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.1.1; the artifacts of 1.1.1 are unchanged. The
specification PDF is carried over unchanged.

### Artifacts in this directory

- AASX: IDTA 02011-1-1-2_Template_HSEBoM.aasx
- AASX: IDTA 02011-1-1-2_Template_HSEBoM_forAASMetamodelV3.1.aasx
- JSON: IDTA 02011-1-1-2_Template_HSEBoM.json
- JSON: IDTA 02011-1-1-2_Template_HSEBoM_forAASMetamodelV3.1.json
- PDF: IDTA 02011-1-1_Submodel_HierarchicalStructuresEnablingBoM.pdf (unchanged)

### Bug fixes applied

- [#209](https://github.com/admin-shell-io/submodel-templates/issues/209) -
  [Hierarchical Structures enabling Bill of Materials 1.1.1] Multiple issues.
  Partially addressed:

  - **Deprecated `category` field removed** from all artifacts. Schema-conformant
    APIs reject templates that still populate it.
  - Whitespace inside semantic identifier URIs removed, and AASd-120 idShorts
    removed from direct children of SubmodelElementLists (see below).

  Two parts of this issue are **not** addressed here:

  - *Missing administration/version information on the submodel.* Adding it means
    choosing the `version` and `revision` values to publish, which is a release
    decision rather than a correction.
  - *Submodel semanticId modelled as a ModelReference to itself.* This is
    schema-valid, and the repository is split between the two styles
    (110 ModelReference against 67 ExternalReference), so it belongs with the
    repository-wide identifier policy discussed in
    [#224](https://github.com/admin-shell-io/submodel-templates/issues/224) and
    [#152](https://github.com/admin-shell-io/submodel-templates/issues/152)
    rather than being changed in one template.

  The issue also mentions a deprecated spelling. `ArcheType` is used consistently
  (19 occurrences across the repository) and matches the specification's own
  wording, so it was left unchanged.

### Verification

- Both JSON artifacts deserialize and pass `aas-core3` constraint verification
  with **0 violations**.
- Both AASX packages open as valid OPC packages with well-formed XML payloads.
  All non-payload package entries are byte-identical to version 1.1.1.
