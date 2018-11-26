
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QVariant
from qgis.PyQt.QtCore import QVariant
#from PyQt5.QtCore import Qt
#from qgis.utils import iface

#join_layer = QgsVectorLayer('/Users/ep9k/Desktop/SandraMonson/cb_2017_us_zcta510_500k/cb_2017_us_zcta510_500k.shp', 'US Zip Codes', 'ogr')
uri = '/Users/ep9k/Desktop/SandraMonson/cb_2017_us_zcta510_500k/cb_2017_us_zcta510_500k.shp'
join_layer = iface.addVectorLayer(uri, 'Zip Codez', 'ogr')

def add_base_layers():
    #Do I really need this function? I'll probably just save a plain map with standard layers already added
    #standard layers include: basemap, US Zip codes, cville boundary, cville buffers (30,60miles)
    pass

def add_csv():
    """Adds csv file. Will later be specified as user input"""
    #TODO: Specify csv file based on user input
    
    uri = 'file:///Users/ep9k/Desktop/SandraMonson/CountByZip2.csv?delimiter=,'      #don't know why, but it needs file:/// before path to csv
    info_layer = QgsVectorLayer(uri, 'Patient_Data', 'delimitedtext')
    if info_layer.isValid():
        print("info_layer is valid")
        QgsProject.instance().addMapLayer(info_layer)
    else:
        print("Invalid csv file. Please check your file path. (uri variable)")
        
    return info_layer


def join_tables(join_layer, info_layer):
    """Joins attributes tables of join_layer and info_layer
    join_layer is US zip codes layer
    info_layer is csv file with patient data"""
    QgsProject.instance().addMapLayer(join_layer)
    
    csvField = 'ZipCode'
    shpField = 'GEOID10'
    joinObject=QgsVectorLayerJoinInfo()
    joinObject.setJoinFieldName(csvField)
    joinObject.setTargetFieldName(shpField)
    joinObject.setJoinLayerId(info_layer.id())
    joinObject.setUsingMemoryCache(True)
    joinObject.setJoinLayer(info_layer)
    join_layer.addJoin(joinObject)
    

def add_column_to_attribute_table():
    """Adds new column to attribute table of join_layer.
    Then computes column (copies PatientCount field as numeric value)"""
    
    caps = join_layer.dataProvider().capabilities()         #checks capabilities of join_layer. Can also print all capabilities
    if caps & QgsVectorDataProvider.AddAttributes:
        join_layer.dataProvider().addAttributes([QgsField('PatCNT', QVariant.Int)])        #QVariant.Int is type for new column


def calculate_attributes():
    """Copies attributes from Patient_Data_PatientCount and adds them to 'PatCNT' layer in US Zip Codes table"""

    with edit(join_layer):
        for feature in join_layer.getFeatures():
            feature.setAttribute(feature.fieldNameIndex('PatCNT'), feature['Patient_Data_PatientCount'])
            join_layer.updateFeature(feature)

def change_color():
    """Changes symbology of zip codes. Currently single symbol. Will be graduated based on PatCNT in future"""
    
    renderer = join_layer.renderer()
    symbol = renderer.symbol()
    symbol.setColor(QColor(Qt.black))
    join_layer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(join_layer.id())


def main_module():
    """main module which runs all steps in script"""
    info_layer = add_csv()
    join_tables(join_layer, info_layer)
    add_column_to_attribute_table()
    calculate_attributes()
    change_color()

main_module()



