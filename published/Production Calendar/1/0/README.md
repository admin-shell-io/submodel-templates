
# Production Calendar (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 
This Submodel defines a general interoperable representation of production calendars, detailing operating times within the industrial domain. It includes a template to retain one production calendar in the MIME-Type iCalendar (iCal), as specified in RFC 5545. The objective of this Submodel is to establish a single source of truth that facilitates the synchronization and utilization of production calendars across various applications.

For instance, this Submodel can be utilized by Manufacturing Execution Systems (MES) and Value Chain Simulations to exchange information such as shift schedules for individual production systems and workstations. Additionally, the Submodel could also be used to define the shift schedule in departments and companies if they are described through their own AAS. The production calendar Submodel in the higher business levels could be used to affect the production planning process in the single departments at lower levels. Thus, this Submodel allows the inheritance of one production calendar from another, enabling external applications to implement complex industrial use cases, like the aggregation of operating times of a works environment comprising multiple locations, departments, and machinery.

The definition of a production calendar using an AAS Submodel ensures that the production calendar is available in a standardized, machine-readable form. This allows different systems (MES, ERP, SCADA, etc.) to interpret and synchronize the same calendar data. Defining a production calendar as an AAS Submodel Template thus provides a standardized, automated and interoperable basis for calculating KPIs.

However, since the iCal format provides only abstract guidelines, it lacks sufficient standardization for industrial applications. Therefore, it is essential to first specify the necessary variables for accurately describing the content of the production calendar. These variables are defined in the Submodel itself and should be extended by the working group to assure the interoperability within the extended iCal format.

## About this version

This version is the first version officially published by IDTA


## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box)



