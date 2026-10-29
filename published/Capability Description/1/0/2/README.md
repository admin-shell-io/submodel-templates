## Capability Description bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.1, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02020_Template_Capability_Description.json
- AASX: IDTA 02020_Template_Capability_Description.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02020_Submodel_Capability_Description.pdf](../IDTA%2002020_Submodel_Capability_Description.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)
- relationship references point to the submodel id instead of a non-existent id (9 places) (#347)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
- [#347](https://github.com/admin-shell-io/submodel-templates/issues/347)
