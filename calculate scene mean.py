# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 20:48:01 2014

@author: Ziqi
"""
import arcpy

workpath = r"R:\Shiklomanov Research\Ziqi-Norilsk\New_Clipped2"
arcpy.env.workspace = workpath
arcpy.env.overwriteOutput = True

max_value = 0
min_value = 99999
mean = []
rasters = arcpy.ListRasters("*","TIF")
for raster in rasters:
    print rasters
    max_val_tmp = float(arcpy.GetRasterProperties_management(raster, "MAXIMUM").getOutput(0))
    min_val_tmp = float(arcpy.GetRasterProperties_management(raster, "MINIMUM").getOutput(0))
    mean_val_tmp = float(arcpy.GetRasterProperties_management(raster, "MEAN").getOutput(0))
    if max_val_tmp > max_value:
         max_value = max_val_tmp
    if min_val_tmp < min_value:
         min_value = min_val_tmp
    mean.append(mean_val_tmp)
print max_value
print min_value
print mean
print "done!"