# Nameplate for Software in Manufacturing (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 

Software becomes more and more an essential part in manufacturing value networks, in smart manufacturing, and in smart products. For an effective and efficient use and management of such software, it is necessary to gather relevant information in a uniform representation. Use cases like updates, patch management, license management, audits, etc. rely on information regarding identification, sources and features of software (Figure 1). This information shall be provided in a consistent manner in form of a “nameplate for software”, derived and specialized from a common digital nameplate as defined in [9].
 ![image](https://github.com/admin-shell-io/submodel-templates/assets/93717810/dd4048b1-bdf6-418a-af45-070d7fc5d12b)

Figure 1: Software in manufacturing and the nameplate for software
The nameplate for software applies to stand-alone software Assets (Figure 2), as well as to software as integral part of a physical Asset, e.g. firmware or application software of a machine, modelled as a composite component using hierarchies according to [11] (Figure 3). 

![image](https://github.com/admin-shell-io/submodel-templates/assets/93717810/c4f9ff30-b78b-410a-91bb-907daa949e10)
 
Figure 2: Software as an Asset
![image](https://github.com/admin-shell-io/submodel-templates/assets/93717810/cc1fda23-9457-45c2-be6a-7d65bded19cf)

Figure 3: Software as integral part of a composite component (e.g. machine)
This Submodel Template aims at interoperable provision of software nameplate data describing the asset of the respective Asset Administration Shell. Central element is the provision of properties [7], ideally interoperable by the means of dictionaries such as ECLASS and IEC CDD (Common data dictionary).
The intended use-case is, that a manufacturer of industrial equipment describes Assets (type or instance), which are provided to the market, by the means of software nameplate data (properties), which are interoperable and unambiguously understood by the other market participants, such as system integrators or operators of industrial equipment. For providing individual industrial equipment to the market, also a supplier is covered by the use-case (for this purpose seen as functioning as manufacturer).
This Submodel Template specifies two basic sets of SubmodelElements in order to describe the necessary information according to this use-case.


## About this version

This version is the first version officially published by IDTA


## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box)


## Update of AASX File for Compatibility with Version 3.0 of the "Asset Administration Shell" Metamodel Specification

The AASX file has been updated for compatibility with version 3.0 of the Asset Administration Shell metamodel specification. The contents of the submodel remain unchanged.
