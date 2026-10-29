## Hierarchical Structures enabling Bills of Material bug-fix version 1.1.3

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.1.2, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02011-1-1-3_Template_HSEBoM.json
- AASX: IDTA 02011-1-1-3_Template_HSEBoM.aasx (AAS metamodel V3.0)
- AASX: IDTA 02011-1-1-3_Template_HSEBoM_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02011-1-1_Submodel_HierarchicalStructuresEnablingBoM.pdf](../IDTA%2002011-1-1_Submodel_HierarchicalStructuresEnablingBoM.pdf) (unchanged, not copied)

### Corrections

- administration (version 1, revision 1) added (#209)
- submodel semanticId is an ExternalReference/GlobalReference (#209, #224)

### Issues fixed in this release

- [#209](https://github.com/admin-shell-io/submodel-templates/issues/209)
- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
