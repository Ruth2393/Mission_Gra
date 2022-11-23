import os
import json
import networkx as nx
import graphviz
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry import LineString
import shapely


def trace_graph(inicio,final):

    G= nx.Graph()
    #os.chdir('../')
    homePath = os.path.dirname(os.path.abspath(__file__))

    print(os.getcwd())
    #os.chdir('../..')
    homePath = os.getcwd()
    print(homePath)
    pathtoEntity = homePath + '/map-builder/filledTemplates/'
    files= os.listdir(pathtoEntity)
    print(files)


    buildings = []
    parcels = []
    roads =[]
    xy_coord=[]


    dicc1={}   #diccionario de todas las entidades, {uid,entidad}
    gates_localization={} #diccionario de {"gate1", coodninate, "gate2", coord .....}
    parcels_gates={}
    name_parcels={}
    files_id={}
    idbuild_dis_road={}
    dist_build_roads ={}


    dic_parcels={}
    dic_buildings={}
    dic_roads={}
    idbuild_coord={}
    idbuild_centroide={}
    idroad_linestring={}
    gate_pm ={}
    idroad_material={}



    #----------------------------------------------------------------------------------------------------------------------------------
    #Punto Inicial del Robot
    # openfield_coord={"OpenField":shapely.geometry.Point(40.31359542166298,-3.4824728965759277)}
    # print(openfield_coord)
    #--------------------------------------------------------------------------------------------------------------------------------------

    try:
        for i in range(len(files)):
            with open(pathtoEntity+files[i]) as f:
                EntityToDump = json.load(f)
                dicc1[EntityToDump["id"]]= EntityToDump
                id= EntityToDump["id"]
                files_id[files[i]]=id #  {"AgriParcel1.json",uuid.......}

                if "AgriFarm" in id:
                    buildings = EntityToDump["hasBuilding"]   #[uuid1,uuid2,uuid3...]
                    parcels = EntityToDump["hasAgriParcel"]    #[uuid1,uuid2.......]
                    roads = EntityToDump["hasRoadSegment"] #[uuid1,uuid2,uuid3]

    except:
        print('ERROR: AgriFarm Entity not defined')


    #̣̣̣̣̣̣̣--------------------------------------------------------------------------------------------------------

    def search_name(uid):   # Busca el name.json de un uid y retorna el name.json
        for key in files_id:
            if files_id[key] == uid:
                return (key)


    def find_key(dic, val):  # Busca el key de un valor en un diccionario y retorna  [True, key] si lo encuentra, caso contratio [False,None]
        for key in dic:
            if dic[key] == val:
                return [True,key]
        return [False,"None"]


    def translate(lista):  # Realiza un diccionario con el nombre del archivo y el uid
        dic_name={}
        for i in range(len(lista)):
            [bool,key]=find_key(files_id,lista[i])
            dic_name[key]=lista[i]
        return(dic_name)


    #----------------------------------------------------------------------------------------------------------------------

    for i in range(len(parcels)):  #    Localiza las puertas en las parcelas y realiza un match
        idp = parcels[i]
        ga = dicc1[idp]["gateLocation"]["coordinates"]

        if len(gates_localization) == 0:
            var_gate=1
            gates_localization["Gate"+str(var_gate)]=ga
        else:
            if find_key(gates_localization,ga)[0] == False:
                var_gate=var_gate+1
                gates_localization["Gate"+str(var_gate)]=ga
        parcels_gates[idp]="Gate"+str(var_gate)


    #----------------------------------------------------------------------------------------------------------------------


    #Sacar punto medio de los Gates {Gate1, punto medio, Gate2, punto medio}
    for key in gates_localization:
        p1= gates_localization[key][0]
        p2 = gates_localization[key][1]
        pm =  shapely.geometry.Point((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        gate_pm[key]=pm

    print("Gate y su punto medio:")
    print(gate_pm)
    print(gate_pm["Gate1"])
    print(gate_pm["Gate2"])



    #------------------------------------------------------------------------


    #Encontrar el Centroide de los Buildings
    for i in range(len(buildings)):
        id_build = buildings[i]
        build_coord =dicc1[id_build]["location"]["coordinates"][0]
        print(build_coord)
        poligono = shapely.geometry.Polygon(build_coord)
        centr= poligono.centroid

        idbuild_coord[id_build]=poligono
        idbuild_centroide[id_build]=centr



    #Realiza un diccionario con idroad y las coordenadas las tranforma en tipo LineString para poder encontrar la distancia.
    for i in range(len(roads)):
        id_road = roads[i]
        road_LineString=dicc1[id_road]["location"]["coordinates"]
        roadline = LineString(road_LineString)
        print(roadline)
        idroad_linestring[id_road]=roadline
        idroad_material[id_road]=dicc1[id_road]["roadMaterial"]


    #Distancia minima del Centroide(Point) a los Roads (LineString)
    for key_build in idbuild_centroide:
        for key_road in idroad_linestring:
            dist = (idbuild_centroide[key_build].distance(idroad_linestring[key_road]))*100000


    #Distancia minima de los Buildings(poligonos) a los Roads (LineString)
    for key_build in idbuild_coord:
        dist_build_roads={}
        for key_road in idroad_linestring:
            dist = (idbuild_coord[key_build].distance(idroad_linestring[key_road]))*100000
            dist_build_roads[search_name(key_road)]=dist
            idbuild_dis_road[search_name(key_build)]=dist_build_roads


    print("Distancia de Buildings a Roads")
    print(idbuild_dis_road)


    #print(gates_localization)   #{"gate1",coordinate[],"gate2",coordinate[].....}
    #print(parcels_gates) #{idparcel,gate , idparcel,gate ...}


    dic_parcels=translate(parcels)  # Pasa de uid a Name.json
    print(dic_parcels)
    dic_buildings=translate(buildings) # Pasa de uid a Name.json
    print(dic_buildings)
    dic_roads=translate(roads) # Pasa de uid a Name.json
    print(dic_roads)


    roads_key = list(dic_roads)
    print(roads_key)
    parcels_key = list(dic_parcels)
    print(parcels_key)
    buildings_key=list(dic_buildings)
    print(buildings_key)



    #Añade los nodos al Grafo
    #G.add_nodes_from(buildings_key)
    G.add_nodes_from(gates_localization)
    G.add_nodes_from(roads_key)
    G.add_nodes_from(parcels_key)
    G.add_node("OpenField")



    #Añadir union entre las parcelas y los Gates con peso = 0
    for key in parcels_gates:
        G.add_edge(find_key(dic_parcels,key)[1],parcels_gates[key],weight=0)


    #Añadir unión entre los ROADS con el peso(distancia entre ellos)
    for key1 in idroad_linestring:
        for key2 in idroad_linestring:
            if key1 != key2:
                dist = (idroad_linestring[key1].distance(idroad_linestring[key2]))*100000
                #print(dist)
                G.add_edge(search_name(key1),search_name(key2),weight=float(dist))
            #search_name(key)



    #Añadir union entre Buildings y Roads con pesos (distancia)
    print(idbuild_dis_road)
    for key1 in idbuild_dis_road:
        for key2 in idbuild_dis_road[key1]:
            if idbuild_dis_road[key1][key2] == 0.0:
                if idroad_material[files_id[key2]] == 'asphalt':
                    pesos = '{0:.4g}'.format(idbuild_dis_road[key1][key2])
                    G.add_edge(key1,key2,weight=float(pesos))


    #Añadir union entre Gate y ROad y pesos (distancia)
    for key1 in idroad_linestring:
        for key2 in gate_pm:
            if idroad_material[key1] == 'dirt':
                dist=(gate_pm[key2].distance(idroad_linestring[key1]))*100000
                if dist<=0.5:
                    pesos = '{0:.4g}'.format(dist)
                    G.add_edge(search_name(key1),key2,weight=float(pesos))
                    G.add_edge("OpenField",search_name(key1),weight=0)
                    G.add_edge("OpenField","Gate2",weight=0)


    #graphviz.Source(A.to_string()) # mostrar en jupyter
    #pos = nx.spring_layout(G,seed=7,k=5)  # positions for all nodes - seed for reproducibility
    pos = nx.spring_layout(G, iterations=100, seed=173, weight=None)

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=100)

    # edges
    nx.draw_networkx_edges(G, pos, width=1)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels,font_size=8)
    nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif")

    # node labels

    # ax = plt.gca()
    # ax.margins(0.08)
    # plt.axis("off")
    # plt.tight_layout()
    # plt.show()


