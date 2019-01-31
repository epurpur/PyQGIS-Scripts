#Brian Libgober's stack overflow thread
#https://gis.stackexchange.com/questions/277223/qgsprintlayout-setup-from-pyqgis-3

"""This creates a new print layout"""
project = QgsProject.instance()             #gets a reference to the project instance
#projectInstance = QgsProject()                     #reference to project, but not the instance. Doesn't add new layout to Layout Manager. Do I need a reference to the instance?
manager = project.layoutManager()           #gets a reference to the layout manager
layout = QgsPrintLayout(project)            #makes a new print layout object, takes a QgsProject as argument
layout.initializeDefaults()                         #needs to call this according to documentation
layout.setName('Console4')                           #lets you choose a name for the layout
manager.addLayout(layout)                           #adds layout to manager


"""This adds a map item to the Print Layout"""
map = QgsLayoutItemMap(layout)
map.setRect(20, 20, 20, 20)  
#Set Extent
rectangle = QgsRectangle(1355502, -46398, 1734534, 137094)
map.setExtent(rectangle)
#canvas = iface.mapCanvas()
#map.setExtent(canvas.extent())
layout.addLayoutItem(map)
#Move & Resize
map.attemptMove(QgsLayoutPoint(5, 27, QgsUnitTypes.LayoutMillimeters))
map.attemptResize(QgsLayoutSize(239, 178, QgsUnitTypes.LayoutMillimeters))


"""Checks layer tree objects and stores them in a list. This includes csv tables"""
checked_layers = [layer.name() for layer in QgsProject().instance().layerTreeRoot().children() if layer.isVisible()]
print(f"Adding {checked_layers}" )
#get map layer objects of checked layers by matching their names and store those in a list
layersToAdd = [layer for layer in QgsProject().instance().mapLayers().values() if layer.name() in checked_layers]

"""This adds a legend item to the Print Layout"""
legend = QgsLayoutItemLegend(layout)
legend.setTitle("Legend")
root = QgsLayerTree()
for layer in layersToAdd:
    #add layer objects to the layer tree
    root.addLayer(layer)
legend.model().setRootGroup(root)
layout.addLayoutItem(legend)
legend.attemptMove(QgsLayoutPoint(246, 5, QgsUnitTypes.LayoutMillimeters))


"""This adds labels to the map"""
title = QgsLayoutItemLabel(layout)
title.setText("Title Here")
title.setFont(QFont("Arial", 28))
title.adjustSizeToText()
layout.addLayoutItem(title)
title.attemptMove(QgsLayoutPoint(10, 4, QgsUnitTypes.LayoutMillimeters))

subtitle = QgsLayoutItemLabel(layout)
subtitle.setText("Subtitle Here")
subtitle.setFont(QFont("Arial", 17))
subtitle.adjustSizeToText()
layout.addLayoutItem(subtitle)
subtitle.attemptMove(QgsLayoutPoint(11, 20, QgsUnitTypes.LayoutMillimeters))   #allows moving text box

credit_text = QgsLayoutItemLabel(layout)
credit_text.setText("Credit Text Here")
credit_text.setFont(QFont("Arial", 10))
credit_text.adjustSizeToText()
layout.addLayoutItem(credit_text)
credit_text.attemptMove(QgsLayoutPoint(246, 190, QgsUnitTypes.LayoutMillimeters))



"""This exports a Print Layout as an image"""
manager = QgsProject.instance().layoutManager()     #this is a reference to the layout Manager, which contains a list of print layouts
for layout in manager.printLayouts():               #this prints all existing print layouts in a list
    print(layout.name())

layout = manager.layoutByName("Console4")         #this accesses a specific layout, by name (which is a string)

exporter = QgsLayoutExporter(layout)                #this creates a QgsLayoutExporter object
exporter.exportToPdf('/Users/ep9k/Desktop/TestLayout.pdf', QgsLayoutExporter.PdfExportSettings())      #this exports a pdf of the layout object
#exporter.exportToImage('/Users/ep9k/Desktop/TestLayout.png', QgsLayoutExporter.ImageExportSettings())  #this exports an image of the layout object


