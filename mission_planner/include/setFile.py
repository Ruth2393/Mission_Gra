# -*-encoding:utf-8-*-

import os
import json


def LoadTemplates(path):    # This function searches for the templates corresponding to AgriFarm and AgriParcel and loads them.

    thisdir = os.path.join(path,'Task/examples')
    content = os.listdir(thisdir)

    for file in content:

        if file.endswith(".json") and file.startswith("Task_Template"):
            with open(os.path.join(thisdir,file)) as taskFile:
                taskTemplate = json.load(taskFile)

    return  taskTemplate
