## Control Configuration and Parametrization for NC and CNC Machines bug-fix version 1.0.3

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.2, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02053-1-0-3_Template_ControlConfig.json
- AASX: IDTA 02053-1-0-3_Template_ControlConfig.aasx (AAS metamodel V3.0)
- AASX: IDTA 02053-1-0-3_Template_ControlConfig_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02053-1-0_Submodel_ControlConfig.pdf](../IDTA%2002053-1-0_Submodel_ControlConfig.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
