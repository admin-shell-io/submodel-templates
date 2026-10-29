## Process Variables for Manufacturing Key Performance Indicators bug-fix version 1.0.1

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02066_Template_PVM.json
- AASX: IDTA 02066_Template_PVM.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02066_Submodel_PVM.pdf](../IDTA%2002066_Submodel_PVM.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
