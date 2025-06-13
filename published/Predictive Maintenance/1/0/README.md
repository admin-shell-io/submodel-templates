
# Predictive Maintenance (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 
The Submodel Predictive Maintenance aims to standardize metadata and information from various sub-systems within highly automated production lines, that are required for developing and deploying predictive maintenance solutions (PdM solutions). This facilitates integration and interoperability of sub-systems of production lines into PdM solutions. In addition, their data can be evaluated in a more targeted manner in the context of the PdM application in order to reduce unplanned machine downtimes. Accordingly, the PdM solutions can in turn provide maintenance-relevant information via the AAS, e.g., on predicted remaining lifetime and/or the probability of failure.

In general PdM aims to predict the end of useful life of a specific device or component (asset). The remaining useful life (RUL) is the duration until this end of life is reached, and the asset must be replaced or a maintenance action must be performed. RUL can be measured in time or other wear relevant units such as a distance/length or numbers of process cycles. The scope of the Submodel is mainly on data related to PdM, not on the prediction model itself.

Thus, this Submodel does not contain the implementation details data-driven and AI-boosted models for PdM,. As a matter of fact, this Submodel is merely structuring the data attained from an algorithm or model (physical or mathematical) for better utilization in planning and maintaining physical assets in a shopfloor.

The Submodel Predictive Maintenance aims at interoperable provision of information describing PdM topics in regard to an asset. Central element is the provision of properties [7], ideally interoperable by the means of dictionaries such as ECLASS and IEC CDD (Common Data Dictionary). The purpose of this document is to make selected specifications of Submodels in such manner that information about assets can be exchanged in a meaningful way between partners in a value creation network. It targets components of machines or plant sections which are themselves sub-systems of factories or plants and predictive maintenance applications for these components and sub-systems.

The conception is based on existing norms, studies of common practices at enterprises, directives and standards so that a far-reaching acceptance can be achieved (see also section 1.3).
In the context of maintenance, it is important to understand that PdM for industrial applications is a niche but rapidly growing segment within the much broader field of maintenance use cases. Therefore, only functionalities which are directly enabled because of PdM, namely predicted remaining useful lifetime of an asset, are the main focus of this Submodel. Topics out of the scope of this Submodel are maintenance instructions and preparation, corrective maintenance, predetermined or condition-based maintenance. Figure 1 shows a schematic overview on types of maintenance adapted from DIN EN 13306. Appendix B provides a future vision for the embedding of PdM Submodel in the context of maintenance as a whole and its connections to other existing and potential Submodels

Furthermore, it is important to understand that the aforementioned predicted useful lifetime of an asset in the sense of predictive maintenance is not static. Rather it depends on the concrete use of the asset in a specific process environment. In that regard, this prediction is impacted by the constant changes of the process values, which cause wear and tear to the asset. 

![image](https://github.com/user-attachments/assets/af28110d-2209-452f-a8bc-2616bfa4f30a)
Figure: Schematic overview on types of maintenance adapted from DIN EN 13306.

## About this version

This version is the first version officially published by IDTA


## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box)
