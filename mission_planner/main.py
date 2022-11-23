# -*-encoding:utf-8-*-

import json
import os.path
import datetime

from include.setFile import LoadTemplates
from include.taskte import openMissionTemplate, openActionTemplate, openGoto_FieldTemplate, openWakeupTemplate, openShutdownTemplate,openTreatmentTemplate, openGoto_WarehouseTemplate,openAction_1Template
from include.grafo_welaser_functions import trace_graph
from shapely.geometry import Point
import shapely
from shapely.geometry import Polygon



if __name__ == '__main__':

    MissionEntity = []
    OperationEntity = []
    OperationGoToEntity = []
    ActionFollowEntity = []
    ActionEntity = []

    list_plan=[]
    list_id_actions=[]
    list_inv_id_actions=[]
    list_id_op=[]


    #time = datetime.datetime.now()

    os.chdir('../')
    mainPath = os.path.dirname(os.path.abspath(__file__)).split('mission_planner')[0]
    filled_tasks = mainPath + "/mission_planner/filledTask"
    print(filled_tasks)

    dir_welaser_datamodels = mainPath + "/welaser-datamodels"
    print(dir_welaser_datamodels)

    taskTemplate = LoadTemplates(dir_welaser_datamodels)

    #------------------------------------------------------------------------------
    #OPEN AgriFarm.

    with open(dir_welaser_datamodels + "/AgriFarm/examples/AgriFarm.json") as f:
        EntityAgriFarm = json.load(f)

    #------------------------------------------------------------------------------


    #------------------------------------------------------------------------------
    #OPEN AgriRObot

    with open(dir_welaser_datamodels + "/AgriRobot/examples/carob-123.json") as f:
        EntityAgriRobot_id = json.load(f)

    #------------------------------------------------------------------------------


    dicc_plan=trace_graph("Building1.json","AgriParcel3.json")

    id_build=dicc_plan["Building1.json"]["id"]
    id_build_location=dicc_plan["Building1.json"]["location"]["coordinates"]
    id_build_descrip=dicc_plan["Building1.json"]["description"]

    pc=Polygon(id_build_location[0])
    location_bu=pc.centroid


    location_building=list(location_bu.coords)[0]
    #dicc_build={"type":{"coordinates":location_building}}

    a=list(dicc_plan.keys())
    for i in range(len(a)):
        b=a[i].split(".")
        list_plan.append(b[0])

    if "OpenField" in a:
        a.remove("OpenField")

    if "OpenField" in list_plan:
        list_plan.remove("OpenField")


    print(list_plan)
    list_inv_plan=list(reversed(list_plan))
    print(list_inv_plan)

#------------------------------

    if "Building" in a:
        build_coord =dicc1[id_build]["location"]["coordinates"]
        centr= poligono.centroid

        idbuild_centroide[id_build]=centr

        print("Puntocentride")
        print(centr)

        diccB={"type":{"coordinates":centr}}
#-----------------------


#-----------------full_path_location------
    full_path_locations=[]
#-------------------------


