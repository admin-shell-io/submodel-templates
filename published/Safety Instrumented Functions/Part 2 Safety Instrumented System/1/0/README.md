# Safety Instrumented System (Version 1.0)

This is a Submodel template specification for the Asset Administration Shell.

## Scope of the Submodel

A Safety Instrumented System (SIS) is the instrumented system that implements one or more Safety Instrumented Functions. It comprises sensors, logic solvers and final elements, together with the interfaces to the other systems of the plant.

This Submodel aims to provide a standardized and machine-readable way to exchange the requirements allocated to a safety instrumented system and the information describing how it interfaces with its environment, so that this data can be exchanged between plant operators, system integrators and manufacturers instead of being held in documents.

The Submodel covers the following subject areas:

- **System identification**: the name of the safety instrumented system, for example an ESD, PSD or F&G system
- **Safety requirements**: the requirements allocated to the system from the safety requirement specification according to IEC 61511, including survivability and the requirements for starting up and restarting the system
- **Interfacing systems**: the systems the SIS interfaces with, such as the process control system, the operator interface or another SIS, together with the network type and the nature of the links
- **Supporting documents**: the performance standard, the application program safety requirements, the design accidental load specification and further relevant documents

The individual safety instrumented functions the system implements are described by the Safety Instrumented Function Submodel, and the devices making up the system by the SIS Device Submodel.

## About this version

This version is the first version officially published by IDTA.

## Difference to prior versions

No prior versions were officially published.
