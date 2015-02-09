# -*- coding: utf-8 -*-
"""
@author: Ziqi
For IDW Interpolation
"""

import arcpy
arcpy.CheckOutExtension("Spatial")
arcpy.CheckOutExtension("3D")
arcpy.env.overwriteOutput = True

workpath =  r"F:\Nor_100X100"
arcpy.env.workspace = workpath
outPoint = r"C:\Users\Ziqi\Documents\ArcGIS\Default.gdb\temp"
#%%
year = 2002
month = 1
rasters = arcpy.ListRasters()
for raster in rasters:
    print year
    print month
    
    arcpy.RasterToPoint_conversion(raster, outPoint, "VALUE")
    outRaster =  r"F:\Nor_100_IDWed\LST_"+ str(year) +'_'+ str(month).zfill(2) + "_IDW.tif"
    cellSize = 1000
    power = 2
    searchRadius = 8
    arcpy.Idw_3d(outPoint, "grid_code",outRaster,cellSize,power,searchRadius)
    arcpy.DeleteFeatures_management(outPoint)
    month = month+1
    if month > 12:
        year = year+1
        month=1
        