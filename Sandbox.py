
#This creates a new print layout
project = QgsProject.instance()                    
manager = project.layoutManager()
layout = QgsPrintLayout(project)
layout.initializeDefaults()                         
layout.setName('My Layout6')                           
manager.addLayout(layout) 

map = QgsLayoutItemMap(layout)

#sets initial position on the page
map.attemptSetSceneRect(QRectF(0, 0, 100, 100))

#sets size for the image
map.attemptResize(QgsLayoutSize(6, 5, QgsUnitTypes.LayoutInches))

#set extent of map
rectangle = QgsRectangle(-1350312, -21811, 1741463, 116086)
map.setExtent(rectangle)

layout.addLayoutItem(map)