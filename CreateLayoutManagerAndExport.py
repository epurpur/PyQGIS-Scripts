
"""This creates a new print layout"""
project = QgsProject.instance()             #gets a reference to the project instance
#projectInstance = QgsProject()                     #reference to project, but not the instance. Doesn't add new layout to Layout Manager. Do I need a reference to the instance?
manager = project.layoutManager()           #gets a reference to the layout manager
layout = QgsPrintLayout(project)            #makes a new print layout object, takes a QgsProject as argument
layout.initializeDefaults()                         #needs to call this according to documentation
layout.setName('Console2')                           #lets you choose a name for the layout
manager.addLayout(layout)                           #adds layout to manager




#"""This exports a Print Layout as an image"""
#manager = QgsProject.instance().layoutManager()     #this is a reference to the layout Manager, which contains a list of print layouts
#for layout in manager.printLayouts():               #this prints all existing print layouts in a list
#    print(layout.name())
#
#layout = manager.layoutByName("Console2")         #this accesses a specific layout, by name (which is a string)
#
#exporter = QgsLayoutExporter(layout)                #this creates a QgsLayoutExporter object
##exporter.exportToPdf('/Users/ep9k/Desktop/TestLayout.pdf', QgsLayoutExporter.PdfExportSettings())      #this exports a pdf of the layout object
##exporter.exportToImage('/Users/ep9k/Desktop/TestLayout.png', QgsLayoutExporter.ImageExportSettings())  #this exports an image of the layout object


