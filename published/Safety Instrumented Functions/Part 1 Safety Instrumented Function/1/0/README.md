# Safety Instrumented Function (Version 1.0)

This is a Submodel template specification for the Asset Administration Shell.

## Scope of the Submodel

A Safety Instrumented Function (SIF) is a function implemented by a Safety Instrumented System to achieve or maintain a safe state of the process when a specified hazardous condition occurs. Each SIF is allocated a Safety Integrity Level (SIL) expressing the risk reduction it is required to deliver, and is realised by a combination of sensors, logic solvers and final elements.

This Submodel aims to provide a standardized and machine-readable way to exchange the information describing an individual Safety Instrumented Function across its lifecycle, so that it can be passed between the plant operator, the equipment manufacturer, the engineering contractor and the functional safety tools used in design and operation. It replaces the current practice of exchanging safety requirement specification data in documents such as PDF, Word and Excel.

The Submodel covers the following subject areas:

- **SIF specification**: identification and description of the individual safety instrumented function
- **Safety requirements**: the requirements allocated to the function from the safety requirement specification according to IEC 61511
- **Equipment under control**: the specification of the equipment whose risk the function reduces
- **Hazardous event**: the hazardous event the function is designed to prevent or mitigate
- **SIF configuration**: the input device, logic solver and final element groups realising the function, and their voting arrangement
- **Demand data**: the demands placed on the function during operation
- **Loop test data**: the loop tests performed on the function and their results
- **Performance measures**: the reliability performance achieved by the function

Information about the individual devices realising the function is not covered here; it is provided by the Safety Instrumented System Device Submodel. The safety instrumented system as a whole is described by the Safety Instrumented System Submodel.

## About this version

This version is the first version officially published by IDTA.

## Difference to prior versions

No prior versions were officially published.
