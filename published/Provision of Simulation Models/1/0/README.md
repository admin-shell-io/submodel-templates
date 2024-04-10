# Provision of Simulation Models (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 

The presented Submodel allows the interoperable provision of simulation model files for an asset via the 
asset administration shell. The Submodel enables this for a wide range of simulation model types and 
simulation purposes. It contains information about the type of model, how to use the model, and the areas of 
application.
The main underlying class of models for this Submodel are DAEs, models described by differential algebraic 
equations. However, models of other types, such as CAD, FMEA, etc., can also be described. FEM type 
models are not considered explicitly, they will be covered by another Submodel by interest. The models
described by this Submodel may be provided in ASCII or binary form to be used with a specific simulation 
software (e.g. Matlab/Simulink, Virtuos, etc.), as source code (e.g. C, Modelica, etc.), or in a model exchange 
format such as FMI.
It describes rudimentarily the content of the model.
Assets, where you can provide simulation models via AAS, can be passive parts, active devices, 
subsystems, machines or even production plants. When using this Submodel template, it is requiered that 
the asset for which a simulation model should beprovided has an AAS. That is, if there are no AAS yet, first 
an asset-ID needs to be defined and an AAS created. A Submodel can then be added to this AAS.
In the first step, the Submodel supports searching and finding, as well as requesting simulation model files
from manufacturers or distributors.
In further steps, the Submodel will also support the automatic integration of a model into a specific simulation 
environment, up to an automatic generation of an overall simulation based on structural descriptions of a 
system containing different components. As it is possible with e.g., the Submodel candidate for hierarchical 
structures enabling “Bills of Material” (BoM).

## About this version

This version is the first version officially published by IDTA


## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box)

## Update of AASX File for Compatibility with Version 3.0 of the "Asset Administration Shell" Metamodel Specification

The AASX file has been updated for compatibility with version 3.0 of the Asset Administration Shell metamodel specification. The contents of the submodel remain unchanged.
