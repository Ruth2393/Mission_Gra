import math
from pyproj import Proj


def calculateBearing(number,data):
    utm= Proj(proj='utm',zone=30,ellps='WGS84', preserve_units=False)
    for i in range(len(data)):
        if str(number) in data[i]["type"]:
            coord=(data[i]["geometry"]["coordinates"])
           # x1, y1 = utm(coord[0][1], coord[0][0])
           # x2, y2 = utm(coord[1][1], coord[1][0])
            x1, y1 = utm(coord[0][0], coord[0][1])
            x2, y2 = utm(coord[1][0], coord[1][1])
            angulo = coord_a_angulo(x1,y1,x2,y2)
            break
    return angulo


def coord_a_angulo(x1, y1, x2, y2):
    rads = math.atan((y2-y1)/(x2-x1))*(180/math.pi)
    if rads < 0:
        rads = 180+rads
    return rads
