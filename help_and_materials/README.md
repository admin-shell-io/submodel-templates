# Help and materials

This folder shall provide further advice and materials.

## Organization of repository

On top level, the repo organizes a linear list of Submodel templates. For each of these Submodel templates, multiple versions are foreseen by the folder structure. Versioning follows semantic versioning, with version (breaking changes) and revision (non-breaking changes).

For each Submodel template (SMT), the following information is provided:

### README.md

README describes scope, tags and details of the Submodel template. See below.

### Submodel template specification document (.pdf, .docx, ..)

This document holds the actual specification for the Submodel template. This is provided as written text in order to be potentially standardized by standardization organizations (SDOs) such as ISO or IEC.

An appendix holding a serializiation of a Submodel of kind = Template might exist in this document.

### Submodel template (SMT_*.aasx)

This file holds an AASX, e.g. edited by the [AASX Package Explorer](https://github.com/admin-shell-io/aasx-package-explorer), which contains one or more Submodels of kind = Template. These shall be described by the above document. No Qualifiers for generic forms or such shall be contained.

### Submodel template (SMT_qualified_*.aasx)

This file holds an AASX, e.g. edited by the [AASX Package Explorer](https://github.com/admin-shell-io/aasx-package-explorer), which contains one or more Submodels of kind = Template. These Submodels are the same as the Submodel templates above, however Qualifiers for generic forms or such are contained.

### JSON for generic-forms for AASX Package Explorer (*.add-options.json)

These JSON files can be added to the plugin folder of the AASX Package Explorer (typically .\plugins\AasxPluginGenericForms relative to AasxPackageExplorer.exe). Generic form help editing Submodels.

### Samples (Sample_*.aasx)

One or more samples shall be provided.

## Organization of README.md 

The README shall contain the following sections

### Title of Submodel template in written text.

This title shall be the first line, marked as H1 header.

### Scope of the Submodel 

Scope declaration, typically copied from the Submodel template specification document.

### Difference to prior versions

Description, what has changed compared to the prior published or productive version(s).

### Status

Says "This version is in productive use and supported by AASX Package Explorer.", if applicable.

### Submodel template criteria



# Available Submodel template criteria

Currently, the following criteria or tags are discussed.

| Criteria description                                                    | Badge | URL
| ----------------------------------------------------------------------- | ----- | --------------------------------------------------------|
| Specification document exists                                           | ![Template](https://img.shields.io/static/v1?style=plastic&label=SMT&message=Template&color=green) | https://img.shields.io/static/v1?style=plastic&label=SMT&message=Template&color=green |
| Submodel template is the only one existing for a single domain          | ![Unique](https://img.shields.io/static/v1?style=plastic&label=SMT&message=Unique&color=b5179e) | https://img.shields.io/static/v1?style=plastic&label=SMT&message=Unique&color=b5179e |
| Submodel template is preferred and well accepted for a domain           | ![Pref](https://img.shields.io/static/v1?style=plastic&label=SMT&message=Pref&color=560bad) | https://img.shields.io/static/v1?style=plastic&label=SMT&message=Pref&color=560bad |
| Defined for a specific domain                                           | ![Domain](https://img.shields.io/static/v1?style=plastic&label=SMT&message=Domain&color=7209b7) | https://img.shields.io/static/v1?style=plastic&label=SMT&message=Domain&color=7209b7 |
| Submodel template is a base model for type asset                        | ![Base](https://img.shields.io/static/v1?style=plastic&label=SMT&message=Base&color=480ca8) | https://img.shields.io/static/v1?style=plastic&label=SMT&message=Base&color=480ca8 |
| Submodel template was derived (extended) from another submodel          | ![Ext](https://img.shields.io/static/v1?style=plastic&label=SMT&message=Ext&color=3a0ca3) | https://img.shields.io/static/v1?style=plastic&label=SMT&message=Ext&color=3a0ca3 |
| Submodel template is maintained by a single company                     | ![Vendor](https://img.shields.io/static/v1?style=plastic&label=SMT&message=Vendor&color=3f37c9) | https://img.shields.io/static/v1?style=plastic&label=SMT&message=Vendor&color=3f37c9 |
| Submodel template is maintained by a single company                     | ![Vendor](https://img.shields.io/static/v1?style=plastic&label=SMT&message=Vendor&color=3f37c9) | https://img.shields.io/static/v1?style=plastic&label=SMT&message=Vendor&color=3f37c9 |
| Submodel template is maintained by external consortium                  | ![Consort](https://img.shields.io/static/v1?style=plastic&label=SMT&message=Consort&color=4361ee) | https://img.shields.io/static/v1?style=plastic&label=SMT&message=Consrot&color=4361ee |
| Submodel template is maintained by an international standard            | ![Std](https://img.shields.io/static/v1?style=plastic&label=SMT&message=Std&color=4895ef) | https://img.shields.io/static/v1?style=plastic&label=SMT&message=Std&color=4895ef |
| Submodel template supports ECLASS properties                            | ![ECLASS](https://img.shields.io/static/v1?style=plastic&label=SMT&message=ECLASS&color=000055) | https://img.shields.io/static/v1?style=plastic&label=SMT&message=ECLASS&color=000055 |

# Example

```
# ZVEI Digital Nameplate V1.0

This is a Submodel template specification for the Asset Adminstration Shell.

(https://img.shields.io/static/v1?style=plastic&label=SMT&message=Template&color=green)
(https://img.shields.io/static/v1?style=plastic&label=SMT&message=Base&color=480ca8)
(https://img.shields.io/static/v1?style=plastic&label=SMT&message=ECLASS&color=000055)

## Scope of the Submodel 

This Submodel template aims at interoperable provision of information describing the nameplate of the asset of the respective Asset Administration Shell. Central element is the provision of properties, ideally interoperable by the means of dictionaries such as ECLASS and IEC CDD (Common Data Dictionary). The purpose of this document is to make selected specifications of submodels in such manner that information about assets and their nameplate can be exchanged in a meaningful way between partners in a value creation network. It targets equipment for process industry  and factory automation by defining standardized meta data.  
The intended use-case is the provision of a standardized property structure within a digital nameplate, which enables the interoperability of digital nameplates from different manufacturers. 
This concept can serve as a basis for standardizing the respective submodel. The conception is based on existing norms, directives and standards so that a far-reaching acceptance can be achieved.  
Beside standardized submodel this template also introduces standardized SubmodelElementCollections (SMC) in order to improve the interoperability while modelling partial aspects within submodels. The standardized SMCs include address and asset product marking. 

## About this version

This version is the first version officially published by ZVEI and Plattform Industrie 4.0.
It is succeeding the version of "Digital Typeplate by HSU".

## Difference to prior versions

No prior versions were published.

## Status

This version is in productive use and supported by AASX Package Explorer.
```
