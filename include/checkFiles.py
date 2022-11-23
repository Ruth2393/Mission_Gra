# -*-encoding:utf-8-*-

from .loadFiles import LoadTemplates, LoadMap

def CheckFiles():  # This function checks and loads the different files necessary for program operation.

    map = LoadMap()
    parcelTemplate, farmTemplate, buildingTemplate, roadTemplate, restrictedTemplate, soilTemplate, cropTemplate = LoadTemplates()

    return map, parcelTemplate, farmTemplate, buildingTemplate, roadTemplate, restrictedTemplate, soilTemplate, cropTemplate
