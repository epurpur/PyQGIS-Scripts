
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from qgis.utils import iface

"""
#TODO: add csv file with patient data to map

uri = 'file:///Users/ep9k/Desktop/SandraMonson/CountByZip.csv?delimiter=,'
csv_file = QgsVectorLayer(uri, 'Patient Data', 'delimitedtext')
QgsProject.instance().addMapLayer(csv_file)
"""



#TODO: add csv file of patient data
join_layer = QgsVectorLayer('/Users/ep9k/Desktop/SandraMonson/cb_2017_us_zcta510_500k/cb_2017_us_zcta510_500k.shp', 'US Zip Codes', 'ogr')
if join_layer.isValid():
    print("join_layer is valid")
    uri = 'file:///Users/ep9k/Desktop/SandraMonson/CountByZip.csv?delimiter=,'      #don't know why, but it needs file:/// before path to csv
#    Also this is correct path to add csv to map
    info_layer = QgsVectorLayer(uri, 'Patient_Data', 'delimitedtext')
    if info_layer.isValid():
        print("info_layer is valid")
        QgsProject.instance().addMapLayer(join_layer)
#        QgsProject.instance().addMapLayer(info_layer)
        csvField = 'ZipCode'
        shpField = 'GEOID10'
        joinObject=QgsVectorLayerJoinInfo()
        joinObject.setJoinFieldName(csvField)
        joinObject.setTargetFieldName(shpField)
        joinObject.setJoinLayerId(info_layer.id())
        joinObject.setUsingMemoryCache(True)
        joinObject.setJoinLayer(info_layer)
        join_layer.addJoin(joinObject)





