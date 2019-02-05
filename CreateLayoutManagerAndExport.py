import numpy            #using percentile function when calculating raster pixel value range


"""This creates a new print layout"""
project = QgsProject.instance()             #gets a reference to the project instance
#projectInstance = QgsProject()                     #reference to project, but not the instance. Doesn't add new layout to Layout Manager. Do I need a reference to the instance?
manager = project.layoutManager()           #gets a reference to the layout manager
layout = QgsPrintLayout(project)            #makes a new print layout object, takes a QgsProject as argument
layout.initializeDefaults()                         #needs to call this according to documentation
layoutName = "PrintLayout2"
layout.setName(layoutName)                           #lets you choose a name for the layout
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



"""Gathers active layers to add to legend"""
#Checks layer tree objects and stores them in a list. This includes csv tables
checked_layers = [layer.name() for layer in QgsProject().instance().layerTreeRoot().children() if layer.isVisible()]
print(f"Adding {checked_layers}" )
#get map layer objects of checked layers by matching their names and store those in a list
layersToAdd = [layer for layer in QgsProject().instance().mapLayers().values() if layer.name() in checked_layers]



"""This adds a legend item to the Print Layout"""
legend = QgsLayoutItemLegend(layout)
#legend.setTitle("Legend")
root = QgsLayerTree()
for layer in layersToAdd:
    #add layer objects to the layer tree
    root.addLayer(layer)
legend.model().setRootGroup(root)
layout.addLayoutItem(legend)
legend.attemptMove(QgsLayoutPoint(246, 5, QgsUnitTypes.LayoutMillimeters))



"""This symbolizes raster layer in legend"""
#defining raster layer to work with (active layer in layer panel)
layer = iface.activeLayer()
print("Active Layer: ", layer.name())
provider = layer.dataProvider()
extent = layer.extent()
#Using RasterBandStats to find range of values in raster layer
stats = provider.bandStatistics(1, QgsRasterBandStats.All) 
min_val = stats.minimumValue            #minimum pixel value in layer
max_val = stats.maximumValue            #maximum pixel value in layer
print("min value =", min_val)
print("max value =", max_val)

value_range = range(int(min_val), int(max_val+1))           #Range of values in raster layer. Without +1 doesn't capture highest value

#we will categorize pixel values into 5 quintiles, based on value_range of raster layer
#defining min and max values for each quintile. 
first_quintile_max = numpy.percentile(value_range, 20)
first_quintile_min = min_val
second_quintile_max = numpy.percentile(value_range, 40)
second_quintile_min = first_quintile_max + .01
third_quintile_max = numpy.percentile(value_range, 60)
third_quintile_min = second_quintile_max + .01
fourth_quintile_max = numpy.percentile(value_range, 80)
fourth_quintile_min = third_quintile_max + .01
fifth_quintile_max = numpy.percentile(value_range, 100)
fifth_quintile_min = fourth_quintile_max + .01


#builds raster shader with colors_list. 
raster_shader = QgsColorRampShader()
raster_shader.setColorRampType(QgsColorRampShader.Discrete)           #Shading raster layer with QgsColorRampShader.Discrete
colors_list = [ QgsColorRampShader.ColorRampItem(first_quintile_max, QColor(219, 230, 255), f"{first_quintile_min} - {first_quintile_max}"), \
    QgsColorRampShader.ColorRampItem(second_quintile_max, QColor(183, 204, 255), f"{second_quintile_min} - {second_quintile_max}"), \
    QgsColorRampShader.ColorRampItem(third_quintile_max, QColor(147, 180, 255), f"{third_quintile_min} - {third_quintile_max}"), \
    QgsColorRampShader.ColorRampItem(fourth_quintile_max, QColor(111, 154, 255), f"{fourth_quintile_min} - {fourth_quintile_max}"), \
    QgsColorRampShader.ColorRampItem(fifth_quintile_max, QColor(75, 130, 255), f"{fifth_quintile_min} - {fifth_quintile_max}"), \
    QgsColorRampShader.ColorRampItem(255, QColor(0, 0, 0), 'Missing Value') ]

raster_shader.setColorRampItemList(colors_list)         #applies colors_list to raster_shader
shader = QgsRasterShader()
shader.setRasterShaderFunction(raster_shader)       

renderer = QgsSingleBandPseudoColorRenderer(layer.dataProvider(), 1, shader)    #renders selected raster layer
layer.setRenderer(renderer)
layer.triggerRepaint()



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

layout = manager.layoutByName(layoutName)         #this accesses a specific layout, by name (which is a string)

exporter = QgsLayoutExporter(layout)                #this creates a QgsLayoutExporter object
exporter.exportToPdf('/Users/ep9k/Desktop/TestLayout.pdf', QgsLayoutExporter.PdfExportSettings())      #this exports a pdf of the layout object
#exporter.exportToImage('/Users/ep9k/Desktop/TestLayout.png', QgsLayoutExporter.ImageExportSettings())  #this exports an image of the layout object