##################################################   action1 -> MoveTo      Action - > FollowPath
    v="f"#  f ---> fordward     b-->backward
    for i in range(1,len(a)):

        print(dicc_plan[a[i]])
        if dicc_plan[a[i]]["type"] == "AgriParcel":
            parcela_p=dicc_plan[a[i]]["description"][-1]

        if i == 1:
            if dicc_plan[a[i]]["type"] == "RoadSegment":
                file_name = os.path.join(filled_tasks,"ActionMoveTo"+list_plan[i] +".json")
                Mission_E_1 = openAction_1Template(taskTemplate,dicc_plan[a[i]],v,EntityAgriFarm)
                list_id_actions.append(Mission_E_1["id"])
                full_path_locations.append(Mission_E_1["plannedLocation"]["coordinates"])
                with open(file_name, 'w+') as f:
                    json.dump(Mission_E_1, f, indent=2, separators=(',', ':'))

                file_name = os.path.join(filled_tasks,"ActionFollowPath"+list_plan[i] +".json")
                Mission_E = openActionTemplate(taskTemplate,dicc_plan[a[i]],v,EntityAgriFarm)
                list_id_actions.append(Mission_E["id"])
                for i in range(len(Mission_E["plannedLocation"]["coordinates"])):
                    full_path_locations.append(Mission_E["plannedLocation"]["coordinates"][i])
                with open(file_name, 'w+') as f:
                    json.dump(Mission_E, f, indent=2, separators=(',', ':'))

            else:
                file_name = os.path.join(filled_tasks,"ActionMoveTo"+list_plan[i] +".json")
                Mission_E_1 = openAction_1Template(taskTemplate,dicc_plan[a[i]],v,EntityAgriFarm)
                list_id_actions.append(Mission_E_1["id"])
                full_path_locations.append(Mission_E_1["plannedLocation"]["coordinates"])
                with open(file_name, 'w+') as f:
                    json.dump(Mission_E_1, f, indent=2, separators=(',', ':'))
        else:
            print(dicc_plan[a[i]])
            if (dicc_plan[a[i]]["type"] == "RoadSegment") and (dicc_plan[a[i-1]]["type"] != "RoadSegment"):
                file_name = os.path.join(filled_tasks,"ActionMoveTo"+list_plan[i] +".json")
                Mission_E_1 = openAction_1Template(taskTemplate,dicc_plan[a[i]],v,EntityAgriFarm)
                list_id_actions.append(Mission_E_1["id"])
                full_path_locations.append(Mission_E_1["plannedLocation"]["coordinates"])
                with open(file_name, 'w+') as f:
                    json.dump(Mission_E_1, f, indent=2, separators=(',', ':'))

                file_name = os.path.join(filled_tasks,"ActionFollowPath"+list_plan[i] +".json")
                Mission_E = openActionTemplate(taskTemplate,dicc_plan[a[i]],v,EntityAgriFarm)
                list_id_actions.append(Mission_E["id"])
                for i in range(len(Mission_E["plannedLocation"]["coordinates"])):
                    full_path_locations.append(Mission_E["plannedLocation"]["coordinates"][i])
                with open(file_name, 'w+') as f:
                    json.dump(Mission_E, f, indent=2, separators=(',', ':'))

            else:
                if (dicc_plan[a[i-1]]["type"] == "RoadSegment") and (dicc_plan[a[i]]["type"] == "RoadSegment"):
                    file_name = os.path.join(filled_tasks,"ActionFollowPath"+list_plan[i] +".json")
                    Mission_E = openActionTemplate(taskTemplate,dicc_plan[a[i]],v,EntityAgriFarm)
                    list_id_actions.append(Mission_E["id"])
                    for i in range(len(Mission_E["plannedLocation"]["coordinates"])):
                        full_path_locations.append(Mission_E["plannedLocation"]["coordinates"][i])
                    with open(file_name, 'w+') as f:
                        json.dump(Mission_E, f, indent=2, separators=(',', ':'))
                else:
                    file_name = os.path.join(filled_tasks,"ActionMoveTo"+list_plan[i] +".json")
                    Mission_E_1 = openAction_1Template(taskTemplate,dicc_plan[a[i]],v,EntityAgriFarm)
                    list_id_actions.append(Mission_E_1["id"])
                    full_path_locations.append(Mission_E_1["plannedLocation"]["coordinates"])
                    with open(file_name, 'w+') as f:
                        json.dump(Mission_E_1, f, indent=2, separators=(',', ':'))


    print(list_id_actions)

