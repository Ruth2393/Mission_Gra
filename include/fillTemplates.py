# -*-encoding:utf-8-*-

import uuid
import datetime
import pycountry
#print(pycountry.__version__)

from shapely.geometry import Polygon
from geopy.geocoders import Nominatim

from .coorProperties import StandardCoordinates, Polygon_utm
from .bearing_calc import calculateBearing
from .road_length import distance
from .gate import match_gates

def setHeader(template, type_):  #This function creates the header of the generated files.
    temp = template.copy()
    temp["id"] = "urn:ngsi-ld:" + type_ + ":" + str(uuid.uuid4())
    now = datetime.datetime.now()
    temp['dateCreated'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    temp['dateModified'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    return temp


def openFarmTemplate(entity, farmTemplate): #This function fills the AgriFarm template with the required data.
    template = farmTemplate.copy()
    template = setHeader(template, "AgriFarm")

    template["description"] = entity["description"]
    template["name"]="Farm WeLASER Arganda del Rey"
    template["relatedSource"][0]["application"] = ""
    template["relatedSource"][0]["applicationEntityId"] = ""
    template["seeAlso"] = []
    template["location"]["type"] = "Point"
    location = entity["geometry"]["coordinates"][0][0]
    template["location"]["coordinates"] = [location[1], location[0]]
    template["landLocation"]["type"] = entity["geometry"]["type"]
    coordinates = entity["geometry"]["coordinates"][0]
    inversion = StandardCoordinates(coordinates)
    template["landLocation"]["coordinates"] = [inversion]
    geolocator = Nominatim(user_agent="AgriFarm address")
    location = geolocator.reverse(str(location[1]) + ", " + str(location[0]), language="en-GB")
    template["address"]["addressLocality"] = location.address.split(',')[2:4]
    country = location.address.split(',')[-1]
    initial = pycountry.countries.search_fuzzy(country)
    template["address"]["addressCountry"] = initial[0].alpha_2
    template["address"]["streetAddress"] = location.address.split(',')[0:2]
    template["contactPoint"]["email"] = input("Introduzca su email: ")
    #template["contactPoint"]["telephone"] = input("Introduzca su teléfono: ")
    template["ownedBy"] = ""
    template["hasBuilding"] = []
    hasAgriParcel = []
    template["hasAgriParcel"] = []  #Se rellena en el main
    template["hasRestrictedTrafficArea"] = []
    template["hasRoadSegment"] = []


    return template


def getType(name):   #This function filter types to interconnect the templates.
    variety = "Parcel"
    indicator = name.split(" ")[-1]

    if "Children" in name:
        variety = "Children"
        m_index = int(indicator.split(".")[0])
        s_index = int(indicator.split(".")[-1])
    else:
        m_index = int(indicator)
        s_index = 0

    index = [m_index, s_index]

    return variety, index


def openParcelTemplate(entity, parcelTemplate, bearings, gates,soil): #This function fills the AgriParcel template with the required data.

    template = parcelTemplate.copy()
    template["id"] = "urn:ngsi-ld:" + "AgriParcel" + ":" + str(uuid.uuid4())
    now = datetime.datetime.now()
    template['dateCreated'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    template['dateModified'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    variety, index = getType(entity["type"])
    coord_ang=calculateBearing(index[0],bearings)
    template["location"]["type"] = entity["geometry"]["type"]
    geometry = entity["geometry"]
    location = entity["geometry"]["coordinates"][0]
    template["location"]["coordinates"] = entity["geometry"]["coordinates"]
    coordinates = geometry["coordinates"][0]
    utm_coord = Polygon_utm(coordinates)
    inversion = StandardCoordinates(coordinates)
    template['location']['coordinates'] = [inversion]
    template["area"] = round(Polygon(utm_coord).area, 2)
    template["description"] = entity["type"]
    template["name"] = "Field" + " "+ entity["type"][-1] + " "+ entity["category"]
    template["category"] = entity["category"]
    template["relatedSource"][0]["application"] = ""
    template["relatedSource"][0]["applicationEntityId"] = ""
    template["seeAlso"] = []
    template["belongsTo"] = template["id"]
    template["ownedBy"] = ""
    template["hasAgriSoil"] = soil["id"]
    template["hasAgriCrop"] = []
    template["cropStatus"] = ""
    template["lastPlantedAt"] = ""
    template["hasDevice"] = []
    template["bearing"] = int(coord_ang)
    template["headlandWidth"] = entity["headland"]
    puertas= match_gates(index[0],gates)
    template["gateLocation"]["coordinates"] = StandardCoordinates(puertas)
    return template, variety, index


def openBuildTemplate(entity, buildingTemplate): #This function fills the AgriFarm template with the required data.

    template = buildingTemplate.copy()
    template = setHeader(template, "Building")

    template["category"] = "office"
    template["location"]["type"] = entity["geometry"]["type"]
    geometry = entity["geometry"]
    location = entity["geometry"]["coordinates"][0][0]
    template["location"]["coordinates"] = entity["geometry"]["coordinates"]
    coordinates = geometry["coordinates"][0]
    utm_coord = Polygon_utm(coordinates)
    inversion = StandardCoordinates(coordinates)
    template['location']['coordinates'] = [inversion]
    geolocator = Nominatim(user_agent="Building address")
    location = geolocator.reverse(str(location[1]) + ", " + str(location[0]), language="en-GB")
    template["address"]["addressLocality"] = location.address.split(',')[2:4]
    country = location.address.split(',')[-1]
    initial = pycountry.countries.search_fuzzy(country)
    #template["address"]["postalCode"] = []
    template["address"]["streetAddress"] = location.address.split(',')[0:2]
    template["ownedBy"] = ""
    template["description"] = entity["type"]
    template["name"]=entity["type"]
    template["ownedBy"] = ""

    return template


def openRoad_Template(entity, roadTemplate): #This function fills the AgriFarm template with the required data.

    template = roadTemplate.copy()
    template = setHeader(template, "RoadSegment")


    coordinates = entity["geometry"]["coordinates"]
    inversion = StandardCoordinates(coordinates)
    template['location']['coordinates'] = inversion

    template["startPoint"]["coordinates"] = inversion[0]
    template["endPoint"]["coordinates"] = inversion[-1]

    template["length"]=distance(entity["geometry"]["coordinates"])
    template ["roadMaterial"]= (entity["material"])
    template["name"] = entity["type"]

    return template

def openRestrictedTemplate(entity, restrictedTemplate):

    template = restrictedTemplate.copy()
    template = setHeader(template, "RestrictedTrafficArea")
    template["category"] = "onlyPedestrian"
    template["location"]["type"] = "Point"
    template["name"]=entity["category"]
    template["description"] = "Restricted Area"
    location = entity["geometry"]["coordinates"][0][0]
    template["location"]["coordinates"] = [location[1], location[0]]
    template["landLocation"]["type"] = entity["geometry"]["type"]
    coordinates = entity["geometry"]["coordinates"][0]
    inversion = StandardCoordinates(coordinates)
    template["landLocation"]["coordinates"] = [inversion]
    geolocator = Nominatim(user_agent="Restricted address")
    location = geolocator.reverse(str(location[1]) + ", " + str(location[0]), language="en-GB")

    return template



def openSoilTemplate(soilTemplate):

    template = soilTemplate.copy()
    template = setHeader(template, "AgriSoil")
    template["name"]="Loam(Limosos)"
    template["description"]="Fine grained, poor draining soil. Particle size between 0.002 and 0.05 mm. They have intermediate properties between sandy soils and clay soils."
    template["relatedSource"]=[]
    template["hasAgriProductType"]=[]
    template["agroVocConcept"]=[]
    template["seeAlso"]=[]

    return template


def openCropTemplate(cropTemplate):

    template = cropTemplate.copy()
    template = setHeader(template, "AgriCrop")
    lista=["Corn, Wheat, Beetroot"]
    template["name"]=""
    template["alternateName"]=""
    template["agroVocConcept"]=[]
    template["seeAlso"]=[]
    template["description"]=""
    template["relatedSource"]=[]
    template["hasAgriSoil"]=[]
    template["hasAgriFertiliser"]=[]
    template["hasAgriPest"]=[]
    template["plantingFrom"]=[]
    template["harvestingInterval"]=[]
    template["wateringFrequency"]=""



    return template
