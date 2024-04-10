# Hierarchical Structures enabling Bills of Material (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 

This Submodel Template aims to provide hierarchical structures applicable to industrial equipment in an interoperable manner. For this primarily Entities and Relationship Elements of the AAS Metamodel are used.
This industrial equipment, for example production lines, modules and sub systems, are provided by partners in the value chain, such as suppliers, equipment manufacturers and systems integrators and used in specific applications by industrial operators and end users, both in factory as also process automation. Industrial equipment can be composed of subsystems down to material and component level, can include produced products and can be described on type or instance level.
The AAS contains Submodels that cover aspects of the assets among their life cycle. Already in the design phase, assets are composed and aggregated into newly created hierarchical structures. 
Typically, assets have their own AAS (Entity with entityType “SelfManagedEntity"), but it is possible that an Asset has no AAS and is represented by a co-managed Entity.
Since nesting of AAS and Submodels is forbidden by the metamodel, this Submodel is intended to provide a description of the internal structure of an asset. It shall allow the consumer of an AAS to identify assets and their corresponding entities and find their respective AAS if they exist. The Submodel serves as an index, pointing to Assets (described as co- or self-managed entities) and AAS in a distributed network capable of transcending the limits of a single organization.
Instances of this Submodel Template shall be the authoritative source for hierarchical structures within an AAS during all lifecycle phases. Complementing information about each asset and their own lifecycle phase is enabled to be discoverable into the n-th level of the hierarchy and across the whole supply chain depending on the design of the Submodel Instance.


## About this version

This version is the first version officially published by IDTA


## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box)

## Update of AASX File for Compatibility with Version 3.0 of the "Asset Administration Shell" Metamodel Specification

The AASX file has been updated for compatibility with version 3.0 of the Asset Administration Shell metamodel specification. The contents of the submodel remain unchanged.