##################################################

    v="b"#  f ---> fordward     b-->backward

    inv_a = list(reversed(a))

    for i in range(1,len(inv_a)):

        print(dicc_plan[a[i]])


        if i == 1:
            if dicc_plan[inv_a[i]]["type"] == "RoadSegment":
                file_name = os.path.join(filled_tasks,"ActionMoveToReturn"+list_inv_plan[i] +".json")
                Mission_E_1 = openAction_1Template(taskTemplate,dicc_plan[inv_a[i]],v,EntityAgriFarm)
                list_inv_id_actions.append(Mission_E_1["id"])
                full_path_locations.append(Mission_E_1["plannedLocation"]["coordinates"])
                with open(file_name, 'w+') as f:
                    json.dump(Mission_E_1, f, indent=2, separators=(',', ':'))

                file_name = os.path.join(filled_tasks,"ActionFollowPathReturn"+list_inv_plan[i] +".json")
                Mission_E = openActionTemplate(taskTemplate,dicc_plan[inv_a[i]],v,EntityAgriFarm)
                list_inv_id_actions.append(Mission_E["id"])
                for i in range(len(Mission_E["plannedLocation"]["coordinates"])):
                    full_path_locations.append(Mission_E["plannedLocation"]["coordinates"][i])
                with open(file_name, 'w+') as f:
                    json.dump(Mission_E, f, indent=2, separators=(',', ':'))

            else:
                file_name = os.path.join(filled_tasks,"ActionMoveToReturn"+list_inv_plan[i] +".json")
                Mission_E_1 = openAction_1Template(taskTemplate,dicc_plan[inv_a[i]],v,EntityAgriFarm)
                list_inv_id_actions.append(Mission_E_1["id"])
                full_path_locations.append(Mission_E_1["plannedLocation"]["coordinates"])
                with open(file_name, 'w+') as f:
                    json.dump(Mission_E_1, f, indent=2, separators=(',', ':'))
        else:
            print(dicc_plan[a[i]])
            if (dicc_plan[inv_a[i]]["type"] == "RoadSegment") and (dicc_plan[inv_a[i-1]]["type"] != "RoadSegment"):
                file_name = os.path.join(filled_tasks,"ActionMoveToReturn"+list_inv_plan[i] +".json")
                Mission_E_1 = openAction_1Template(taskTemplate,dicc_plan[inv_a[i]],v,EntityAgriFarm)
                list_inv_id_actions.append(Mission_E_1["id"])
                full_path_locations.append(Mission_E_1["plannedLocation"]["coordinates"])
                with open(file_name, 'w+') as f:
                    json.dump(Mission_E_1, f, indent=2, separators=(',', ':'))

                file_name = os.path.join(filled_tasks,"ActionFollowPathReturn"+list_inv_plan[i] +".json")
                Mission_E = openActionTemplate(taskTemplate,dicc_plan[inv_a[i]],v,EntityAgriFarm)
                list_inv_id_actions.append(Mission_E["id"])
                for i in range(len(Mission_E["plannedLocation"]["coordinates"])):
                    full_path_locations.append(Mission_E["plannedLocation"]["coordinates"][i])
                with open(file_name, 'w+') as f:
                    json.dump(Mission_E, f, indent=2, separators=(',', ':'))

            else:
                if (dicc_plan[inv_a[i-1]]["type"] == "RoadSegment") and (dicc_plan[inv_a[i]]["type"] == "RoadSegment"):
                    file_name = os.path.join(filled_tasks,"ActionFollowPathReturn"+list_inv_plan[i] +".json")
                    Mission_E = openActionTemplate(taskTemplate,dicc_plan[inv_a[i]],v,EntityAgriFarm)
                    list_inv_id_actions.append(Mission_E["id"])
                    for i in range(len(Mission_E["plannedLocation"]["coordinates"])):
                        full_path_locations.append(Mission_E["plannedLocation"]["coordinates"][i])
                    #full_path_locations.append(Mission_E["plannedLocation"]["coordinates"])
                    with open(file_name, 'w+') as f:
                        json.dump(Mission_E, f, indent=2, separators=(',', ':'))
                else:
                    file_name = os.path.join(filled_tasks,"ActionMoveToReturn"+list_inv_plan[i] +".json")
                    Mission_E_1 = openAction_1Template(taskTemplate,dicc_plan[inv_a[i]],v,EntityAgriFarm)
                    list_inv_id_actions.append(Mission_E_1["id"])
                    full_path_locations.append(Mission_E_1["plannedLocation"]["coordinates"])
                    with open(file_name, 'w+') as f:
                        json.dump(Mission_E_1, f, indent=2, separators=(',', ':'))

    print(list_inv_id_actions)
    print(full_path_locations)
    full_path_locations.remove([])



    Operation_E = openWakeupTemplate(taskTemplate,id_build,id_build_descrip,location_building,EntityAgriFarm)
    OperationEntity.append(Operation_E)
    list_id_op.append(Operation_E["id"])
    file_name = os.path.join(filled_tasks,'OperationWakeup.json')
    #file_name = os.path.join(filled_tasks,'OperationWakeup.json'+" "+(time.strftime("%Y-%m-%dT%H:%M:%SZ")))
    with open(file_name, 'w+') as f:
        json.dump(Operation_E, f, indent=2, separators=(',', ':'))


    Operation_E = openGoto_FieldTemplate(taskTemplate,list_id_actions,location_building,dicc_plan[a[i]],EntityAgriFarm)
    OperationEntity.append(Operation_E)
    list_id_op.append(Operation_E["id"])
    #full_path_locations.append(Operation_E["plannedLocation"])
    file_name = os.path.join(filled_tasks, 'OperationGotoField'+ str(parcela_p) + '.json')
    with open(file_name, 'w+') as f:
        json.dump(Operation_E, f, indent=2, separators=(',', ':'))



    Operation_E = openTreatmentTemplate(taskTemplate,dicc_plan[a[i]],EntityAgriFarm)
    OperationEntity.append(Operation_E)
    list_id_op.append(Operation_E["id"])
    file_name = os.path.join(filled_tasks, 'OperationTreatment.json')
    with open(file_name, 'w+') as f:
        json.dump(Operation_E, f, indent=2, separators=(',', ':'))


    #newList = list(reversed(list_id_actions))
    Operation_E = openGoto_WarehouseTemplate(taskTemplate,list_inv_id_actions,id_build,id_build_descrip,location_building,EntityAgriFarm)
    OperationEntity.append(Operation_E)
    list_id_op.append(Operation_E["id"])
    file_name = os.path.join(filled_tasks, 'OperationGotoWarehouse.json')
    with open(file_name, 'w+') as f:
        json.dump(Operation_E, f, indent=2, separators=(',', ':'))

    Operation_E = openShutdownTemplate(taskTemplate,id_build,id_build_descrip,location_building,EntityAgriFarm)
    OperationEntity.append(Operation_E)
    list_id_op.append(Operation_E["id"])
    file_name = os.path.join(filled_tasks, 'OperationShutdown.json')
    with open(file_name, 'w+') as f:
        json.dump(Operation_E, f, indent=2, separators=(',', ':'))

    #print(list_id_op)

    Mission_E = openMissionTemplate(taskTemplate,list_id_op,EntityAgriFarm,dicc_plan[a[i]],full_path_locations,EntityAgriRobot_id)
    MissionEntity.append(Mission_E)
    file_name = os.path.join(filled_tasks, 'MissionFarmCSIC.json')
    with open(file_name, 'w+') as f:
        json.dump(Mission_E, f, indent=2, separators=(',', ':'))
