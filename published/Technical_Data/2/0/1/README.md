# Technical Data (Version 2.0.1)

This is a Submodel template specification for the Asset Administration Shell.

## About this version

This version 2.0.1 is a bug fix release that addresses GitHub issues identified in version 2.0 of the Technical Data submodel template.

## Changes in Version 2.0.1

### Bug Fixes

This version addresses the following GitHub issues:

- [#190](https://github.com/admin-shell-io/submodel-templates/issues/190) - [IDTA 02003 2 0 TechnicalData] Non-unique ExampleValue Qualifiers - The TechnicalData 2.0 SMT violates constraint AASd-021, for ClassificationSystem. This SubmodelElement has multiple qualifier entries of type "SMT/ExampleValue" with varying valueIds. Instead, the different options for example values should be separated by "|" characters. Furthermore, the semantic id for the example values look incorrect, they read "<https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0>", instead, they should probably be "<https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0>"
- [#178](https://github.com/admin-shell-io/submodel-templates/issues/178) - [TechnicalData 2.0] ProductImages SML contains SMC ProductImage: rename - Please rename SMC ProductImages to SMC ProductImage: it is the SMC for a single ProductImage. The SML has the name ProductImages. The semanticId for SML and SMC within the SML shall not be identical
- [#174](https://github.com/admin-shell-io/submodel-templates/issues/174) - [TechnicalData 2.0] Cardinality of SML itself is 0..1 or 1 but not 0..* - For SML TechnicalPropertyAreas the cardinality should be ZeroToOne but not ZeroToMany
- [#173](https://github.com/admin-shell-io/submodel-templates/issues/173) - [TechnicalData 2.0] SML shall not have same semanticId as the elements within the SML - The SML idShort: TechnicalPropertyAreas has the same semanticId as its elements, the SMC with (same) name TechnicalPropertyAreas. Please correct
- [#168](https://github.com/admin-shell-io/submodel-templates/issues/168) - Technical Data 2.0 bug fix
- [#161](https://github.com/admin-shell-io/submodel-templates/issues/161) - Technical Data 2.0 bug fix

## Status

This version is ready for productive use and addresses all known issues from version 2.0.
