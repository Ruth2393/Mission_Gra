Entity: RoadSegment  
===================


Global description: **This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road.**  

version: 0.4.1  

This is taken from: https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadSegment/doc/spec.md

## List of properties  


- `address`: The mailing address  
- `agency_name`: The agency_name field contains the full name of the agency or organisation responsible for maintenance of the entity under consideration. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  
- `allowedVehicleType`: Vehicle type(s) allowed to transit through this road segment. Enum:'agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle'. Allowed values: The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/):  
- `alternateName`: An alternative name for this item  
- `annotations`: Annotations about the item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `bridgeCount`: Number of bridges in the road segment corresponding to this observation. Takes 0 (zero) as the value when the road segment has no bridges.  
- `carriagewayLength`: Total length of the carriage way of the road segment corresponding to this observation.  
- `carriagewayWidth`: Total width of the carriage way of the road segment corresponding to this observation.  
- `category`: Allows to convey extra characteristics of a road segment. Enum:'oneway, toll, link'.  `oneway`: Flags whether the road segment can only be used in one direction. If not present it means road segment can be used in both directions (forwards and backwards). See also [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Flags whether the road segment is under toll fees. `link` : Flags whether this road segment is an auxiliary link segment for exiting or entering a road. See [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Any other value meaningful to an application.  
- `color`: The color of the product  
- `culvertCount`: Number of culverts prevalent in the trace of the road corresponding to this observation.  
- `cyclePathLeftHeight`: Height of the cycle track on the left edge of the road corresponding to this observation.  
- `cyclePathLeftWidth`: Width of the cycle track on the left edge of the road corresponding to this observation.  
- `cyclePathMaterial`: Construction material used for laying the cycle path on the sides of the road corresponding to this observation.  
- `cyclePathPlacement`: Describes the placement of cycle track along the road segment corresponding to this observation. Enum:' ['RIGHT, LEFT, BOTH, NOT_AVAILABLE'  
- `cyclePathRightHeight`: Height of the cycle track on the right edge of the road corresponding to this observation.  
- `cyclePathRightWidth`: Width of the cycle track on the right edge of the road corresponding to this observation.  
- `dataDescriptor`: URI pointing to the data-descriptor entity  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `endKilometer`: The kilometer number (measured from the road's start point) where this road segment ends.   
- `endPoint`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `id`: Unique identifier of the entity  
- `image`: An image of the item  
- `laneInfo`: Describes the aspects of lanes of the road corresponding to this observation.  
- `laneUsage`: This attribute can be used to convey specific parameters describing each lane. It must contain a string per road segment lane. The element 0 of the array must contain the information of lane 1, and so on. Format of the referred string must be: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> is a text string with the following allowed values: `forward`. The lane is currently used in the `forwards` direction. `backward`. The lane is currently used in the `backwards` direction. The only mandatory parameter is `lane_direction`. If not specified, the rest of parameters can be assumed to be equal to those specified at entity level.  
- `length`: Total length of this road segment in kilometers  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `maximumAllowedHeight`: Maximum allowed height for vehicles transiting this road segment  
- `maximumAllowedSpeed`: Maximum allowed speed plying the road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)  
- `maximumAllowedWeight`: Maximum allowed weight for vehicles transiting this road segment  
- `maximumAllowedWidth`: Maximum allowed width for vehicles using the entity corresponding to this observation.  
- `medianHeight`: Height of the median or central reservation in the road corresponding to this observation.  
- `medianLength`: Length of the median or central reservation in the road corresponding to this observation.  
- `medianWidth`: Width of the median or central reservation in the road corresponding to this observation.  
- `minimumAllowedSpeed`: Minimum allowed speed while transiting this road segment  
- `municipalityInfo`: Municipality information corresponding to this observation.  
- `name`: The name of this item.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `pedestrianPathLeftHeight`: Height of the walkway placed on the left edge of the road corresponding to this observation.  
- `pedestrianPathLeftWidth`: Width of the walkway placed on the left edge of the road corresponding to this observation.  
- `pedestrianPathMaterial`: Construction material used for laying the walkway / footpath on the sides of the road corresponding to this observation.  
- `pedestrianPathPlacement`: Describes the presence and placement of pedestrian along the road segment corresponding to this observation. Enum:'RIGHT, LEFT, BOTH, NOT_AVAILABLE'  
- `pedestrianPathRightHeight`: Height of the walkway placed on the right edge of the road corresponding to this observation.  
- `pedestrianPathRightWidth`: Width of the walkway placed on the right edge of the road corresponding to this observation.  
- `refRoad`: Road to which this road segment belongs to.  
- `rightOfWayWidth`: Right of Way (RoW) is the total land area available for the roadway. Its width accommodates for carriages way + other necessities + future extension, along the road's alignment.  
- `roadClass`: The type of road corresponding to this observation. Enum: [OTHER_PUBLIC_ROAD, PRIVATE_ROAD, MINOR_CITY_ROAD, MAJOR_DISTRICT_ROAD, MAJOR_CITY_ROAD, NATIONAL_HIGHWAY, SERVICE_ROAD, STATE_HIGHWAY, OTHER_DISTRICT_ROAD, PORT_ROAD].  
- `roadDirection`: Represents the direction the road is heading to. Enum:' ['N, S, E, W'. The values N,S,E,W represent North,South,East,West respectively.  
- `roadId`: Unique internal representation of the road corresponding to this observation.  
- `roadMaterial`: The construction material used for laying the carriageway corresponding to this observation. For eg. concrete, earthen, tar etc.  
- `roadName`: The name of the road corresponding to this observation.  
- `roadWork`: Reasons for the road work in case of urgent intervention. A combination of these values. Enum:'COLLAPSE, DERAILMENT, FIRE, FLOOD, GASLEAK, LANDSLIDE, OTHER, POWERCUT, ROCKFALL, SAGGING, WATERLEAK'.  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `startKilometer`: The kilometer number (measured from the road's start point) where this road segment starts.   
- `startPoint`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `status`: Specific driving conditions on the roadsegment. Use statusDescription for additional information. Enum: ‘open, closed, limited’.  `open`: the roadsegment can be used in full intended capacity, `closed`: no traffic is possible, e.g. due to roadworks, an open bridge or lock, or any other event preventing traffic. `limited`: traffic is possible, but not in the full capacity.  
- `statusDescription`: Additional information to the status attribute.  
- `totalCyclePathWidth`: Total width of the cycle track present in the road corresponding to this observation.  
- `totalLaneNumber`: Total number of lanes offered by this road segment  
- `totalPedestrianPathLength`: Total length of the walkway present in the road corresponding to this observation.  
- `totalPedestrianPathWidth`: Total width of the walkway present in the road corresponding to this observation.  
- `type`: NGSI Entity type. It has to be RoadSegment  
- `width`: Road's segment width.  


Required properties  
- `allowedVehicleType`  
- `endPoint`  
- `id`  
- `name`  
- `refRoad`  
- `startPoint`  
- `type`  


Road segments can include several lanes. This data model allows to convey road segments made up of heterogeneous lanes (different in their usage, speed, height, etc.). Lanes are identified by using integer numbers between 1 and n, being number 1 the lane to the right when going forwards. The forward direction is the direction denoted by the vector which goes from the segment"s start point to the segment"s end point. This is the same convention as the one used by OpenStreetMap. This entity is primarily associated with the Automotive and Smart City vertical segments and related IoT applications. This data model has been developed in cooperation with mobile operators and the GSMA.  
