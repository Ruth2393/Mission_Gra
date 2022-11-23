Entity: Building
==================

Global description: **Information on a given Building.**  

This is taken from https://github.com/smart-data-models/dataModel.Building/blob/master/Building/doc/spec.md#list-of-properties

## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `category`: Category of the building. Enum:'apartments, bakehouse, barn, bridge, bungalow, bunker, cathedral, cabin, carport, chapel, church, civic, commercial, conservatory, construction, cowshed, detached, digester, dormitory, farm, farm_auxiliary, garage, garages, garbage_shed, grandstand, greenhouse, hangar, hospital, hotel, house, houseboat, hut, industrial, kindergarten, kiosk, mosque, office, parking, pavilion, public, residential, retail, riding_hall, roof, ruins, school, service, shed, shrine, stable, stadium, static_caravan, sty, synagogue, temple, terrace, train_station, transformer_tower, transportation, university, warehouse, water_tower'  
- `collapseRisk`: Probability of total collapse of the building.  
- `containedInPlace`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `floorsAboveGround`: Floors above the ground level  
- `floorsBelowGround`: Floors below the ground level  
- `id`: Unique identifier of the entity  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `occupier`: Person or entity using the building  
- `openingHours`: Opening hours of this building.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `peopleCapacity`: Allowed people present at the building  
- `peopleOccupancy`: People present at the building  
- `refMap`: Reference to the map containing the building  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: NGSI Entity type  


Required properties  
- `address`  
- `category`  
- `id`  
- `type`  
