## Control Component Type bug-fix version 2.0.3

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 2.0.2, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02015-2-0-3 _Template_ControlComponentType.json
- AASX: IDTA 02015-2-0-3 _Template_ControlComponentType.aasx (AAS metamodel V3.0)
- AASX: IDTA 02015-2-0-3 _Template_ControlComponentType_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02015-2-0 _Submodel_CCType.pdf](../IDTA%2002015-2-0%20_Submodel_CCType.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
