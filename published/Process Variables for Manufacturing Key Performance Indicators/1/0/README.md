# Process Variables for Manufacturing Key Performance Indicators (Version 1.0)

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel

In industrial production environments, heterogeneous landscapes of production systems (machines) are common. These landscapes facilitate high flexibility in production processes due to varied production capabilities that can be combined in a modular way. However, the control and optimization of the production flow by Manufacturing Operations Management (MOM) and its subsystem, the Manufacturing Execution System (MES), become more complex when heterogeneous machinery is used.

Manufacturing Key Performance Indicators (KPIs), such as Overall Equipment Effectiveness (OEE), play a crucial role in assessing and optimizing MOM. To calculate KPIs, defined process variables for all available machines are required. These process variables can be derived from combinations of user-defined machine signals.

For example, process variables indicating whether a machine is producing, in error mode, or idle can result from logical combinations of machine signals. For one machine, this combination could include:

- automatic mode is active
- override <> 0
- program is running
- start cycle

For another machine, the combination could include:

- automatic mode is active
- program is running
- override = 100%
- spindle drive = 100%
- NC ready

MES vendors must analyze each machine type regarding communication interface, signal meaning, and communication protocol used to transfer signals to the MES in order to derive typical process variables as defined and standardized in ISO 22400-2. After deriving process variables for single machines, OEE can be calculated.

This process often requires collaboration between MES vendors, operators, and machine manufacturers, which leads to complex coordination and consultation needs because different departments use different terminology and concepts, and because customers may be entering new territory when integrating into an MES for the first time.

The Submodel "Process Variables for Manufacturing KPI Calculation" (PVM) defines an initial set of specified process variables, based on ISO 22400-2, required by MES. The current values of these process variables should be provided via the Submodel so other applications can use them, for example to automatically compute Manufacturing KPIs for heterogeneous machinery.

The Submodel is intended to be used as a standalone Submodel as well as in combination with already published Submodels, specifically the Asset Interface Description [7] and Asset Interface Mapping Configuration Submodel [8]. The developed solution considers the existence of different communication protocols and PLCs while providing a standardized information model for process variables required by MES and other systems. Furthermore, this Submodel is designed to be extensible and to serve as a foundation for computing Manufacturing KPIs beyond its initial scope.


## About this version

This version is the first version officially published by IDTA.

## Difference to prior versions

No prior versions were officially published.

