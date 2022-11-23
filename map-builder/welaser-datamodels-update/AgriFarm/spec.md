Entity: AgriFarm  
================
  
Global description: **This entity contains a harmonised description of a generic farm made up of buildings and parcels. This entity is primarily associated with the agricultural vertical and related IoT applications.**  

This is taken from https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriFarm/doc/spec.md

## List of properties  

- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `contactPoint`: The details to contact with the item.  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `hasAgriParcel`: List of agri parcels belonging to the farm  
- `hasBuilding`: List of buildings belonging to the farm  
- `id`: Unique identifier of the entity  
- `landLocation`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `ownedBy`: Owner (Person or Organization) of the farm  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `relatedSource`: List of IDs the current entity may have in external applications  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: NGSI Entity Type. It has to be AgriFarm  
- `hasRestrictedArea`: List of restricted areas belonging to the farm  
- `hasRoad`: List of roads belonging to the farm  
