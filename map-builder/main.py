# -*-encoding:utf-8-*-

import json
import os.path

from include.checkFiles import CheckFiles
from include.extractProperties import Extract
from include.fillTemplates import openParcelTemplate, openFarmTemplate, openBuildTemplate, openRoad_Template, openRestrictedTemplate,openSoilTemplate, openCropTemplate


if __name__ == '__main__':

    geomap, parcelTemplate, farmTemplate, buildingTemplate, roadTemplate, restrictedTemplate, soilTemplate, cropTemplate = CheckFiles()

    extraction = Extract(geomap)

    print('Number of entities: ' + str(len(extraction)))

    AgriFarmEntity = []
    AgriParcelEntity = [{},{},{},{},{},{},{},{},{}]
    ParcelType = []
    Parcel_id = []
    Farm_id = []
    BearingEntity=[]
    AgriSoilEntity=[]

    BuildingEntity = []
    BuildType = []
    Build_id = []

    RoadEntity = []
    GateEntity = []

    RestrictedEntity = []
    RestricType = []
    Restric_id = []
    Road_id=[]

    SoilEntity = []
    Soil_id = []

    CropEntity = []
    Crop_id = []
    Crop_category = []
    soil_id_p=[]



    # add Bearing in a new List to make match in AgriParcel template
    for entity in extraction:
        if "Bearing" in entity['type']:
            BearingEntity.append(entity)


    for entity in extraction:
        if "Gate" in entity['type']:
            GateEntity.append(entity)




    # addEntities
    i=0
    r=0
    j=0
    for entity in extraction:
        thisdir = os.path.join(os.getcwd()+ "/filledTemplates")


        if 'AgriFarm' in entity['type']:
            FarmEntity = openFarmTemplate(entity, farmTemplate)
            AgriFarmEntity.append(FarmEntity)


        if 'Building' in entity['type']:
            Building_Entity = openBuildTemplate(entity, buildingTemplate)
            BuildingEntity.append(Building_Entity)
            Build_id.append(Building_Entity["id"])
            i=i+1
            file_name = os.path.join(thisdir, "Building"+str(i)+ '.json')
            with open(file_name, 'w+') as f:
                json.dump(Building_Entity, f, indent=2, separators=(',', ':'))


        if 'Restricted' in entity['type']:
            Restricted_Entity = openRestrictedTemplate(entity, restrictedTemplate)
            RestrictedEntity.append(Restricted_Entity)
            Restric_id.append(Restricted_Entity["id"])
            r=r+1
            file_name = os.path.join(thisdir, "Restricted"+ str(r) + '.json')
            with open(file_name, 'w+') as f:
                json.dump(Restricted_Entity, f, indent=2, separators=(',', ':'))

        if 'Road' in entity['type']:
            Road_Entity = openRoad_Template(entity, roadTemplate)
            RoadEntity.append(Road_Entity)
            Road_id.append(Road_Entity["id"])
            j=j+1
            file_name = os.path.join(thisdir, "Road"+ str(j)+ '.json')
            with open(file_name, 'w+') as f:
                json.dump(Road_Entity, f, indent=2, separators=(',', ':'))


    Soil_Entity = openSoilTemplate(soilTemplate)
    SoilEntity.append(Soil_Entity)
    Soil_id.append(Soil_Entity["id"])
    print(Soil_id)

    soil=Soil_id
    print("holaaa")
    print(soil)

    file_name = os.path.join(thisdir, "AgriSoil.json")
    with open(file_name, 'w+') as f:
        json.dump(Soil_Entity, f, indent=2, separators=(',', ':'))

        if 'AgriParcel' in entity['type']:
            ParcelEntity, variety, index = openParcelTemplate(entity, parcelTemplate,BearingEntity,GateEntity,soil)
            AgriParcelEntity[index[0]-1] = [ParcelEntity]
            ParcelType.append(variety)
            Parcel_id.append(ParcelEntity["id"])
            ParcelEntity["hasAgriSoil"]=soil
            print("qqqqq")
            print(ParcelEntity["hasAgriSoil"])

            file_name = os.path.join(thisdir, "AgriParcel"+ str(index[0]) + '.json')
            with open(file_name, 'w+') as f:
                json.dump(ParcelEntity, f, indent=2, separators=(',', ':'))







Crop_Entity = openCropTemplate(cropTemplate)
CropEntity.append(Crop_Entity)
Crop_id.append(Crop_Entity["id"])
file_name = os.path.join(thisdir, "AgriCrop.json")
with open(file_name, 'w+') as f:
    json.dump(Crop_Entity, f, indent=2, separators=(',', ':'))



    hasAgriParcel = []

    thisdir = os.path.join(os.getcwd(), 'filledTemplates')

    if len(AgriFarmEntity) == 1:
        AgriFarm = AgriFarmEntity[0]
        AgriFarm["hasAgriParcel"] = Parcel_id
        AgriFarm["hasBuilding"]=Build_id
        AgriFarm["hasRestrictedTrafficArea"]=Restric_id
        AgriFarm["hasRoadSegment"]=Road_id
        file_name = os.path.join(thisdir, 'AgriFarm.json')
        with open(file_name, 'w+') as f:
            json.dump(AgriFarm, f, indent=2, separators=(',', ':'))
    else:
        # Not implemented if more than one farm
        for entity, indx in zip(AgriFarmEntity, range(len(AgriFarmEntity))):
            file_name = os.path.join(thisdir, entity["type"] + str(indx) + '.json')
            with open(file_name, 'w+') as f:
                json.dump(entity, f, indent=2, separators=(',', ':'))
