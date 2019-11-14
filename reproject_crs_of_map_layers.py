import os


#checked_layers = [layer.name() for layer in QgsProject().instance().layerTreeRoot().children()]

wrong_crs = []

for layer in QgsProject().instance().mapLayers().values():
#    print(layer.name(), "=",layer.crs().authid())
    if layer.crs().authid() != 'EPSG:4326':
        wrong_crs.append(layer)

print("Layers with wrong CRS...")
for layer in wrong_crs:
    print(layer.name(), '=', layer.crs().authid())
    

#print(qgis.utils.iface.activeLayer().crs().authid())


#processing.algorithmHelp('native:reprojectlayer')

myfilepath = iface.activeLayer().dataProvider().dataSourceUri()
#print(type(iface.activeLayer()))

for layer in wrong_crs:
#    print(layer.dataProvider().dataSourceUri())
    parameters = { 'INPUT' : '/Users/ep9k/Desktop/Oyster Reefs/Hog Island/HG2.shp', 
                    'OUTPUT' : 'memory:', 
                    'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:4326') }
    
    processing.runAndLoadResults('native:reprojectlayer', parameters)
    



