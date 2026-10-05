# Asset Interfaces Description (Version 1.2)

This is a Submodel template specification for the Asset Administration Shell.

## Scope of the Submodel

This Submodel specifies an information model and a common representation for describing the interface(s) of an asset service or asset-related service. Based on this information, it is possible to initiate a connection to such kind of service and start to request or subscribe to served datapoints, and/or perform operations. Such datapoints of a system service can be, for example, various sensor and/or status values, and an operation can trigger an actuator, such as switching a motor "on" or "off".
The Asset Interfaces Description (AID) in version 1.2 supports the description of interfaces based on following specific protocols:

- Modbus
- HTTP
- MQTT
- OPC UA
- BACnet
- IO-Link
- SNMP
- CAN

The W3C Web of Things Thing Description (WoT TD) as an open, royalty-free standard is considered as a baseline for the content and structure of the definition of this Submodel template. The protocol-specific information is taken from the official WoT bindings that are maintained by the W3C or other SDOs like the OPC Foundation (e.g., OPC 10101 for OPC UA Binding).
In addition to the protocol-specific information provided by the AID, it also provides the ability to reference external descriptors such as GSD, GSDML, IO Device Description, native WoT TD (as a supplement), etc. This external descriptor is not restricted to the protocols currently defined in AID.
As a complement to the AID, an Asset Interfaces Mapping Configuration (AIMC) Submodel can be used to map the received data from the asset services to a specific place within an AAS (e.g., an application-specific Submodel to monitor data). The principal scope and use of the AID Submodel in combination with an AIMC is explained in the following figure:

![Figure 1 - AID Submodel usage and mapping process](https://github.com/admin-shell-io/submodel-templates/assets/93717810/02879e8f-8028-47d0-be8c-fcb3d6395457)

The legends in Figure 1 are described as follows:

1. Asset Interfaces Description Submodel: it holds the description model of the asset service (or asset-related service) interfaces and its datapoint.
2. Data Mapping Processor (DMP): This is a software component that provides connection (e.g., via Modbus) to the asset service and/or asset-related service and exchanges data as defined within the AID Submodel. It also manages the mapping of retrieved data to a desired SM according to AIMC SM definition. Note: The location of the DMP should not be derived from the figure above. The DMP can be part of an internal implementation or can be operated externally.
3. Data transmission channel between Data Mapping Processor and asset service. Depending on the underlying protocol (e.g., Modbus, MQTT, OPC UA) used by the asset service (and as described by the AID), the specific datapoint can be requested/subscribed.
4. Data transmission channel between Data Mapping Processor and asset-related service. Depending on the underlying protocol (e.g., HTTP) used by the asset-related service (and as described by the AID), the specific datapoint can be requested/subscribed.
5. AIMC Submodel: it provides the necessary information about the mapping of the datapoints described by the AID to elements in a desired (application-specific) operation data Submodel.
6. Operational Data Submodel: it is a Submodel where the (runtime) data is being stored. The details about this location are in the AIMC. With AIMC's information, the Data Mapping Processor can correctly map the asset's data to the right parts of the Submodel.
7. HTTP/REST Interface: This is an AAS Interface defined in details of AAS Part 2 as a standardized API. It is used to enable communication between AASX server and external applications.

## Not in scope of the Submodel

Out of the scope of AID 1.2 is the detailed definition of actions and events of asset interfaces. AID 1.2 focuses on monitoring purposes and thus concentrates on property definitions. The actions and events paradigm will be introduced in one of the forthcoming AID versions.

## About this version

This version is the minor release 1.2 of the Submodel template officially published by IDTA.

The Submodel semanticId is `https://admin-shell.io/idta/AssetInterfacesDescription/1/2/Submodel` (templateId `02017-1-2`).

### Artifacts in this directory

- PDF: IDTA 02017_Submodel_Asset Interfaces Description.pdf
- AASX: IDTA 02017_Template_Asset Interfaces Description.aasx (AAS metamodel V3.1)
- JSON: IDTA 02017_Template_Asset Interfaces Description.json
- AASX: IDTA 02017_Example_Asset Interfaces Description.aasx (example with values)

## Difference to prior versions

Version 1.1 is available under [`../1`](../1), with its bug-fix release 1.1.1 under [`../1/1`](../1/1). Version 1.0 is available under [`../0`](../0).

Main changes from 1.1 to 1.2 (see Annex G of the specification):

- New protocol bindings for SNMP and CAN, each with its own interface semanticId (`.../AssetInterfacesDescription/1/2/SNMP`, `.../AssetInterfacesDescription/1/2/CAN`) and base/href definitions.
- IO-Link moves from an informative annex to a normative binding section (`iolv_*` terms in `forms`, including payload mapping and enumerated values).
- CAN binding terms in `forms` (`canv_offset`, `canv_length`, `canv_valueOffset`, `canv_payloadMapping`, `canv_enumeratedValues` and nested elements).
- `EndpointMetadata`: `base` is now optional, and the new `protocolVersion` element supports protocol versioning.
- The Submodel semanticId changes to version 1.2.
