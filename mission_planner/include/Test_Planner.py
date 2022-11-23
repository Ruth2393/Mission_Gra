# -*-encoding:utf-8-*-

import json
import os.path
import shapely.geometry as sg
from shapely.geometry import Polygon
from shapely.geometry import *
from grafo_welaser_functions import trace_graph
import matplotlib.pyplot as plt
import numpy as np
import math
from shapely import affinity
import utm
import pyproj
import shapely.geometry as geometry
from pyproj import Proj
from shapely.wkt import loads
import networkx as nx
import graphviz

import itertools
import random




if __name__ == '__main__':



	os.chdir('../..')
	th=os.getcwd()
	dir_parcel=th+"/map-builder/filledTemplates"
	files=os.listdir(dir_parcel)

	with open(dir_parcel+"/AgriParcel6.json") as f:
		ParcelEntity = json.load(f)
		print(ParcelEntity)


coordenadas = ParcelEntity["location"]["coordinates"][0]
interRow=ParcelEntity["interRowDistance"]
gate_loc= ParcelEntity["gateLocation"]["coordinates"]


utm= Proj(proj='utm',zone=30,ellps='WGS84', preserve_units=False)

#--------------------------------------------------------------------------------------------------
gate_loc_utm=[]
for i in range(len(gate_loc)):
	x, y = utm(gate_loc[i][1], gate_loc[i][0])
	gate_loc_utm.append([x,y])
	#plt.plot(x,y,marker="p")
	#print(x, y)

gate_loc_utm=[((gate_loc_utm[0][0]+gate_loc_utm[1][0])/2),((gate_loc_utm[0][1]+gate_loc_utm[1][1])/2)]  #Punto medio
#plt.plot(gate_loc_utm[0],gate_loc_utm[1],marker="o")
print(gate_loc_utm)
gate_loc_utm = Point(gate_loc_utm)
print(gate_loc_utm)
coord_utm=[]


for i in range(len(coordenadas)):
	x, y = utm(coordenadas[i][1], coordenadas[i][0])
	coord_utm.append([x,y])
#---------------------------------------------------------------------------------------------------

#plt.plot(coord_utm[0][0],coord_utm[0][1],marker="o")
#plt.plot(coord_utm[len(coord_utm)-2][0],coord_utm[len(coord_utm)-2][1],marker="o")


poly= Polygon(coord_utm)
int_poly = sg.polygon.orient(poly, (-0.75)).buffer(-0.75)


#Calculamos la lista de vertices
vertices=np.array(int_poly.exterior.coords)

#Calculamos la distancia
distancia=np.sqrt((vertices[:,0]-gate_loc_utm.x)**2+(vertices[:,1]-gate_loc_utm.y)**2)

#Buscamos el valor minimo
index=np.argmin(distancia)

#Buscamos la coordenada del vertice minimo
vertice_cercano=vertices[index]

#Imprimimos la coordenada del vertice minimo
print("vertice_cercano")
print(vertice_cercano)


#plt.plot(vertice_cercano[0], vertice_cercano[1], marker="x")


#--------------------------------------------------
# Crea un LineString con un punto y el bearing,  #1.5707+bearing
def createLineString(coor_a,bearing):
	end_x = coor_a.x + (30 * math.cos(bearing))
	end_y = coor_a.y + (30 * math.sin(bearing))
	ini_x = coor_a.x - (30 * math.cos(bearing))
	ini_y = coor_a.y - (30 * math.sin(bearing))
	lin=LineString([(ini_x,ini_y),(end_x,end_y)])
	return lin


#coor_a=geometry.Point(coord_utm[0][0],coord_utm[0][1])
coor_a=geometry.Point(vertice_cercano[0],vertice_cercano[1])
bearing= math.radians(ParcelEntity["bearing"])

#Se crea la primera linea de la siembra con las coordenadas mas cercanas al vertice y el bearing
lin1=createLineString(coor_a,bearing)

t=30	#numero de lineas a crear
espacio= interRow


lista=[]
tamaño= int(t/espacio)
for i in range(tamaño):
	lista.append(i*espacio)

list_lineas=[]
for i in range(len(lista)):
    list_lineas.append(lin1.parallel_offset(lista[i],"right"))
for i in range(len(lista)):
    list_lineas.append(lin1.parallel_offset(lista[i],"left"))


#-----------------------------------------------------------------------------------------------

