# Digital Quality Documents Part 1:Core Elements (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 
This Submodel template addresses the need to handle documentation, certificates and reports about the
conformity of an asset to relevant requirements. These kinds of requirements are usually related to the
quality infrastructure (metrology, accreditation, conformity assessment, standards, market surveillance) and
the corresponding documents are for the purpose of simplicity called “quality documents” here.

The Submodel aims to provide a Digital Quality Documents (DQD) model that can be transferred across an
asset lifecycle. A quality document in the sense of this specification is a (usually machine-readable)
document that contains information about quality properties about an asset, with this specification focusing
on conformity statements. In general, one asset may have several conformity statements related to different
domains and application purposes. For instance, for a measuring instrument there can be statements about
calibration (based on ISO/IEC 17025) and about the compliance with explosion protection (ATEX/IECEx).
Each instance of the DQD Submodel is then related to one document for each such statement. That is,
several instances of the DQD Submodel may exist for one asset at the same time. Moreover, some
conformity statements may relate to the product type rather than the individual asset. This is the case, for
instance, for type approval in a conformity assessment based on ISO/IEC 17065.

The information contained in the Submodel is inspired by the already developed XML schema for Digital
Calibration Certificates (DCC) [7]. This XML schema meets the requirements of ISO/IEC 17025 and can be
signed electronically and secured cryptographically. There is an ongoing international harmonization of
DCCs, and an increasing number of certificates and reports in other domains than calibration is being
developed in a similar way.

Information described in this DQD Submodel regarding the assets of the respective Asset Administration
Shell is semantically identified by means of the DCC namespace and dictionaries such as ECLASS and IEC
CDD (Common Data Dictionary).

Part 1 of this Submodel focuses on general information expected to be relevant for all types of quality
documents, especially with documents related to the ISO/IEC 170xx series in mind. Subsequent versions of
this Submodel will extend the general specifications to more specific ones for various domains, such as
conformity assessment, reference material, testing, and verification.

## About this version

This version is the first version officially published by IDTA

## Difference to prior versions

No prior versions were offically published.
