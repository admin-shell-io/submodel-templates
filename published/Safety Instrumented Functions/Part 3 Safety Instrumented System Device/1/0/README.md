# Safety Instrumented System Device (Version 1.0)

This is a Submodel template specification for the Asset Administration Shell.

## Scope of the Submodel

A Safety Instrumented System Device is an individual device forming part of a Safety Instrumented System: a sensor, a logic solver or a final element. The reliability of each such device determines whether the safety instrumented functions it participates in can achieve their required Safety Integrity Level.

This Submodel aims to provide a standardized and machine-readable way to exchange the functional safety data of a device across its lifecycle, covering both the reliability data stated by the manufacturer at design time and the reliability data observed by the operator during operation. This allows design assumptions to be verified against field experience and supports the systematic evaluation of operational reliability.

The Submodel covers the following subject areas:

- **Tag information**: the plant identification of the device instance
- **Safety requirements**: the requirements allocated to the device from the safety requirement specification according to IEC 61511
- **Device model specification**: the type-level specification of the device, including its input, logic solver and final element characteristics
- **Reliability data (design)**: the failure rates, safe failure fraction and hardware fault tolerance stated for the device type
- **Reliability influencing properties**: the properties of the installation and process that affect the reliability of the device
- **Device instance specification**: the data specific to the installed instance
- **Bypass data**: the bypass arrangements and recorded bypass events
- **Diagnostics**: the diagnostic functions of the device and the alarms they raise
- **Device operation data**: operating time, surveillance time and repair times
- **Demand data**: the demands placed on the device during operation
- **Failure data**: the failures recorded against the device
- **Reliability data (operational)**: the failure rates derived from operational experience
- **Proof test data**: the proof test procedure, interval, coverage and recorded test events

General product characteristics that are not specific to functional safety are not covered here; they are provided by Submodels such as Digital Nameplate and Technical Data.

## About this version

This version is the first version officially published by IDTA.

## Difference to prior versions

No prior versions were officially published.
