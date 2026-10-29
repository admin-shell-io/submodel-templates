# Interface Connector (Version 1.0)

This is a Submodel template specification for the Asset Administration Shell.

## Scope of the Submodel

This Submodel template aims at interoperable provision of product connection points between manufacturers and users of industrial product types and items, particularly industrial components. These industrial product types and items are typically provided by manufacturers and suppliers, including dealers, and are used by industrial users, e.g. original equipment manufacturers (OEMs), system integrators and producing enterprises (industrial end users). Product types have individual types and numbers of connection points, which are important to know for industrial users especially during engineering.

The aim of this Submodel is to digitalize and interoperably convey sets of minimal required information and to ease the handover of these information sets, so that this information can be efficiently filtered, monitored and stored in software systems on the industrial user's side. The intended use case is that a manufacturer of industrial product types and items provides data for all connection points of the product in a way that is interoperable and unambiguously understood by the other market participants, such as OEMs, system integrators or operators of industrial equipment.

Each connector of a component (for example an I/O device or a cable) is described individually, with Submodel element collections for its physical aspects. The following connection types are considered:

- Mechanical connection (screw, push-in, solder, welded, clamp, press and open connections)
- Electrical connection
- Pneumatic connection
- Hydraulic connection
- Optic connection

The connection points of a connector (for example the pins of an M12 plug) are described with their own properties and can be grouped into configurations, of which exactly one is active. Supplier-specific properties can be added via `AssetSpecificProperties`.

## About this version

This version is the first version officially published by IDTA.

## Difference to prior versions

No prior versions were officially published.