dist=lin1.length/120
points_inter=[]
points_inter_p=[]
list_points=[]
for i in range(len(list_lineas)):
	x,y = list_lineas[i].coords.xy
	for j in range(120):
		p=list_lineas[i].interpolate(j*dist)
		if p.within(int_poly) == True:
			points_inter.append([p.x,p.y])
			points_inter_p.append(p)
		#if p.touches(int_poly) ==True:
	list_points.append(points_inter)
	points_inter=[]


#print(list_points)   #lista de puntos de lineas


line_ma=[]
for points_inter in list_points:
	linea_lon= len(points_inter)
	#print(linea_lon)
	line_ma.append(linea_lon)

line_ma.sort(reverse=True)
#print("ordenados")
#print(line_ma)
p1=line_ma[0]
p1m=(p1*75)/100



for i in line_ma:
	if i<p1m:
		line_ma.remove(i)

segunda_lista = [elemento_lista for elemento_lista in list_points if elemento_lista != []]

print(len(segunda_lista))
i=0
while i < len(segunda_lista):
	#print(i)
	#print(segunda_lista[i])
	linea_lon = len(segunda_lista[i])
	if linea_lon<p1m:
		segunda_lista.pop(i)
		#i=i-1
		#print("elim")
	else:
		for j in range(len(segunda_lista[i])):
			x1p=segunda_lista[i][j][0]
			y1p=segunda_lista[i][j][1]
			plt.plot(x1p,y1p,marker="1",color='#8fce00')
		i=i+1


 #Lista sin items vacios y sin menores a la mitad
#print(segunda_lista)  #lista de lineas(puntos) sin menores a la mitad y sin items vacios.


#-------CAMINO DEL ROBOT ENTRE LAS LINEAS DE CULTIVO-----------------
list_roadrobot=[]


# Pregunta si la distancia de la siembra esta entre dos valores determinados.
if (interRow > 0.676) and (interRow < 1.2 ):
	 list_roadrobot.append(lin1.parallel_offset(interRow/2,"right"))
	 list_roadrobot.append(lin1.parallel_offset(interRow/2,"left"))


t=30
espacio= interRow*2  #Aqui es x2 porq en este intervalo 0.676 y 1.2 solo se pueden abarcar dos lineas de siembra.

lista=[]
tamaño= int(t/espacio)
for i in range(tamaño):
	lista.append(i*espacio)


linea_inicial_right=list_roadrobot[0]
linea_inicial_left=list_roadrobot[1]
list_roadrobot=[]


list_lineas=[]
for i in range(len(lista)):
    list_roadrobot.append(linea_inicial_right.parallel_offset(lista[i],"left"))
for i in range(len(lista)):
    list_roadrobot.append(linea_inicial_left.parallel_offset(lista[i],"left"))


#-------------------------------------------------

dist=lin1.length/120
points_inter=[]
points_inter_p=[]
list_points=[]
for i in range(len(list_roadrobot)):
	x,y = list_roadrobot[i].coords.xy
	for j in range(120):
		p=list_roadrobot[i].interpolate(j*dist)
		if p.within(int_poly) == True:
			points_inter.append([p.x,p.y])
			points_inter_p.append(p)

	list_points.append(points_inter)
	points_inter=[]

segunda_lista = [elemento_lista for elemento_lista in list_points if elemento_lista != []]

for i in range(len(segunda_lista)):
	linea_lon = len(segunda_lista[i])
	if linea_lon<p1m:
		segunda_lista.pop(i)
	else:
		for j in range(len(segunda_lista[i])):
			x1p=segunda_lista[i][j][0]
			y1p=segunda_lista[i][j][1]



in_fin_road_robot=[]
for i in range(len(segunda_lista)):
	xin=segunda_lista[i][0][0]
	yin=segunda_lista[i][0][1]
	tamaño=len(segunda_lista[i])
	xout=segunda_lista[i][tamaño-1][0]
	yout=segunda_lista[i][tamaño-1][1]
	distancia1=np.sqrt((xin-gate_loc_utm.x)**2+(yin-gate_loc_utm.y)**2)
	distancia2=np.sqrt((xout-gate_loc_utm.x)**2+(yout-gate_loc_utm.y)**2)
	if distancia1<distancia2:
		in_fin_road_robot.append([[xin,yin],[xout,yout]])
	else:
		in_fin_road_robot.append([[xout,yout],[xin,yin]])

