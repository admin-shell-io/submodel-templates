# Asset Interfaces Description (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 

This Submodel specifies an information model and a common representation for describing the interface(s)
of an asset service or asset related service. Based on this information, it is possible to initiate a connection to 
such kind of service and start to request or subscribe to served datapoints, and/or perform operations. Such 
datapoints of a system service can be, for example, various sensor and/or status values, and an operation 
can trigger an actuator, such as switching a motor “on” or “off”.
The Asset Interfaces Description (AID) in version 1.0 supports the description of interfaces based on three 
specific protocols: Modbus, HTTP and MQTT. Any other protocols and interfaces will be addressed in 
upcoming versions of the AID. As a forward-looking note, the AID working group at IDTA has outlined plans 
for the AID 1.1 version to incorporate support for both OPC UA (joint activity with the OPC Foundation) and 
BACnet.
The W3C Web of Things Thing Description (WoT TD) as an open, royalty-free standard is considered as a 
baseline for the content and structure of the definition of this Submodel template.
In addition to the protocol specific information provided by the AID, it also provides the ability to reference 
external descriptors such as GSD, GSDML, IO Device Description, WoT TD (as a supplement) etc. These 
external descriptor is not restricted to the protocols currently defined in the AID.
As a complement to the AID, an Asset Interfaces Mapping Configuration (AIMC) Submodel can be used to 
map the received data from the asset services to a specific place within an AAS (e.g. an application specific 
Submodel to monitor data). The principle scope and use of the AID Submodel in combination with an AIMC 
is explained in the following figure:
![image](https://github.com/admin-shell-io/submodel-templates/assets/93717810/02879e8f-8028-47d0-be8c-fcb3d6395457)

Figure 1 Principle AID submodel usage and possible data mapping process e.g. by Asset Interfaces

Mapping Configuration (AIMC).
The number legends in Figure 1 are described as follows:
(1) Asset Interfaces Description Submodel: it holds the description model of the asset service (or asset 
related service) interfaces and its datapoint.
(2) Data Mapping Processor (DMP): This is a software component that provides connection (e.g., via 
Modbus) to the asset service and/or asset related service and exchanges data as defined within the 
AID Submodel. It also manages the mapping of retrieved data to a desired SM according to AIMC 
SM definition.
(3) Data transmission channel between Data Mapping Processor and asset service. Depending on the 
underlying protocol (e.g. Modbus, MQTT) used by the asset service (and as described by the AID), 
the specific datapoint can be requested/subscribed.
(4) Data transmission channel between Data Mapping Processor and asset related service. Depending 
on the underlying protocol (e.g. HTTP) used by the asset related service (and as described by the 
AID), the specific datapoint can be requested/subscribed.
(5) AIMC Submodel: it provides the necessary information about the mapping of the datapoints 
described by the AID to elements in a desired (application-specific) operation data Submodel.
(6) Operational Data Submodel: it is a Submodel where the (runtime) data is being stored. The details 
about this location are in the AIMC. With AIMC's information, the Data Mapping Processor can 
correctly map the asset's data to the right parts of the Submodel.
(7) HTTP/REST Interface: This is an AAS Interface defined in details of AAS Part 2 as a standardized 
API [11]. It is used to enable communication between AASX server and external applications.

## About this version

This version is the first version officially published by IDTA

## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box).
Additionally, Eclipse Thingweb implements it at <https://github.com/eclipse-thingweb/td-tools/tree/main/node/aas-aid> which is published on [npm](https://www.npmjs.com/package/@thingweb/aas-aid).

