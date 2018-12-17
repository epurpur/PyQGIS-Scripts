"""This script takes data from QGISweather_app_main (which is stored in temp.csv) and applies a categorized color symbology to the map.
Basically, it reads the zip codes from temp.csv and joins them to the ZipCodesWithClimbing shapefile. Then represents the 
'Climbing Area Conditions Data_Rank' column of the attribute table to show either the 'best' conditions or 'other' conditions today.

***Note - State must have zip codes in ClimbingAreasInfo csv file or will not be represented in the final output"""


from PyQt5.QtGui import QColor
from PyQt5.QtCore import QVariant
from qgis.PyQt.QtCore import QVariant

#sets uri, join_layer and target_field as global variables
uri = '/Users/ep9k/Desktop/ClimbingWeatherApp-QGIS/Shapefiles/ZipCodesWithClimbing.shp'

join_layer = iface.addVectorLayer(uri, 'US Zip Codes', 'ogr')


def read_temp_csv():
    """Reads temp.csv, which contains weather info by zip code for chosen state. Adds it to map"""
    uri = "file:///Users/ep9k/Desktop/ClimbingWeatherApp-QGIS/temp.csv?delimiter=,'"
    
    info_layer = QgsVectorLayer(uri, 'Climbing Area Conditions Data', 'delimitedtext')
    if info_layer.isValid():
        print("info_layer is valid. Adding csv to map")
        QgsProject.instance().addMapLayer(info_layer)
    else:
        print("Invalid csv file. please check your file path (uri variable)")
        
    return info_layer
    

def join_tables(info_layer):
    """joins temp.csv to zip codes layer based on zip code column in attribute table
    join_layer is US zip codes layer, which is a global variable.
    info_layer is csv file with conditions data for each climbing location"""
    QgsProject.instance().addMapLayer(join_layer)
    
    csvField = 'Zip_codes'      #this is zip codes column in attribute table of info_layer
    shpField = 'GEOID10'        #this is zip codes column in attribute table of join_layer
    joinObject = QgsVectorLayerJoinInfo()
    joinObject.setJoinFieldName(csvField)           #sets name of column for csvField, which is 'Zip Codes' column from attribute table of csv file
    joinObject.setTargetFieldName(shpField)         #sets name of column for shpField, which is 'GEOID10' column from attribute table of zip code layer
    joinObject.setJoinLayerId(info_layer.id())
    joinObject.setUsingMemoryCache(True)
    joinObject.setJoinLayer(info_layer)
    join_layer.addJoin(joinObject)
    
    print("Tables joined")

    
def apply_categorized_symbology():
    """this will take zip codes layer afer temp_csv is joined and creates a categorized symbology based on the 'Climbing Area Conditions Data_Rank' field in the attribute table
    Because there is only one "best conditions" for the day, the rank for each location are either "best" or "other". I hard coded these."""
    
    categories_list = []
    target_field = 'Climbing Area Conditions Data_Rank'
    
    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#f28500"))
    my_category = QgsRendererCategory('best', symbol, 'Best Conditions')
    categories_list.append(my_category)
    
    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#8a0000"))
    my_category = QgsRendererCategory('other', symbol, 'Suboptimal Conditions')
    categories_list.append(my_category)
    
    my_renderer = QgsCategorizedSymbolRenderer(target_field, categories_list)
    
    join_layer.setRenderer(my_renderer)
    
    print("Categorized color scheme applied")
    
    
def main():
    """this main module runs other functions in script"""
    info_layer = read_temp_csv()
    join_tables(info_layer)
    apply_categorized_symbology()
    

main()