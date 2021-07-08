# Help and materials

This folder shall provide further advice and materials.

## Organization of repository

On top level, the repo organizes a linear list of Submodel templates. For each of these Submodel templates, multiple versions are foreseen by the folder structure. Versioning follows semantic versioning, with version (breaking changes) and revision (non-breaking changes).

For each Submodel template, the following information is provided:

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

Currently, the following criteria or tags are discussed.

| Criteria      | Description                            | Badge | URL
| ------------- | -------------------------------------- | ----- | --------------------------------------------------------|
|               | Specification document exists          | https://img.shields.io/static/v1?style=plastic&label=SMT&message=Template&color=green |

bla

# Color palette

see (https://coolors.co/f72585-b5179e-7209b7-560bad-480ca8-3a0ca3-3f37c9-4361ee-4895ef-4cc9f0).