print("#PUNTOS DE LAS LINEAS POR DONDE PASARÍA EL ROBOT")
print(in_fin_road_robot)  #PUNTOS DE LAS LINEAS POR DONDE PASARÍA EL ROBOT

#print(in_fin_road_robot[0])


print(len(in_fin_road_robot))

x,y = poly.exterior.xy
plt.plot(x, y, color='#6699cc', alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)
#plt.plot(in_fin_road_robot[0][0][0],in_fin_road_robot[0][0][1],marker="s")
#plt.show()
#-------------------------------------------------------------------------------------

n=4

new_order_list=[]
transition_list= in_fin_road_robot.copy()
print('Luuis')
print(transition_list)
#transition_list=[1,2,3,4,5,6,7,8,9,10]
i=0
while len(transition_list)>0:
	if (i)>=(len(transition_list)):
		i=0
		n=n-1
	else:
		new_order_list.append(transition_list[i])
		transition_list.pop(i)
		i=i+n


# while len(transition_list)>0:
# 	if (i)>=(len(transition_list)):
# 		break
# 	else:
# 		new_order_list.append(transition_list[i])
# 		transition_list.pop(i)
# 		i=i+n




print(new_order_list)


#print(len(new_order_list))

sucesion_puntos_parcel=[]
change=0
for i in range(len(new_order_list)):
	if change == 0:
		sucesion_puntos_parcel.append(new_order_list[i][0])
		sucesion_puntos_parcel.append(new_order_list[i][1])
		change=1
	else:
		sucesion_puntos_parcel.append(new_order_list[i][1])
		sucesion_puntos_parcel.append(new_order_list[i][0])
		change=0

# indexes = []
# for point in sucesion_puntos_parcel:
# 	print(point[0])
# 	for i in range(len(in_fin_road_robot)):
# 		lane = in_fin_road_robot[i]
# 		for point2 in lane:
# 			print(point2)
# 			if point[0] == point2[0]:
# 				indexes.append(i)
# 				break
# print(indexes)
# print('Paola')
# print(len(in_fin_road_robot))


def plot(puntos):
	x=list(map(lambda x:x[0],puntos))
	y=list(map(lambda x:x[1],puntos))
	plt.plot(x,y,color='#66c2cc')
	plt.show()


plot(sucesion_puntos_parcel)



#--- GRAFFO ------------------------------------------------------------

G = nx.Graph()

lista_g=in_fin_road_robot
print("HOlssss")
print(lista_g)

diccionario_lista_g={}
i=0
for elemento in lista_g:
	i+=1
	diccionario_lista_g["p"+str(i)]=elemento[0]
	i+=1
	diccionario_lista_g["p"+str(i)]=elemento[1]
print(diccionario_lista_g)

G.add_nodes_from(diccionario_lista_g.keys())
points=list(diccionario_lista_g.keys())
print("gggggggg")
print(len(points))

for i in range(len(points)):
	if (i+1)<len(points):
		if i%2==0:
			print(points[i], " + ", points[i+1])
			G.add_edge(points[i],points[i+1],weight=0.01)
			#G.add_edge(points[i],points[i+2],weight=1)
		else:
			print(points[i], " + ", points[i+2])
			G.add_edge(points[i],points[i+2],weight=30)
	if (i+2)<len(points):
		if i%2==0:
			print(points[i], " + ", points[i+2])
			G.add_edge(points[i],points[i+2],weight=30)
			#G.add_edge(points[i],points[i+2],weight=1)

	if (i+4)<len(points):
		print(points[i], " + ", points[i+4])
		G.add_edge(points[i],points[i+4],weight=20)

	if (i+6)<len(points):
		print(points[i], " + ", points[i+6])
		G.add_edge(points[i],points[i+6],weight=10)
	p=10
	for x in range(8, (len(points)), 2):
		if (i+x)<len(points):
			print(points[i], " + ", points[i+x]," = ",p+10)
			G.add_edge(points[i],points[i+x],weight=p+10)
			p=p+10


#nx.draw(G)
pos = nx.spring_layout(G, iterations=100, seed=173, weight=None)

# nodes
nx.draw_networkx_nodes(G, pos, node_size=100)

# edges
nx.draw_networkx_edges(G, pos, width=1)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels,font_size=8)
nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif")

plt.show()

#-------------------------------------------------------------------------------
