# run r.param.scale
input_elevation_layer = '/Users/ep9k/Desktop/GRASS_TEST/elevation_export.tif'
processing.run("grass7:r.param.scale", {'input': input_elevation_layer,'slope_tolerance':1,'curvature_tolerance':0.0001,'size':33,'method':0,'exponent':0,'zscale':1,'-c':False,'output':'/Users/ep9k/Desktop/GRASS_TEST/geomorphic_parameters.tif','GRASS_REGION_PARAMETER':None,'GRASS_REGION_CELLSIZE_PARAMETER':0,'GRASS_RASTER_FORMAT_OPT':'','GRASS_RASTER_FORMAT_META':''})

# run r.geomorphon
geomorphic_parameters = '/Users/ep9k/Desktop/GRASS_TEST/geomorphic_parameters.tif'
processing.run("grass7:r.geomorphon", {'elevation': geomorphic_parameters,'search':3,'skip':0,'flat':1,'dist':0,'forms':'/Users/ep9k/Desktop/GRASS_TEST/geomorphic_output.tif','-m':False,'-e':False,'GRASS_REGION_PARAMETER':None,'GRASS_REGION_CELLSIZE_PARAMETER':0,'GRASS_RASTER_FORMAT_OPT':'','GRASS_RASTER_FORMAT_META':''})
