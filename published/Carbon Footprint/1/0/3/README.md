## Carbon Footprint bug-fix version 1.0.3

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.2, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02023-1-0-3 _Template_CarbonFootprint.json
- AASX: IDTA 02023-1-0-3 _Template_CarbonFootprint.aasx (AAS metamodel V3.0)
- AASX: IDTA 02023-1-0-3 _Template_CarbonFootprint_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- PDF: IDTA 02023_Submodel_CarbonFootprint.pdf (corrected: Table 1 idShort ProductCarbonFootprint -> ProductCarbonFootprints; based on the 1.0.2 PDF)

### Corrections

- PcfCalculationMethods / LifeCyclePhases lists back to cardinality One (3 places) (#124)
- cardinality removed from the elements inside lists (3 places) (#124)
- leading/trailing space removed from reference key values
- specification PDF: the idShort of the SML in Table 1 is ProductCarbonFootprints (#130)

### Issues fixed in this release

- [#124](https://github.com/admin-shell-io/submodel-templates/issues/124)
- [#130](https://github.com/admin-shell-io/submodel-templates/issues/130)
