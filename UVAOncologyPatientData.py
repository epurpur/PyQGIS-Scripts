from PyQt5.QtGui import QColor
from PyQt5.QtCore import QVariant
from qgis.PyQt.QtCore import QVariant


uri = '/Users/ep9k/Desktop/SandraMonson/cb_2017_us_zcta510_500k/cb_2017_us_zcta510_500k.shp'
join_layer = iface.addVectorLayer(uri, 'Patients by Zip Code', 'ogr')
target_field = 'PatCNT'

def add_csv():
    """Adds csv file of patient data to map. Pop-up dialog box prompts user to input file path
    QInputDialog prompts user for file name"""

    file_name = QInputDialog.getText(None, 'Enter input filepath to csv file', 'Please save patient data as csv and paste full pathname here. (Example: /Users/ep9k/Desktop/SandraMonson/TestZips.csv)')
    file_name = file_name[0]        #QInputDialog returns a tuple, this is first object of tuple, which is a string of the file name

    uri = f"file://{file_name}?delimiter=,'"    #needs file:// before path to csv  
    
    info_layer = QgsVectorLayer(uri, 'Patient_Data', 'delimitedtext')
    if info_layer.isValid():
        print("info_layer is valid. Adding csv to map")
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
    joinObject = QgsVectorLayerJoinInfo()
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


def apply_graduated_symbology():
    """Creates Symbology for each value in range of values. 
        Values are # of patients per zip code.
        Hard codes min value, max value, symbol (color), and label for each range of values.
        Then QgsSymbolRenderer takes field from attribute table and item from myRangeList and applies them to join_layer"""
    myRangeList = []

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#f5c9c9"))
    myRange = QgsRendererRange(0, 1, symbol, '1')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#f97a7a"))
    myRange = QgsRendererRange(1.1, 2, symbol, '2')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#ff0000"))
    myRange = QgsRendererRange(2.1, 3, symbol, '3')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#8a0000"))
    myRange = QgsRendererRange(3.1, 4, symbol, '4')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#4a0000"))
    myRange = QgsRendererRange(4.1, 5, symbol, '5')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#000000"))
    myRange = QgsRendererRange(5.1, 6, symbol, '6 or more patients')
    myRangeList.append(myRange)

    myRenderer = QgsGraduatedSymbolRenderer(target_field, myRangeList)
    myRenderer.setMode(QgsGraduatedSymbolRenderer.Custom)

    join_layer.setRenderer(myRenderer)


def main_module():
    """main module which runs all steps in script"""
    info_layer = add_csv()
    join_tables(join_layer, info_layer)
    add_column_to_attribute_table()
    calculate_attributes()
    apply_graduated_symbology()


main_module()
