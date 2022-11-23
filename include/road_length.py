
from geopy.distance import geodesic
import math

def distance(coordinates):
    total = 0
    #print(coordinates)
    for i in range (len(coordinates)-1):
        distancia=geodesic(coordinates[i],coordinates[i+1]).meters
        total = total + distancia
        #print(total)
    return total
