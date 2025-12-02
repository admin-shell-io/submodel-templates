# Quality Control for Machining (Version 1.0) 

This is a Submodel template specification for the Asset Administration Shell.

## Scope of the Submodel 

This Submodel template aims at interoperable provision of information describing quality control relevant data regarding the asset of the respective Asset Administration Shell. Central element is the provision of properties [7], ideally interoperable by the means of dictionaries such as ECLASS and IEC CDD (Common Data Dictionary). The purpose of this document is to make selected specifications of Submodels in such manner that information about assets can be exchanged in a meaningful way between partners in a value creation network. It targets quality control processes and metrology data measured for parts manufactured in cyclical production processes, particularly for, but not limited to machining processes.

The intended use-case is the provision of a standardized property structure for quality control in machining, which enables the standardized and automated assignment of metrology data of manufactured parts to their production parameters.

This concept can serve as a basis for standardizing the respective Submodel. The conception is based on existing norms, studies of common practices at enterprises, directives and standards so that a far-reaching acceptance can be achieved.

Beside a standardized Submodel this template also introduces standardized SubmodelEle¬mentCollections (SMC) in order to improve the interoperability while modelling aspects of quality topics within other Submodels.

The task of quality control is to check the quality of the intermediate or/and end products against customer requirements and applicable standards through inline inspections or in offline laboratory tests. The quality control process and results must be documented and relevant quality control documents must be collected and maintained. 

In the field of machining, there are already standardized characteristics for describing the dimensional and surface quality, which are used as test parameters in quality control. However, there are no standardized data formats for the representation and transmission of the definition of these characteristics across different instances. In practice, the assignment of data records from quality control to other data of the specific part, such as machine cycle data, is therefore a challenge that is often carried out manually or via automation steps individually tailored to the specific application and is therefore time-consuming and cost-intensive in operation and maintenance as well as error-prone. In particular, use cases in the area of Industry 4.0 and artificial intelligence require an efficient and error-free transfer of such data from one instance to another.

The Submodel addresses the interoperable standardized provision of data and information from quality inspections on manufactured parts, such as dimensional accuracy and surface quality. The focus of the Submodel is on machining processes. In order to achieve an easy transferability to other processes, the Submodel shall contain a section for the description of generally valid quality-relevant properties and a domain-specific section that contains the specific aspects for machining manufacturing processes. Within the machining processes, turning, milling and drilling are considered.


## About this version

This version is the first version officially published by IDTA

## Difference to prior versions

No prior versions were officially published.

