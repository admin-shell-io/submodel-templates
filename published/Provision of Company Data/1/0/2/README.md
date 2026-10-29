## Provision of Company Data bug-fix version 1.0.2

This folder contains a bug-fix release of the submodel template artifacts.
It builds on version 1.0.1, whose artifacts are unchanged.
The AASX packages are generated from the template JSON (tools/build_aasx.py).

The template follows the specification again: version 1.0.1 had turned BankAccounts into a SubmodelElementList and moved MainAccount out of it (for #267), which contradicts Table 5 and Figure 4 of the specification. Changing that structure needs a new version of the specification, so #267 stays open as a change request. The other corrections of 1.0.1 are kept.

### Artifacts in this directory

- JSON: IDTA 02068_Template_Provision Of Company Data.json
- AASX: IDTA 02068_Template_Provision Of Company Data.aasx (AAS metamodel V3.1)
- AASX: IDTA 02068_Template_Provision Of Company Data_forAASMetamodelV3.1.aasx (AAS metamodel V3.1)
- PDF: [IDTA 02068_Submodel Provision of Company Data.pdf](../1/IDTA%2002068_Submodel%20Provision%20of%20Company%20Data.pdf) (unchanged, not copied)

### Corrections

- BankAccounts restored as specified: SMC with MainAccount and BankAccount__00__ (reverts the 1.0.1 restructuring for #267)

### Issues fixed in this release

None. This release reverts a change that did not match the specification (see above).
