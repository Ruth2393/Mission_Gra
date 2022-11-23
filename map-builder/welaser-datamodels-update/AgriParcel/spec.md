Entity: AgriParcel  
==================
  
Global description: **This entity contains a harmonised description of a generic parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.**  

This is taken from https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriParcel/doc/spec.md

## List of properties  

- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `area`: The area of the parcel nominally in square meters.  
- `areaServed`: The geographic area where a service or offered item is provided  
- `belongsTo`: Entity the item belongs to  
- `category`: The category of the parcel of land e.g.: **arable, grassland, vineyard, orchard, mixed crop, lowland, upland, set-aside, forestry, wetland.**  
- `cropStatus`: Enum:'seeded, justBorn, growing, maturing, readyForHarvesting, *UNSEEDED*'. A choice from an enumerated list describing the crop planting status  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `hasAgriCrop`: Reference to the crop associated with this parcel  
- `hasAgriParcelChildren`: Related sub AgriParcel records to which this entity relates  
- `hasAgriParcelParent`: Reference to the parent AgriParcel  
- `hasAgriSoil`: Reference to the soil associated with this parcel of land  
- `hasDevices`: Reference to the IoT devices associated with this parcel i.e. sensors, controls.  
- `id`: Unique identifier of the entity  
- `lastPlantedAt`: Indicates the date when the crop was last planted  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `ownedBy`: Owner (Person or Organization) of the item  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `relatedSource`: List of IDs the current entity may have in external applications  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: NGSI Entity Type. It has to be AgriParcel  

- `bearing`: Gives the vehicle GPS angle measured in a clockwise direction from the True North. SameAs 'bearing' field from GTFS Realtime message-Position (https://developers.google.com/transit/gtfs-realtime/reference#message-position)
- `headlandWidth`: Number (meters)
- `gateLocation`: Geojson reference to the item. It can be Point or MultiPoint
- `interRowDistance`: Number (meters)
- `cropRow`: representation of the crop rows. Geojson reference to the item. It can be MultilineString
- `weedStatus` (TBD)
