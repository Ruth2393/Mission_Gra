# -*-encoding:utf-8-*-


def Extract(map):  # This function extracts the necessary data from the initial map.

    elements = []
    for entity in map["features"]:
        dictionary = {}

        if 'type' in entity['properties'] and entity['properties']['type'] == 'AgriFarm':
            dictionary['type'] = entity['properties']['type'] if 'type' in entity['properties'] else None
            dictionary['description'] = entity['properties']['description'] \
                if 'description' in entity['properties'] else None
            dictionary['geometry'] = entity['geometry'] \
                if 'coordinates' in entity['geometry'] else None

        elif 'type' in entity['properties'] and "AgriParcel" in entity['properties']['type'] \
                and not "Children" in entity['properties']['type']:
            dictionary['type'] = entity['properties']['type'] \
                if 'type' in entity['properties'] else None
            dictionary['description'] = entity['properties']['description'] \
                if 'description' in entity['properties'] else None
            dictionary['geometry'] = entity['geometry'] if 'coordinates' in entity['geometry'] else None
            dictionary['headland'] = entity['properties']['headland'] if 'headland' in entity['properties'] else None
            dictionary['category'] = entity['properties']['category'] if 'category' in entity['properties'] else None

        elif 'type' in entity['properties'] and "AgriParcel" in entity['properties']['type'] \
                and "Children" in entity['properties']['type']:
            dictionary['type'] = entity['properties']['type'] \
                if 'type' in entity['properties'] else None
            dictionary['description'] = entity['properties']['description'] \
                if 'description' in entity['properties'] else None
            dictionary['geometry'] = entity['geometry'] \
                if 'coordinates' in entity['geometry'] else None

        elif 'type' in entity['properties'] and "Road" in entity ['properties']['type']:
            dictionary['type'] = entity['properties']['type'] \
                if 'type' in entity['properties'] else None
            dictionary['geometry'] = entity['geometry'] \
                if 'coordinates' in entity['geometry'] else None
            dictionary['material'] = entity['properties']['material'] if 'material' in entity['properties'] else None


        elif 'type' in entity['properties'] and entity['properties']['type'] == 'Point':
            dictionary['type'] = entity['properties']['type'] \
                if 'type' in entity['properties'] else None
            dictionary['description'] = entity['properties']['description'] \
                if 'description' in entity['properties'] else None
            dictionary['geometry'] = entity['geometry'] \
                if 'coordinates' in entity['geometry'] else None

        elif 'type' in entity['properties'] and "Bearing" in entity['properties']['type']:
            dictionary['type'] = entity['properties']['type'] \
                if 'type' in entity['properties'] else None
            dictionary['geometry'] = entity['geometry'] \
                if 'coordinates' in entity['geometry'] else None


        elif 'type' in entity['properties'] and "Building" in entity ['properties']['type']:
            dictionary['type'] = entity['properties']['type'] \
                if 'type' in entity['properties'] else None
            dictionary['description'] = entity['properties']['description'] \
                if 'description' in entity['properties'] else None
            dictionary['geometry'] = entity['geometry'] \
                if 'coordinates' in entity['geometry'] else None


        elif 'type' in entity['properties'] and "Gate" in entity ['properties']['type']:
            dictionary['type'] = entity['properties']['type'] if 'type' in entity['properties'] else None
            dictionary['hasAgriParcel'] = entity['properties']['hasAgriParcel'] if 'hasAgriParcel' in entity['properties'] else None
            dictionary['description'] = entity['properties']['description'] if 'description' in entity['properties'] else None
            dictionary['geometry'] = entity['geometry'] if 'coordinates' in entity['geometry'] else None


        elif 'type' in entity['properties'] and "Restricted" in entity ['properties']['type']:
            dictionary['type'] = entity['properties']['type'] \
                if 'type' in entity['properties'] else None
            dictionary['description'] = entity['properties']['description'] \
                if 'description' in entity['properties'] else None
            dictionary['geometry'] = entity['geometry'] \
                if 'coordinates' in entity['geometry'] else None
            dictionary['category'] = entity['properties']['category'] if 'category' in entity['properties'] else None


        if len(dictionary) > 0:
            elements.append(dictionary)

    return elements
