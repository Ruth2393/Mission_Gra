# -*-encoding:utf-8-*-

import os
import os.path
import json
import sys


def LoadMap():  # This function displays the available maps and asks the user which one to select.

    map = []
    mainPath = os.path.dirname(os.path.abspath(__file__)).split('include')[0]
    thisdir = os.path.join(os.getcwd()+"/Maps")
    content = os.listdir(thisdir)

    print("Los mapas disponibles son los siguientes: ")
    for file in content:
        if file.endswith(".geojson"):
            print(os.path.join(file))
    cont = 0
    while True:
        cont += 1
        if cont == 3:
            break
        map_name = input("Introduzca el nombre del mapa que desea abrir: ")

        try:
            with open(os.path.join(thisdir,map_name)) as mapfile:
                map = json.load(mapfile)
            break
        except:
            print("Archivo no encontrado. Intentelo de nuevo:")

    return map


def LoadTemplates():    # This function searches for the templates corresponding to AgriFarm and AgriParcel and loads them.

    thi=os.getcwd()
    dir_prin= os.path.join(os.getcwd()+"/welaser-datamodels-update")
    if os.path.isdir(dir_prin):
        print("Exists folder")

        with open(os.path.join((dir_prin+"/AgriParcel/template"),"AgriParcel_Template.json")) as parcelFile:
            parcelTemplate = json.load(parcelFile)

        with open(os.path.join((dir_prin+"/AgriFarm/template"),"AgriFarm_Template.json")) as farmFile:
            farmTemplate = json.load(farmFile)

        with open(os.path.join((dir_prin+"/Building/template"),"Building_Template.json")) as buildingFile:
            buildingTemplate = json.load(buildingFile)

        with open(os.path.join((dir_prin+"/RoadSegment/template"),"RoadSegment_Template.json")) as roadFile:
            roadTemplate = json.load(roadFile)

        with open(os.path.join((dir_prin+"/RestrictedTrafficArea/template"),"RestrictedTrafficArea_Template.json")) as restrictedFile:
            restrictedTemplate = json.load(restrictedFile)


        with open(os.path.join((dir_prin+"/AgriSoil/template"),"AgriSoil_Template.json")) as soilFile:
            soilTemplate = json.load(soilFile)


        with open(os.path.join((dir_prin+"/AgriCrop/template"),"AgriCrop_Template.json")) as cropFile:
            cropTemplate = json.load(cropFile)

        return parcelTemplate, farmTemplate, buildingTemplate, roadTemplate, restrictedTemplate, soilTemplate, cropTemplate
        return True
    else:
        print("There is no folder")
        assert(False)
