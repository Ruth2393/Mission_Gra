# -*-encoding:utf-8-*-

import utm


def Polygon_utm(coordinates):   #This function extracts the geoposition coordinates and converts them to the UTM standard.
    utm_coord = []
    for i in range(1, len(coordinates)):
        coord = coordinates[i]
        temp = utm.from_latlon(coord[1], coord[0])
        utm_coord.append([temp[0], temp[1]])

    return utm_coord


def StandardCoordinates(coordinates):   #This function sorts latitude and longitude according to standard ISO6709.
    latlong = []
    for data in coordinates:
        latlong.append([data[1], data[0]])

    return latlong
