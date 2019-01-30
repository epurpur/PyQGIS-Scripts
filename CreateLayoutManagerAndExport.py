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
map = QgsLayoutItemMap(layout)                              #creates map item
map.setRect(20, 20, 20, 20)                                 #must setRect() but arguments don't seem to do anything
rectangle = QgsRectangle(1355502, -46398, 1734534, 137094)  #create rectangle with extent of stuff I want to map (coordinates)
map.setExtent(rectangle)
#canvas = iface.mapCanvas()                                 #creates Canvas object using reference to iface
#map.setExtent(canvas.extent())                             #set extent as the canvas, which is the current extent of the map canvas (zoom in or out)
layout.addLayoutItem(map)
map.attemptMove(QgsLayoutPoint(0.25, 0.25, QgsUnitTypes.LayoutInches))          #moves map object box
map.attemptResize(QgsLayoutSize(250, 200, QgsUnitTypes.LayoutMillimeters))      #resizes map object box

"""This adds a legend item to the Print Layout"""
legend = QgsLayoutItemLegend(layout)
layout.addLayoutItem(legend)
legend.attemptMove(QgsLayoutPoint(250, 0, QgsUnitTypes.LayoutMillimeters))


"""This exports a Print Layout as an image"""
manager = QgsProject.instance().layoutManager()     #this is a reference to the layout Manager, which contains a list of print layouts
for layout in manager.printLayouts():               #this prints all existing print layouts in a list
    print(layout.name())

layout = manager.layoutByName("Console4")         #this accesses a specific layout, by name (which is a string)

exporter = QgsLayoutExporter(layout)                #this creates a QgsLayoutExporter object
exporter.exportToPdf('/Users/ep9k/Desktop/TestLayout.pdf', QgsLayoutExporter.PdfExportSettings())      #this exports a pdf of the layout object
#exporter.exportToImage('/Users/ep9k/Desktop/TestLayout.png', QgsLayoutExporter.ImageExportSettings())  #this exports an image of the layout object


