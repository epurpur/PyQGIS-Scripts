import processing
from qgis.core import *

raster_layer = QgsRasterLayer('/Users/ep9k/Desktop/Key-LogEcovaluator/Rasters/AestheticMax.tif', 'raster')
mask_layer = QgsVectorLayer('/Users/ep9k/Desktop/Key-LogEcovaluator/TestVectorExtent.shp', 'mask', 'ogr')

parameters = {'INPUT': raster_layer,
                'MASK': mask_layer,
                'NODATA': -9999,
                'ALPHA_BAND': False,
                'CROP_TO_CUTLINE': True,
                'KEEP_RESOLUTION': True,
                'OPTIONS': None,
                'DATA_TYPE': 0,
                'OUTPUT': '/Users/ep9k/Desktop/output_clip.tif'}

processing.runAndLoadResults('gdal:cliprasterbymasklayer', parameters)

#print(processing.algorithmHelp('gdal:cliprasterbymasklayer'))  #prints info about parameters
