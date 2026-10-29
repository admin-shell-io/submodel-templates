## DEXPI bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.1, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02012-1-0-2_Template_DEXPI.json
- AASX: IDTA 02012-1-0-2_Template_DEXPI.aasx (AAS metamodel V3.0)
- AASX: IDTA 02012-1-0-2_Template_DEXPI_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- PDF: IDTA 02012-1-0-2_Submodel_DEXPI.pdf (corrected: Table 6 semanticId of TagMapping is .../Metadata/TagMapping, as in Table 5)

### Corrections

- IRIs changed to the specification's https://admin-shell.io/idta/DEXPI/1/0/... (212 places) (#93)
- TagMapping uses .../Metadata/TagMapping like Metadata/SubTagMapping (12 places) (#94)
- submodel semanticId set to the specification's .../DEXPI/1/0/Submodel (#93, #224)
- administration (version 1, revision 0) added
- semanticIds added where the specification defines them and the template had none: {LocalId}_rel (MappingRelationship), EndProductName, EndProductCASName, ManufacturerName, DateOfManufacture (47 places) (#93)
- specification PDF: Table 6 now gives https://admin-shell.io/idta/DEXPI/1/0/Metadata/TagMapping, matching Table 5 and Metadata/SubTagMapping (#94)

### Issues fixed in this release

- [#93](https://github.com/admin-shell-io/submodel-templates/issues/93)
- [#94](https://github.com/admin-shell-io/submodel-templates/issues/94)
- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
