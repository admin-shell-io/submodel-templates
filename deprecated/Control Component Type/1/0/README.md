# Control Component Type (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 

The scope of this Submodel is the definition of type-specific information of a Control Component (CC) into an AAS. Together with its counterpart, the CCInstance Submodel (IDTA 02016), both Submodels aim to establish templates to ensure a uniform structure. The use of these templates allows the development of manufacturer- and domain-independent control concepts and facilitates the exchange of process information with other Submodels. Additionally, it allows the use of standardized call and monitoring sequences, as well as standardized description of its services, endpoints, error-codes, etc.

![image](https://user-images.githubusercontent.com/93717810/231377636-d7861e44-d581-40e7-8d3b-c168d472255c.png)

 
Figure 1: Using Control Components as Abstract Asset Type
As depicted in Figure 1, the CC concept is used to unify terms as an abstraction of a variety of domains, e.g. ranging from pumps, valves, handling robots, conveyors, packaging machines or process modules to PID, MPC or sequence controllers. Hence, the scope of the Submodels is wide regarding the types of assets, which are already covered in their own domain specific standards, e.g. OPC UA Companion Specifications. In return, the Submodels scope is condensed to common aspects of all these assets from different domains by focusing the use case of orchestrating them in a combined setup. Nevertheless, the Submodels will refer to other standards in certain aspects whenever they are applicable to a broad range of domains, e.g the PackML State Machine to define the activity of a CC.
 
 ![image](https://user-images.githubusercontent.com/93717810/231377732-88252851-8dc3-4fb0-bee8-73f4d83f7260.png)

Figure 2: Simplified Control Component Metamodel and Profile Description
Although CCs behave different depending on their domain, every CC expresses some form of current status (state variables, parameters, …) and operations (command variables, methods, …) to affect those states at its interface, as modelled on the left side of Figure 2. Otherwise, it could not be used in a process control architecture. An easy explanation is that every control component can be at least told when (start, stop, …) it should perform what. And what is decribed as skills (program, task, operation mode, service, procedure, …) which a control component can perform. The CC Submodels try to grasp that semantic core of a component.
A further classification of CCs by so called profiles may be added in the future, as shown on the right side of Figure 2. The profile of a CC describes which features it realizes in terms of standardized facets . Therefore, a common semantics must be defined first, to classify CCs in an abstract and machine-readable way. For example, execution modes like automatic and manual need to be mapped to the corresponding terms in various standards, in order to describe whether a CC supports such modes and corresponding mode changes. The German VDI/VDE GMA is working on a guideline (FA 7.21 Guideline Control Components) to define this common semantics based on definitions [9] from a funding project (BaSys4.2).



## About this version

This version is the first version officially published by IDTA


## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box)

## Update of AASX File for Compatibility with Version 3.0 of the "Asset Administration Shell" Metamodel Specification

The AASX file has been updated for compatibility with version 3.0 of the Asset Administration Shell metamodel specification. The contents of the submodel remain unchanged.
