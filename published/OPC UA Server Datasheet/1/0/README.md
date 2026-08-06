# OPC UA Server Datasheet (Version 1.0)

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel

This Submodel specifies an information model that facilitates the configuration of OPC UA clients and provides the identification of an OPC UA Server responsible for the asset described by the Asset Administration Shell. Based on this information, it is possible to keep the information of an OPC UA Server consistent across a device life cycle.

For the configuration part, OPC UA Server Datasheet in version 1.0 supports the embedding of NodeSet files and other configuration information that are necessary for a client application. It uses the BuildInfo object information of the IEC 62541 Part 5 [10] specification to identify the server in a cluster of multiple servers. Lastly, OPC UA Server Datasheet provides endpoint information of already deployed servers by using the EndpointDescription object information of the IEC 62541 Part 4 [9] specification.

This document was developed by a Joint Working Group (JWG) consisting of members of IDTA and OPC Foundation.

The usage of the OPC UA Server Datasheet in the operational phase of a device life cycle is in two parts. First is by a native OPC UA client (AAS user application, green square) in Figure 1 that uses the OPC UA Server Datasheet Submodel through AASX file or over AAS REST API [7] to understand what the OPC UA Server responsible for an asset offers. The other part is by an OPC UA client (asset integration, black square) in Figure 2 that is enabled by the Submodel template Asset Interfaces Description (AID).

<img width="1004" height="348" alt="image" src="https://github.com/user-attachments/assets/6cce0ce7-83a5-4e9b-8e4c-dd13eb16482e" />

Figure 1: Overall blueprint of OPC UA asset integration with native OPC UA client.

<img width="1004" height="391" alt="image" src="https://github.com/user-attachments/assets/6ab5a057-d19f-4540-85a2-fb2d04a3fb06" />

Figure 2: Overall blueprint of OPC UA asset integration with AID.

## About this version

This version is the first version officially published by IDTA.

## Difference to prior versions

No prior versions were officially published.

## Status

This version is in productive use.
