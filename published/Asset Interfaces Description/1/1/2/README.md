## Asset Interfaces Description bug-fix version 1.1.2

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.1.1, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

### Artifacts in this directory

- JSON: IDTA 02017-1-1-2_Template_Asset Interfaces Description.json
- AASX: IDTA 02017-1-1-2_Template_Asset Interfaces Description.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02017-1-1_Submodel_Asset Interfaces Description.pdf](../IDTA%2002017-1-1_Submodel_Asset%20Interfaces%20Description.pdf) (unchanged, not copied)

### Corrections

- submodel semanticId changed from ModelReference to ExternalReference/GlobalReference (#224)
- SML enum has valueTypeListElement xs:string (AASd-109) (24 places) (#323)
- SMC forms has cardinality One as specified (6 places) (#323)
- SML htv_headers has no valueTypeListElement (its elements are SMCs) (#323)
- SML scopes holds Properties of type xs:string as specified (5 places) (#323)
- SML allOf / oneOf hold ReferenceElements as specified in 2.27.9 (10 places) (#323)

### Issues fixed in this release

- [#224](https://github.com/admin-shell-io/submodel-templates/issues/224)
- [#345](https://github.com/admin-shell-io/submodel-templates/issues/345) (same defect as #224)
- [#323](https://github.com/admin-shell-io/submodel-templates/issues/323)
