"""script for running GRASS v.surf.idw tool"""

import processing

parameters = {
    'input' : '/Users/ep9k/Desktop/qgis_data-master/area3_testdata_clipped.shp',
    'npoints' : 12,
    'power' : 2,
    'column' : 'PDOP',
    'GRASS_REGION_PARAMETER' : '-116.04415744105579,-116.0047567429083,37.029018114312905,37.054281406967974 [EPSG:4326]',
    'GRASS_REGION_CELLSIZE_PARAMETER' : 0,
    'GRASS_RASTER_FORMAT_OPT' : '',
    'GRASS_RASTER_FORMAT_META' : '',
    'GRASS_SNAP_TOLERANCE_PARAMETER' : -1,
    'GRASS_MIN_AREA_PARAMETER' : 0.0001,
    'output' : '/Users/ep9k/Desktop/GRASS_OUTPUT.tif'}

processing.runAndLoadResults('grass7:v.surf.idw', parameters)
    