import json

with open('latlngXY.json') as f:
    datos = json.load(f)

    datos_limpios = []
    for feature in datos['features']:
        new_feature = feature['geometry']['coordinates']
        datos_limpios.append(new_feature)

    invertido = [[y, x] for x, y in datos_limpios]

print(invertido)
