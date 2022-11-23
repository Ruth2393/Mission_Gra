# WeLASER - Data Models

List of used external entities:
- `AgriCrop` https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriCrop/doc/spec.md
- `Building` https://github.com/smart-data-models/dataModel.Building/blob/master/Building/doc/spec.md
    - Transitable (we are not going to model this attribute since we will assume that the warehouse is transitable)
- `Camera`: https://github.com/smart-data-models/dataModel.Device/tree/master/Camera/doc/spec.md
- `Device`: https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md
- `RestrictedTrafficArea` https://github.com/smart-data-models/dataModel.Transportation/blob/master/RestrictedTrafficArea/README.md
- `Road` https://github.com/smart-data-models/dataModel.Transportation/blob/master/Road/doc/spec.md

Other entities:
- `User` (need to look for it, not urgent). All the users listed as owner in the agriFarm will be able to access al the information
- `Weed` (TBD with LZH)

## Next steps

- [x] (MF) Create a Docker environment reproducing the whole cloud infrastructure
- [x] (MF) Create a PoC with robot, devices, and ingestion of the entities
- [ ] (MF) Prepare some mock-ups for Luis in order to 
    - [x] subscribe to robot changes/commands
    - [ ] listen to kafka
    - [ ] read/write to mongo
    - [x] join information on AgriFarm and AgriParcel
- [ ] Update the simulation with the AgriRobot and the mission. Robot starts on the gate, we `start` the weeding mission, `pause`, `resume`, `stop`.
    - [x] (MF) Cloud side
    - [ ] (LF) Robot side 
- [ ] (LE) Check the (un)necessary attributes of the entities, verify if the entities are generic enough also for other robots/applications in the AgriDomain
- [ ] (LE) Update AgriFarm and AgriParcel and add the other entities to describe the CSIC farm
- [ ] (LE) Understand how the MissionPlanner works, and who updates the actions

## Next meetings

- June: preliminary demonstration. Robot moving from warehouse go to the field, move 2 turns, go back to the warehouse.

Python demo
- Listen to kafka
- Query mongodb
- Write to mongodb
- Demonstrate update FIWARE entity

## Open questions

- Should we keep some statistics on the weeds?
    - GA: we could have coverage maps, to map the planning. We are not doing that. Bur we can infer coverage maps from the robot / perception system.
    - Do we need to model the table of conditions? Not for now

- What information do we send back
- [Not critical] Map creation: Draw the polygons / linestring

## Entities

### HMI

This is a device. We can start the robot only if the HMI is close to the robot.
For now we assume that the user that is logged is close to the robot (something we can plan to do)

### AgriFarm

Access control
- Farmer (control all the farms): update when he seeds/crop

### Agriparcel
- Orientation
- Forbidden area (?)
- Field: any polygon. Cropts are planted in straight lines. Whatever machine goes in the same direction as crops (i.e., you don't corss the crops). The fields are four main parts: 
    - Headland, where the robot turns and destroy the path, you cannot seed there) 
    - Lanes (seeded space). The lane depend on the width of the robot, you want to pass on each lane only 1 time
    - Alleys are the sides of the fields
    - Gate where the robot can enter and leave
- What about rasters?
- Model of the agriparcel:
- I only need the crops, and the gate, and the robot. Then after I see the first lane, the robot will adapt to the other. To us, we need the gate and the agriparcel.
- `hasCrop` is very important
- `cropStatus` (it should be misurated and should be accurate for WeLASER)
- `lastPlantedAt`
- `agriSoil`

### AgriMission

- JSON files with a sequence of points (this is the most basic mission). But we should also put a semantics on those points. We infer the orientation from consecutive points.
- When the robot enters the lane activate the laser, when it exits deactivate it.

RobotModel & robot
ROS (1 robot -> 1 active controller per time)
- Controller: the robot chooses the best controller depending on the situation (i.e., a table of conditions). Normally you do the simplest action possible (i.e., the shortest path in case of movement and the movement is constraineted to not damagae the field nor the robot. Also the orientation of the robot).
- Task (share the list of tasks. FieldNavigation / FarmNavigation concatenate basic tasks such as GoToGoal, FollowLine, MoveBack, Uturn)
- Action
- Robot pose (x, y, z, orientation). We assume the robot is moving on a plane.
- Local vs remote supervisor (the remote controller can recreate the behavior, but it is not that important)
- ROSbug to recrete the original behavior by storing the sequences of ros messages

Drones?
