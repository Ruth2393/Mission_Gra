
def match_gates(number,data):
    puerta=[]
    for i in range(len(data)):
        parcels = data[i]["hasAgriParcel"].split(',')
        for j in range(len(parcels)):
            if int(parcels[j]) == int(number):
                puerta.append(data[i]["geometry"]["coordinates"])
    return puerta
