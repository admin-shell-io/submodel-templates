
# Data Model for Asset Location (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 

The location of static or mobile objects (assets / goods / trackables) and, if applicable, the origin and 
destination of transport processes are naturally the most important information in transport and internal 
logistics. In the past, the postal address or a simple location description (e.g., hall B, aisle 3) or a GNSS 
coordinate (Global Navigation Satellite System, like GPS) was sufficient as location information for 
controlling logistics processes. 
With the increasing propagation of localization technologies such as Ultra-Wideband (UWB), BLE (Bluetooth 
Low Energy), RFID (Radio-Frequency Identification) and others, the continuous and precise tracking of 
objects becomes possible at reasonable costs. This opens up new possibilities for the automation, 
monitoring and analysis of goods flows and internal transportation tasks. It is also possible to measure 
masses of localization data for short distances within buildings, which is why the integration of a localization 
solution into warehouse systems or production lines is becoming increasingly popular. The systems for 
localization are usually referred to as real-time location systems (RTLS).
Automated guided vehicles (AGVs) and autonomous transport robots with free navigation (AGVs) are also 
increasingly being used for internal transportation tasks. These are another driver for the use of localization 
technologies in companies.
Location data for assets are determined by different localization systems during the life cycle and even at the 
same point in time more than one system can deliver a location information. Today location data originate 
from a variety of non-interoperable systems, for which the data model for the localization information is not 
standardized.
Since asset location data are generated and used by different systems, for different use cases, in different 
life cycle phases and by different organizations it makes particular sense to manage the location data in the 
AAS of an asset in the form of a standardized Submodel.

## About this version

This version is the first version officially published by IDTA


## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box)
