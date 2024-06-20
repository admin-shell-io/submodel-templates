# Asset Interface Mapping Configuration (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 

This Asset Interfaces Mapping Configuration (AIMC) Submodel specifies an information model and a 
common representation for describing the mapping of interface(s) of an asset service or asset-related 
service already described in an Asset Interfaces Description (AID) Submodel. It can be understood as a 
configuration Submodel for south-bound communication between AAS and asset. Based on this information 
in the AIMC Submodel, it is possible to configure and initiate a connection to an asset service and map 
payloads to intended locations in an AAS automatically, and vice versa. 
As a complement to the AID, an AIMC Submodel is specified to map the received data from asset services to 
a specific place within an AAS (e.g. an application specific Submodel to monitor or log data). The principle 
scope and use of the AID and AIMC Submodels is explained in the following Figure 1.
Even though AID and AIMC can be closely used together, they are separated Submodels. AID describes 
available interfaces of an asset and is usually provided by the asset provider. On the other hand, AIMC 
configures a (bidirectional) mapping between an asset and an AAS and is usually provided by the asset 
user. Furthermore, an AIMC in an AAS A might reference an AID in an AAS B.
• Example 1: An AAS shall integrate data from the asset it represents uniquely. Consequently, AID 
and AIMC are both integrated into the only one AAS of the asset.
• Example 2: An AAS of a product shall integrate product specific production data from a machine that 
manufactures the product. In this case, the AIMC in the AAS of the product references an AID in the 
AAS of the machine.
The AIMC 1.0 adapts to the structure and protocols supported by AID 1.0 standard: MQTT, HTTP and 
Modbus. In this version only a unidirectional mapping from asset to AAS is considered. Subsequent releases 
of AID versions may trigger the release of adapted AIMC versions.

![image](https://github.com/admin-shell-io/submodel-templates/assets/111876087/13b8b6c0-f2bb-4b64-bc10-d3bae3f2a517)



## About this version

This version is the first version officially published by IDTA 


## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box).



