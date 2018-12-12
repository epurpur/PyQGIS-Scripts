from PyQt5.QtGui import QColor
from PyQt5.QtCore import QVariant
from qgis.PyQt.QtCore import QVariant

#sets uri, join_layer and target_field as global variables
uri = '/Users/ep9k/Desktop/SandraMonson/cb_2017_us_zcta510_500k/cb_2017_us_zcta510_500k.shp'

join_layer = iface.addVectorLayer(uri, 'Patients by Zip Code', 'ogr')
target_field = 'PatCNT'

def add_csv():
    """Adds csv file of patient data to map. Pop-up dialog box prompts user to input file path
    QInputDialog prompts user for file name. User must input path to a CSV file"""

    file_name = QInputDialog.getText(None, 'Enter input filepath to csv file', 'Please save patient data as csv and paste full pathname here. (Example: /Users/ep9k/Desktop/SandraMonson/TestZips.csv)')
    file_name = file_name[0]        #QInputDialog returns a tuple, this is first object of tuple, which is a string of the file name

    uri = f"file://{file_name}?delimiter=,'"    #needs file:// before path to csv. I don't know why.
    
    info_layer = QgsVectorLayer(uri, 'Patient_Data', 'delimitedtext')
    if info_layer.isValid():
        print("info_layer is valid. Adding csv to map")
        QgsProject.instance().addMapLayer(info_layer)       #adds csv table to layer panel
    else:
        print("Invalid csv file. Please check your file path. (uri variable)")

    return info_layer               #returns info layer, which is the csv file


def join_tables(join_layer, info_layer):
    """Joins attributes tables of join_layer and info_layer
    join_layer is US zip codes layer
    info_layer is csv file with patient data"""
    QgsProject.instance().addMapLayer(join_layer)
    
    csvField = 'ZipCode'
    shpField = 'GEOID10'
    joinObject = QgsVectorLayerJoinInfo()
    joinObject.setJoinFieldName(csvField)           #sets name of column for csvField, which is 'ZipCode' column from attribute table of csv file
    joinObject.setTargetFieldName(shpField)         #sets name of column for shpField, which is 'GEOID10' column from attribute table of zipcode layer
    joinObject.setJoinLayerId(info_layer.id())
    joinObject.setUsingMemoryCache(True)
    joinObject.setJoinLayer(info_layer)
    join_layer.addJoin(joinObject)
    
    print("Tables joined")
    

def add_column_to_attribute_table():
    """Adds new column to attribute table of join_layer.
    Then computes column (copies PatientCount field as numeric value)"""
    
    caps = join_layer.dataProvider().capabilities()         #checks capabilities of join_layer. Can also print all capabilities
    if caps & QgsVectorDataProvider.AddAttributes:          #if AddAttributes is a capability
        join_layer.dataProvider().addAttributes([QgsField('PatCNT', QVariant.Int)])        #Adds PatCNT as new column to attribute table of join_layer QVariant.Int is type for new column
    print("New Column added to attribute table")


def calculate_attributes():
    """Calculates values for 'PatCNT' by copying attributes from Patient_Data_PatientCount
    and adds them to 'PatCNT' column in US Zip Codes table"""

    with edit(join_layer):
        for feature in join_layer.getFeatures():
            feature.setAttribute(feature.fieldNameIndex('PatCNT'), feature['Patient_Data_PatientCount'])
            join_layer.updateFeature(feature)
    print(f"Attribute calculated for {target_field} field")


def apply_graduated_symbology():
    """Creates Symbology for each value in range of values. 
        Values are # of patients per zip code.
        Hard codes min value, max value, symbol (color), and label for each range of values.
        Then QgsSymbolRenderer takes field from attribute table and item from myRangeList and applies them to join_layer.
        Color values are hex codes, in a graduated fashion from light pink to black depending on intensity"""
    myRangeList = []

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())     #symbol stores a symbol for the geometry type of this layer, which is a polygon
    symbol.setColor(QColor("#f5c9c9"))                              #sets Color for this symbol
    myRange = QgsRendererRange(0, 2, symbol, '2 or fewer')                   #QgsRendererRange is used to define values for a range of values. Arguments are (min value, max value, color, label)
    myRangeList.append(myRange)                                     #appends this range of values to myRangeList

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#f97a7a"))
    myRange = QgsRendererRange(2.1, 4, symbol, '3-4')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#ff0000"))
    myRange = QgsRendererRange(4.1, 6, symbol, '5-6')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#8a0000"))
    myRange = QgsRendererRange(5.1, 7, symbol, '6-7')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#4a0000"))
    myRange = QgsRendererRange(7.1, 9, symbol, '8-9')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(join_layer.geometryType())
    symbol.setColor(QColor("#000000"))
    myRange = QgsRendererRange(9.1, 100, symbol, '10 or more')
    myRangeList.append(myRange)

    myRenderer = QgsGraduatedSymbolRenderer(target_field, myRangeList)  #reads target_field and uses values from myRangeList to populate those values in myRenderer
    myRenderer.setMode(QgsGraduatedSymbolRenderer.Custom)               #sets this mode to Custom, because I have defined custom values

    join_layer.setRenderer(myRenderer)                                  #applies the rendering to join_layer
    
    print(f"Graduated color scheme applied")


def main_module():
    """main module which runs all steps in script"""
    info_layer = add_csv()
    join_tables(join_layer, info_layer)     #join_layer is global variable
    add_column_to_attribute_table()
    calculate_attributes()
    apply_graduated_symbology()
    print("All operations finished")

main_module()
