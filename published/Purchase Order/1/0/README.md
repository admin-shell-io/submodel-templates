# Purchase Order (Version 1.0) 

This is a Submodel template specification for the Asset Adminstration Shell.

## Scope of the Submodel 

The Purchase Order Submodel is designed to enable the interoperable provisioning of information related to a purchase order issued by a buyer / customer to a seller / supplier concerning a specific asset, in alignment with the Asset Administration Shell (AAS) framework. A key element of this submodel is the inclusion of properties [7], ideally enhanced by semantic interoperability through the use of standardized dictionaries such as ECLASS and the IEC Common Data Dictionary (CDD).

The purpose of this document is to specify submodels that allow for the meaningful exchange of asset- related information between partners across the supply chain. It focuses specifically on purchase order processes and the data exchanged during these transactions.

The intended use case is the provision of a standardized data structure for purchase orders. This structure enables the interoperable and unambiguous exchange of essential information, starting from a purchase request, progressing through a quotation, and culminating in the issuance of a formal purchase order.
 
 <img width="982" height="565" alt="image" src="https://github.com/user-attachments/assets/144643ad-83a8-42d0-86bd-47089f6596e8" />

Figure 1. Overview of the purchase order process and fulfillment. The scope of the Submodel Purchase Order is highlighted in blue.

Figure 1 provides an overview of the entire purchase order and fulfillment process. The scope of the Purchase Order Submodel is highlighted in blue and includes the request for quotation (also referred to as a purchase request), the quotation, and the purchase order itself. Activities not within the scope of this submodel include shipment and delivery, receipt confirmation, damage and loss reports, and invoicing. However, any relevant information pertaining to these downstream processes—if required during the ordering phase—is considered within the submodel’s structure.

The conceptual design of the submodel builds upon existing standards, industry practices, guidelines, and de facto norms, aiming for broad acceptance and applicability.

The Asset Administration Shell (AAS) is utilized to represent information throughout the purchase order process. This includes business-to-business (B2B) transactions in which companies procure production components or resources required for more complex assemblies and products along the value chain.

To support this, the information exchange required for a purchase request, its response (quotation), and the resulting purchase order is standardized. This enables a buyer or customer to order materials, products, or services from one or more sellers or suppliers through a structured, interoperable format. Standardization and interoperability are essential because this information is typically processed by backend systems such as ERP, CRM, and others.

The potential transferability of the submodel to business-to-consumer (B2C) scenarios—where end customers order products—is also considered.

A crucial aspect of seamless order processing is the structured provision of item lists for the requested product, as well as information on the required production resources, delivered in the form of a work plan. Conversely, buyers or customers—such as Original Equipment Manufacturers (OEMs)—often face the challenge of requesting and ordering the production of subcomponents or parts from a broad range of different suppliers.

If a purchase request refers to a non-standard, made-to-order product (i.e., not available off the shelf), manual feasibility checks must often be performed by production planners. These checks can be time- consuming and error-prone, particularly in non-standardized processes or when multiple product variants are involved. 


## About this version

This version is the first version officially published by IDTA


## Difference to prior versions

No prior versions were offically published.

