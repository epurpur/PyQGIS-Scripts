
import processing

#gets layer ids for all the map layers
layersToAdd = [layer for layer in QgsProject().instance().mapLayers().values()]

layer_paths = ['/Users/ep9k/Desktop/BRE/Zone1aKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone1bKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone1cKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone1dKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone1eKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone1fKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone1gKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone2aKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone2bKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone2cKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone2dKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone2eKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone2fKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone3aKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone3bKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone3cKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone3dKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone3eKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone3fKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone4aKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone4bKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone4cKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone4dKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone4eKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone4fKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone5aKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone5bKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone5cKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone5dKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone5eKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone5fKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone5gKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone5hKeepers.shp',
                '/Users/ep9k/Desktop/BRE/Zone5iKeepers.shp']

parameters = {'LAYERS': layer_paths,
            'CRS': None,
            'OUTPUT': '/Users/ep9k/Desktop/BRE/AllKeepers2018.shp'}

processing.runAndLoadResults('qgis:mergevectorlayers', parameters)
    

