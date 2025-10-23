
# Maintenance Instructions (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 

### Definition maintenance:

The process of preserving a condition or situation or the state of being preserved.

### Distinction between predictive and preventive maintenance:
The main difference between both maintenance concepts is that preventive maintenance is scheduled at regular intervals while predictive maintenance is scheduled as needed (based on asset conditions).

This Submodel template is focused on the handover of preventive maintenance instructions.
Within the product life cycle of components, machines and production facilities (see Figure 1), maintenance is an essential part of maintaining productivity. Preventive maintenance can be planned and is usually carried out at set intervals. For planned maintenance, appropriate preparation for planning and execution is necessary. For this purpose, information is provided by the manufacturer. In reality, this information is often provided in the form of a PDF containing all the necessary information on maintenance, which is then passed on. Component manufacturers pass on their information to the machine/plant builder, who then has the task of creating the maintenance instructions for the machine/plant based on all the information. 
The disadvantage of the current solutions: maintenance information often has to be collected manually from various sources/documents and transferred by copy & paste, e.g. into a maintenance software. This process is very resource-intensive and offers room for mistakes. 

The intended use case starts here and aims at providing an interoperable Submodel on the topic of maintenance. All required information on maintenance is to be passed on - ideally with the help of dictionaries such as ECLASS and IEC CDD (Common Data Dictionary). While in the current version most of the specified properties have an IRI as semantic identifier, a complete harmonisation of all properties is aimed at for a successor version if possible. The structure by means of SubmodelElementCollections (SMC) is intended to simplify the evaluation and use of the information, especially the spare parts, consumables and tool lists.
This Submodel is not intended for calibrations, or the documentation of maintenance work carried out or calibration values from measurements. However, it can be used as a basis for this.

### Important Note:
This Submodel is not suitable for unplanned repair tasks!

## About this version

This version is the first version officially published by IDTA


## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box)
