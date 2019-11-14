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

