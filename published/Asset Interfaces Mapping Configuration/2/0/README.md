# Asset Interfaces Mapping Configuration (Version 2.0)

This is a Submodel template specification for the Asset Administration Shell.

## Scope of the Submodel

The Asset Interfaces Mapping Configuration (AIMC) Submodel version 2.0 supports two use cases:

1. Asset-to-AAS mapping

Together with the Asset Interface Description (AID) Submodel, AIMC specifies how data provided by assets or asset-related services is mapped to target locations in an Asset Administration Shell (AAS). In this scenario, AIMC functions as a configuration Submodel for northbound communication between an asset and the enclosing AAS (for example, an application-specific Submodel for monitoring or logging).

2. AAS-to-AAS mapping

The AIMC can also specify mappings between locations within an AAS. For example, compute a singular value from multiple existing elements.

In both cases, a mapping defines the relationship between a set of sources (input data) and a set of sinks (output data) where results are written. An optional transformation step may be applied between sources and sinks to convert or process the input data into the desired output format or value.

In conjunction with the AID, the AIMC can help meet regulatory compliance requirements, including those under the EU Digital Product Passport and the EU Data Act. It achieves this by exposing machine-related data via the AAS in a standardized, machine-readable form. Even though the AID and AIMC are closely related, they serve different purposes and are therefore separate Submodels. The AID documents which interfaces an asset offers and is typically provided by the asset provider. The AIMC, by contrast, defines how data is mapped in one direction, optionally including a transformation step. This can be a mapping between an asset and an AAS by leveraging the AID, or a mapping between two AASs (AAS A to AAS B) without involving the AID. AIMC configurations are typically created by the asset user. Finally, the AIMC and AID do not have to be co-located in the same AAS and may be hosted separately.

Figure 1 illustrates how the two AIMC use cases can be combined into a two-step workflow. First, data is onboarded into the AAS by using the AID and AIMC together. Once the data is available in the AAS, the AIMC can be used independently of the AID to define how existing AAS data is mapped and optionally transformed into higher-level signals, such as KPIs, and written to other locations within the AAS domain.

Example AIMC usage patterns:

- Example 1: Onboard asset data into its own AAS. The AAS shall be populated with data coming directly from the asset it represents. Consequently, the AID and AIMC are both integrated into the AAS of the asset to onboard asset data into the AAS.
- Example 2: Onboard machine production data into a product AAS. The AAS of a product shall integrate product-specific production data from a machine that manufactures the product. The AIMC mapping capabilities are used to describe how selected machine data, identified via the machine's AID, are transformed into the product AAS.
- Example 3: Aggregate device state data into a production line AAS. The AAS shall aggregate signals from multiple devices of a production line to derive an overall "machine is running" signal. Each device provides live state data via its own AAS. The production line AAS is extended with an AIMC that maps the relevant device-state sources and uses its optional transformation step to compute the aggregated running signal, which is then written to a defined location in the production line AAS.

The AIMC 2.0 adapts to the structure and protocols supported by the AID 1.1 standard: Modbus, HTTP, MQTT, OPC UA, BACnet. Subsequent releases of AID versions may trigger the release of adapted AIMC versions.

<img width="501" height="204" alt="image" src="https://github.com/user-attachments/assets/3720ff4b-043a-4088-b114-2b19772e34f9" />

Figure 1. AIMC Use Cases

## About this version

This version is the official Submodel template version 2.0 published by IDTA.

## Difference to prior versions

This version is based on version 1.0 (IDTA-02027-1-0).
