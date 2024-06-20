# Data Retention Policies (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 

This Submodel describes a common representation of data retention policies that can be applied to elements 
in the Asset Administration Shell via semantic identifiers. Based on this information, it is possible to automate
the reduction, archiving, or removal of data stored in the Asset Administration Shell. Such data can be, for 
example, raw sensor data, large images, sensitive data, or any data that becomes obsolete over time.
A data retention policy defines how long data must be stored before it may be deleted. It also provides 
information about the policy provider, the specific requirement or law that enforces the policy, and the 
timeframe between which the policy is in effect. Additionally, the authorship of each policy can be traced 
through an audit log, in which all changes to the policy are documented. Based on this information, an 
automated service can apply and validate each policy against the data stored in the Asset Administration 
Shell and reduce, archive, or remove the data as necessary.
This Submodel allows a set of policies to inherit from another set of policies so that an existing policy can be 
extended or adjusted to more specific use cases. For example, business policies may be overridden or 
extended by contracts with more specific policies or longer retention periods.
The enforcement of data retention policies described by this Submodel are outside the scope of this 
document.

## About this version

This version is the first version officially published by IDTA


## Difference to prior versions

No prior versions were offically published.

## Status

This version is in productive use and supported by AASX Package Explorer (out of the box)
