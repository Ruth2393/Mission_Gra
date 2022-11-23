#!/usr/bin/env python
from __future__ import division

import requests
import os
import sys
import argparse
import json
import time
import signal



homePath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(homePath)



#Path to utilities
pathToUtils = homePath + 'utils'
sys.path.append(pathToUtils)


SEPARATOR_CHAR = "%27"

class RobotStatusFiWARE():

    def __init__(self,sim):

        self.pathtoEntity = homePath + '/filledTemplates/'
        self.files= os.listdir(self.pathtoEntity)

    def updatedir(self):
        self.pathtoEntity = homePath + '/filledTemplates/'
        self.files= os.listdir(self.pathtoEntity)

    def RegisterEntity(self,entity,entity_id):
        # Register the entity
        out = True
        try:
            #Check if entity exist
            r = requests.get(url = "http://{}:{}/v2/entities?id={}".format(os.environ.get("ORION_IP"), os.environ.get("ORION_PORT_EXT"), entity_id))
            data = r.json()
            #print(data)
            print(entity_id)

            if len(data) == 0:
                print('Noexiste')
                r = requests.post(url = "http://{}:{}/v2/entities?options=keyValues".format(os.environ.get("ORION_IP"), os.environ.get("ORION_PORT_EXT")), data = json.dumps(entity), headers = {"Content-Type": "application/json"})
                #print(r)
            else:
                del entity["id"]
                del entity["type"]
                #print(entity)
                self.PatchEntity(entity,entity_id)
                print('patched')
        except requests.exceptions.RequestException as e:
            print(e)
            out = False
        return out

    def PatchEntity(self,entity,entity_id):
        #Update
        out = True
        try:
            #r = requests.patch(url = "http://{}:{}/v2/entities/{}/attrs?options=keyValues".format(os.environ.get("ORION_IP"), os.environ.get("ORION_PORT_EXT"), entity_id), data = json.dumps(entity), headers = {"Content-Type": "application/json"})
            r = requests.patch(url = "http://{}:{}/v2/entities/{}/attrs?options=keyValues".format(os.environ.get("ORION_IP"), os.environ.get("ORION_PORT_EXT"),entity_id), data = json.dumps(entity), headers = {"Content-Type": "application/json"})
            #print("patcheado")
        except requests.exceptions.RequestException as e:
            print(e)
            out = False

        return out


    def main(self):

        self.updatedir()
        try:
            for i in range(len(self.files)):
                with open(self.pathtoEntity+self.files[i]) as f:
                    self.EntityToDump = json.load(f)
                    self.id =self.EntityToDump["id"]
                    self.RegisterEntity(self.EntityToDump,self.id)
        except:
                print('ERROR:Update Dir')



    def keyboardInterruptHandler(self,signal,frame):
        self.shutdown_var = True

if __name__ == '__main__':

    main = RobotStatusFiWARE("-s")
    signal.signal(signal.SIGINT, main.keyboardInterruptHandler)

    main.main()
