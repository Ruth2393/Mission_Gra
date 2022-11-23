#Encontar el centroide de un poligono irregular
#uso de la formula de la baricentro

#definimos los puntos del poligono
#poligono irregular
# p1 = (2,2)
# p2 = (4,1)
# p3 = (3,4)
# p4 = (4,6)
# p5 = (1,4)
# puntos = [p1,p2,p3,p4,p5]

#creamos una variable que almacenara la suma de los puntos
from pyproj import Proj, transform

def cal_centroide(puntos):
    #miramos los puntos
    suma = (0,0)
    for i in range(len(puntos)):
        suma = (suma[0] + puntos[i][0], suma[1] + puntos[i][1])
        print(suma)
    #calculamos el centroide de los puntos
    centroide = (suma[0]/len(puntos),suma[1]/len(puntos))

    #mostramos los resultados
    print("El centroide es: ",chg_epsg_utm(centroide))
    print("El centroide es: ",centroide)
    return(centroide)

def chg_utm_epsg(coordinate):
    inProj = Proj('epsg:4326')
    outProj = Proj('epsg:3857')
    x,y = transform(inProj,outProj,coordinate[0],coordinate[1])
    print(x,y)
    return (x,y)


def chg_epsg_utm(coordinate):
    outProj = Proj('epsg:4326')
    inProj = Proj('epsg:3857')
    x,y = transform(inProj,outProj,coordinate[0],coordinate[1])
    print(x,y)
    return (x,y)
