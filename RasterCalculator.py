# In raster calculator, expression is:  ( "AestheticMax@1" != 255) * "AestheticMax@1"
import processing

#processing.algorithmHelp('gdal:rastercalculator')  #for help docs

input_raster = QgsRasterLayer('/Users/ep9k/Desktop/Key-LogEcovaluator/Rasters/AestheticMax.tif', 'raster')
output_raster = '/Users/ep9k/Desktop/reclassoutput.tif'


parameters = {'INPUT_A' : input_raster,
            'BAND_A' : 1,
            'FORMULA' : '(A != 255) * A',
            'OUTPUT' : output_raster}

processing.runAndLoadResults('gdal:rastercalculator', parameters)