#--------------------------------------------------------------------------------------------------------------------------------------------------------

#Algoritmo de Dijkstra para encontrar el camino de menor coste    print("Path a seguir: desde Building 1 hasta AgriParcel5")
    MP = nx.dijkstra_path(G,inicio,final) # (Grafo, "inicio","objetivo") DEVUELVE EL PATH A SEGUIR
    dic_MP={}
    for i in range(len(MP)):
        if "Gate" in MP[i]:
            p =gate_pm[MP[i]]
            punto_medio=list(p.coords)
            dic_MP[MP[i]] = {"location":{"coordinates":punto_medio},"type":"gate","name":"Gate","id":"Gate"}
            print(gate_pm[MP[i]])

        if "OpenField" in MP[i]:
            dic_MP[MP[i]] = ["",""]
            print(["",""])

        if MP[i] != "OpenField" and not "Gate" in MP[i]:
            dic_MP[MP[i]] = dicc1[files_id[MP[i]]]
            dic_mis= files_id[MP[i]]
            print(dic_mis)

    print(dic_MP)
    return dic_MP

#--------------------------------------------------------------------------------
    #return G

# A.layout('dot')
# A.draw('salida.png') # guardar como png
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def main():
    path = trace_graph("Building1.json","AgriParcel6.json")
    #path = mission_path(grafo,"Building 1.json","AgriParcel 5.json")
    #print(grafo)
    print(path.keys())


if __name__ == "__main__":
    main()
