# Capability Description (Version 1.0)

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel

The Capability Description Submodel is used to model process or product requirements (required capabilities) and resource capabilities (provided capabilities) in a specified way. This enables reliable comparison between required and provided capabilities and supports efficient planning and orchestration of production processes.

The Submodel is based on the definition from [8], [9], where a capability is an "implementation-independent specification of a function in industrial production to achieve an effect in the physical or virtual world". As described in [8], the capability class has three central relationships. It is restricted by constraints, specified by properties, and realized by skills.

- Properties specify the capability in more detail (e.g., maximum speed, allowed tolerances, or temperature range).
- Constraints are divided into two types that further restrict the capability:
  - Property constraints: these refer to properties of a capability (e.g., temperature) and can be used as preconditions, invariants, or postconditions.
  - Transition constraints: these refer to relationships between multiple capabilities to determine sequence or parallel flow (e.g., transport must occur before tempering).
- Skills implement a capability in the form of technical or software-based solution modules.

Overall, the Capability Description Submodel provides a basis for defining required capabilities in a production process and matching them with provided capabilities of available resources. It is intended to be used by production planners, machine manufacturers, and plant operators.


## About this version

This version is the first version officially published by IDTA.

## Difference to prior versions

No prior versions were officially published.