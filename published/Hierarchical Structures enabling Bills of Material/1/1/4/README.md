## Hierarchical Structures enabling Bills of Material bug-fix version 1.1.4

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.1.3, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02011-1-1-4_Template_HSEBoM.json
- AASX: IDTA 02011-1-1-4_Template_HSEBoM.aasx (AAS metamodel V3.0)
- AASX: IDTA 02011-1-1-4_Template_HSEBoM_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02011-1-1_Submodel_HierarchicalStructuresEnablingBoM.pdf](../IDTA%2002011-1-1_Submodel_HierarchicalStructuresEnablingBoM.pdf) (unchanged, not copied)

### Corrections

- example globalAssetIds are distinct example asset ids instead of the EntryNode semanticId (3 places) (#346)
- Node description no longer copied from EntryNode (#346)

### Issues fixed in this release

- [#346](https://github.com/admin-shell-io/submodel-templates/issues/346)
