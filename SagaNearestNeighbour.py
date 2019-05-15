"""Template for SAGA: Nearest Neighbour tool"""

import processing


#print(help(processing.algorithmHelp('saga:nearestneighbour')))

parameters = {'SHAPES': '/Users/ep9k/Desktop/RandomPoints.gpkg',
            'FIELD': 'OBJECTID',
            'TARGET_USER_FITS': 0,
            'TARGET_OUT_GRID': '/Users/ep9k/Desktop/Output.sdat'}

processing.runAndLoadResults('saga:nearestneighbour', parameters)