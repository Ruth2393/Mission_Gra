import os
import json
import uuid
import datetime
import networkx as nx
import graphviz
from shapely.geometry import Point
from shapely.geometry import LineString
from shapely.geometry import Polygon
import shapely


time = datetime.datetime.now()

now = datetime.datetime.now()
new_time = now + datetime.timedelta(minutes=5)
new_time_g = new_time + datetime.timedelta(minutes=16)
new_time_t = new_time_g + datetime.timedelta(minutes=35)
new_time_wa=new_time_t + datetime.timedelta(minutes=16)
new_time_s = new_time_wa + datetime.timedelta(minutes=10)

def openMissionTemplate(taskTemplate,list_op,EntityAgriFarm,dicc,full_path_locations,EntityAgriRobot_id,rountrip=False,EntityFinal_name=[]):
    template = taskTemplate.copy()

    template["id"] = "urn:ngsi-ld:" + "Task" + ":" + str(uuid.uuid4())
    new_time_m = new_time_s +  datetime.timedelta(minutes=85)
    template['plannedBeginTime'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    template['plannedEndTime'] = new_time_m.strftime("%Y-%m-%dT%H:%M:%SZ")
    template["taskType"] = "Mission"
    template["hasWorkingArea"] = EntityAgriFarm["id"]
    template["workingAreaType"] = "AgriFarm"
    template["plannedLocation"]["type"]="LineString"
    template["plannedLocation"]["coordinates"] = full_path_locations
    template["hasPlannedTaskChildren"] = list_op
    template["hasExecutedTaskChildren"] = []
    template["actualLocation"]["type"]="LineString"
    template["actualLocation"]["coordinates"] = []
    template["status"] = "planned"
    template["result"] = []
    template["hasAgriRobot"] = EntityAgriRobot_id["id"]
    template["name"] = "Mission weeding with HPL in " + dicc["name"] + " @ " + EntityAgriFarm["name"] + " "+ (time.strftime("%Y-%m-%dT%H:%M:%SZ"))
    goal = "Automatically weeding in " + dicc["name"] + " @ " + EntityAgriFarm["name"]
    if rountrip == True:
        goal = goal + " and roundtrip back to " + EntityFinal_name
    template["goal"] = goal

    return template

def openActionTemplate(taskTemplate,dicc,direction,EntityAgriFarm,actionType="FollowPath"): #FOLLOWPATH
    template = taskTemplate.copy()
    template["id"] = "urn:ngsi-ld:" + "Task:" + str(uuid.uuid4())
    template['plannedBeginTime'] = []
    template['plannedEndTime'] = []
    template["taskType"] = "Action"
    template["name"]  = "Action " + actionType + " in "+ dicc["name"]+ " @ " + EntityAgriFarm["name"]
    template["goal"] = actionType + " in "+ dicc["name"]+ " @ " + EntityAgriFarm["name"]
    template["hasWorkingArea"] = dicc["id"]
    template["workingAreaType"] = dicc["name"]
    if direction == "b":
        coord = list(reversed(dicc["location"]["coordinates"]))
        template["name"]  = "Action " + actionType +" Return" " in "+ dicc["name"]+ " @ " + EntityAgriFarm["name"]
        template["goal"]  = actionType +" Return" " in "+ dicc["name"]+ " @ " + EntityAgriFarm["name"]
        template["actualLocation"]["type"] = "LineString"
        template["actualLocation"]["coordinates"]= []

    else:
        coord = dicc["location"]["coordinates"]
    template["plannedLocation"]["type"] = "LineString"
    template["plannedLocation"]["coordinates"]= coord
    template["actualLocation"]["type"] = "LineString"
    template["actualLocation"]["coordinates"]= []

    template ["hasPlannedTaskChildren"] = []
    template ["hasExecutedTaskChildren"] = []
    template["actualLocation"]["coordinates"]= []
    template ["status"] = "planned"
    template ["result"] = []

    return template

def openAction_1Template(taskTemplate,dicc,direction,EntityAgriFarm,actionType='MoveTo'):  #MOVETO
    template = taskTemplate.copy()
    template["id"] = "urn:ngsi-ld:" + "Task:" + str(uuid.uuid4())
    template['plannedBeginTime'] = []
    template['plannedEndTime'] = []
    template["taskType"] = "Action"
    template["name"]  = "Action " + actionType + " in "+ dicc["name"]+ " @ " + EntityAgriFarm["name"]
    template ["goal"] = actionType + " in "+ dicc["name"]+ " @ " + EntityAgriFarm["name"]
    template["hasWorkingArea"] = dicc["id"]
    template["workingAreaType"] = dicc["type"]
    if direction == "b":
        coord = list(reversed(dicc["location"]["coordinates"]))
        template["name"]  = "Action " + actionType +" Return" " in "+ dicc["name"]+ " @ " + EntityAgriFarm["name"]
        template["goal"]  = actionType +" Return" " in "+ dicc["name"]+ " @ " + EntityAgriFarm["name"]
        template["actualLocation"]["type"] = "Point"
        template["actualLocation"]["coordinates"]= []

    else:
        coord = dicc["location"]["coordinates"]

    if dicc["type"]=="RoadSegment":
        template["plannedLocation"]["type"] = "Point"
        template["plannedLocation"]["coordinates"] = coord[0]
    else:
        if dicc["type"]=="Building":
            p=Polygon(coord[0])
            coord=p.centroid
            template["plannedLocation"]["type"] = "Point"
            template["plannedLocation"]["coordinates"] = list(coord.coords)[0]

    if dicc["type"]== "gate":
        template["plannedLocation"]["type"] = "Point"
        template["plannedLocation"]["coordinates"]= coord[0]


    if dicc["type"]== "AgriParcel":
        template["plannedLocation"]["type"] = "Point"
        template["plannedLocation"]["coordinates"]= []


    template ["hasPlannedTaskChildren"] = []
    template ["hasExecutedTaskChildren"] = []
    template["actualLocation"]["type"] = "Point"
    template ["actualLocation"]["coordinates"] = []
    template ["status"] = "planned"
    template ["result"] = []

    return template



def openWakeupTemplate(taskTemplate,id_build,id_build_descrip,location_building,EntityAgriFarm):
    template = taskTemplate.copy()

    template["id"] = "urn:ngsi-ld:" + "Task" + ":" + str(uuid.uuid4())
    template['plannedBeginTime'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    template['plannedEndTime'] = new_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    template["taskType"] = "Operation"
    template["name"]  = "Operation Wakeup in "  + id_build_descrip + " @ " + EntityAgriFarm["name"]
    template ["goal"] = "Wakeup in "  + id_build_descrip + " @ " + EntityAgriFarm["name"]
    template["plannedSpeed"] = []
    template["hasWorkingArea"] = id_build
    template["workingAreaType"] = id_build_descrip
    template["plannedLocation"]["coordinates"]= location_building
    template ["hasPlannedTaskChildren"] = []
    template ["hasExecutedTaskChildren"] = []
    template ["actualLocation"]["coordinates"] = []
    template ["status"] = "planned"
    template ["result"] = []

    return template


def openTreatmentTemplate(taskTemplate,dicc,EntityAgriFarm):
    template = taskTemplate.copy()
    template["id"] = "urn:ngsi-ld:" + "Task" + ":" + str(uuid.uuid4())

    template['plannedBeginTime'] = new_time_g.strftime("%Y-%m-%dT%H:%M:%SZ")
    template['plannedEndTime'] = new_time_t.strftime("%Y-%m-%dT%H:%M:%SZ")
    template["taskType"] = "Operation"
    template["name"]  = "Operation Treatment in " + dicc["name"] + " @ " + EntityAgriFarm["name"]
    template ["goal"] = "Treatment in " + dicc["name"] + " @ " + EntityAgriFarm["name"]
    template["hasWorkingArea"] = dicc["id"]
    template["workingAreaType"] = dicc["description"]
    template["plannedLocation"]["coordinates"]= []
    template ["hasPlannedTaskChildren"] = []
    template ["hasExecutedTaskChildren"] = []
    template ["actualLocation"]["coordinates"] = []
    template ["status"] = "planned"
    template ["result"] = []

    return template

def openShutdownTemplate(taskTemplate,id_build,id_build_descrip,location_building,EntityAgriFarm):
    template = taskTemplate.copy()
    template["id"] = "urn:ngsi-ld:" + "Task" + ":" + str(uuid.uuid4())
    template['plannedBeginTime'] = new_time_wa.strftime("%Y-%m-%dT%H:%M:%SZ")
    template['plannedEndTime'] = new_time_s.strftime("%Y-%m-%dT%H:%M:%SZ")
    template["taskType"] = "Operation"
    template["name"]  = "Operation Shutdown in "  + id_build_descrip + " @ " + EntityAgriFarm["name"]
    template ["goal"] = "Shutdown in " + id_build_descrip + " @ " + EntityAgriFarm["name"]
    template["hasWorkingArea"] = id_build
    template["workingAreaType"] = id_build_descrip
    template["plannedLocation"]["coordinates"]= location_building
    template ["hasPlannedTaskChildren"] = []
    template ["hasExecutedTaskChildren"] = []
    template ["actualLocation"]["coordinates"] = []
    template ["status"] = "planned"
    template ["result"] = []

    return template


def openGoto_FieldTemplate(taskTemplate,list_action,location_building,dicc,EntityAgriFarm):
    template = taskTemplate.copy()
    template["id"] = "urn:ngsi-ld:" + "Task" + ":" + str(uuid.uuid4())
    template['plannedBeginTime'] = new_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    template['plannedEndTime'] = new_time_g.strftime("%Y-%m-%dT%H:%M:%SZ")
    template["taskType"] = "Operation"
    template["name"]  = "Operation GoToField in " + dicc["name"] + " @ " + EntityAgriFarm["name"]
    template["goal"]  = "GoToFIeld in " + dicc["name"] + " @ " + EntityAgriFarm["name"]
    template["hasWorkingArea"] = EntityAgriFarm["id"]
    template["workingAreaType"] = EntityAgriFarm["type"]
    template["plannedLocation"]["coordinates"]= location_building
    template ["hasPlannedTaskChildren"] = list_action
    template ["hasExecutedTaskChildren"] = []
    template ["actualLocation"]["type"] = "Point"
    template ["actualLocation"]["coordinates"] = []
    template ["status"] = "planned"
    template ["result"] = []

    return template

def openGoto_WarehouseTemplate(taskTemplate,list_action,id_build,id_build_descrip,location_building,EntityAgriFarm):
    template = taskTemplate.copy()
    template["id"] = "urn:ngsi-ld:" + "Task" + ":" + str(uuid.uuid4())
    template['plannedBeginTime'] = new_time_t.strftime("%Y-%m-%dT%H:%M:%SZ")
    template['plannedEndTime'] = new_time_wa.strftime("%Y-%m-%dT%H:%M:%SZ")
    template["taskType"] = "Operation"
    template["name"]  = "Operation GoToWareHouse in "  + id_build_descrip+ " @ " + EntityAgriFarm["name"]
    template["goal"]  = "GoToWareHouse in "  + id_build_descrip+ " @ " + EntityAgriFarm["name"]
    template["hasWorkingArea"] = id_build
    template["workingAreaType"] = id_build_descrip
    template["plannedLocation"]["coordinates"] = location_building
    template ["hasPlannedTaskChildren"] = list_action
    template ["hasExecutedTaskChildren"] = []
    template ["actualLocation"]["coordinates"] = []
    template ["status"] = "planned"
    template ["result"] = []

    return template
