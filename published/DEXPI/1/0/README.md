# Information Model for P&I Diagrams based on DEXPI Standard (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 

The engineering of a process plant is a complex multi-disciplinary and multi-organizational process involving exchange of a vast number of (semi-)standardized artifacts like diagrams, drawings, tables, certificates, and other documents. 
One core artifact which is created and extended during the engineering process is the Piping & Instrumentation Diagram (P&ID) providing among others a good balance of abstraction between the physical layout of the plant (i.e., used equipment and piping connections) and its representation within the automation domain (i.e., signal types, tag names, logical connections between sensor and actuators). Due to this fact P&IDs are long-living artifacts which are frequently used during the whole plant’s lifecycle beyond the engineering phase [7]. 
Even though most engineering artifacts are created digitally, they are not necessarily exchanged in a machine-readable format. The lack of a machine-readable representation of engineering artifacts (including P&IDs) hinders the digital transformation and can be a showstopper for digital use-cases due to high costs of creation of a machine-readable P&ID representation.
Efforts to create a standardized machine-readable exchange format for P&ID are made by the DEXPI working group of DECHEMA including operators from multiple verticals (e.g., Oil and Gas, and Chemistry), engineering companies, software tool vendors and research institutes. DEXPI [8] is an UML-Model implemented using an XML-based P&ID exchange format including multiple aspects of plant design like piping topology and its graphical representation, instrumentation structure, tag names. DEXPI is an open industrial standard aiming for a broad usage across industrial domains.
Due to the paramount role of P&ID during the whole plant’s lifecycle, the importance of DEXPI has been identified by the Industry 4.0 community. Inclusion of DEXPI models into a standardized lifecycle information container – the Industry 4.0 Asset Administration Shell (AAS) – would facilitate links between different disciplines, organizations and industry domains. Mapping of DEXPI models to the AAS by defining an AAS Submodel template is governed by Industrial Digital Twin Association (IDTA) where a respective working group was founded in 2022. The group consists of representatives of the DEXPI working group, oil and gas industry, engineering and procurement companies, automation equipment suppliers, and research institutes.

## About this version

This version is the first version officially published by IDTA

## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box)

## Update of AASX File for Compatibility with Version 3.0 of the "Asset Administration Shell" Metamodel Specification

The AASX file has been updated for compatibility with version 3.0 of the Asset Administration Shell metamodel specification. The contents of the submodel remain unchanged.

