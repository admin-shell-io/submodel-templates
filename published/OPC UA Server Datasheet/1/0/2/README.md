## OPC UA Server Datasheet bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.1, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02009-1-0-Template-OPCUA-Server Datasheet.json
- AASX: IDTA 02009-1-0-Template-OPCUA-Server Datasheet.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02009-1-0_Submodel_OPC UA Server Data Sheet.pdf](../IDTA%2002009-1-0_Submodel_OPC%20UA%20Server%20Data%20Sheet.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
