import os
import json
import pyproj

# define the UTM and lat/lon projections
utm = pyproj.Proj(proj='utm', zone=31, ellps='WGS84')
latlng = pyproj.Proj(proj='latlong', ellps='WGS84')

# folder_path = 'C:/Jaume/projects/python/utm-to-latlng/UTM Files'
folder_path = 'UTM Files'

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            datos = json.load(file)
            
        for feature in datos['features']:
        # get the coordinates of the polygon
            coords = feature['geometry']['coordinates'][0][0]
            # convert each pair of UTM coordinates to lat/lon
            latlng_coords = []
            for coord in coords:
                x, y = coord
                lon, lat = pyproj.transform(utm, latlng, x, y)
                latlng_coords.append([lat, lon])
            # replace the UTM coordinates with the lat/lon coordinates
            feature['geometry']['coordinates'] = [latlng_coords]

        # write the modified data back to a file
        with open('latlng.json', 'w') as f:
            json.dump(datos, f)

        # Convertir a solo coordenadas: latlng
        new_data = []
        for feature in datos['features']:
            new_feature = feature['geometry']['coordinates']
            new_data.extend(new_feature)

        # Guardar los datos modificados en un nuevo archivo
        with open('Latlng Files/{}'.format(filename), 'w') as file:
            json.dump(new_data, file)