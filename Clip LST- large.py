# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 20:48:01 2014

@author: Ziqi
@use: Clip LST based on Landsat extent

"""

import arcpy
import os
workpath = r'R:\Shiklomanov Research\Waterloo LST\Nor_dud_iga_2002_2011'
clipTo = r'C:\Users\ZLi4\Documents\ArcGIS\Default.gdb\landsatDomain2'
arcpy.env.workspace = workpath
arcpy.env.overwriteOutput = True
arcpy.env.extent = clipTo



month = ['01','10','11','12','02','03','04','05','06','07','08','09']

year = 2002
folders = arcpy.ListFiles()
for folder in folders:
    current_wsp = os.path.join(workpath,folder)
    arcpy.env.workspace = current_wsp
    rasters = arcpy.ListRasters("*","TIF")
    i = 1
    j = 0
    for raster in rasters:
        #get the first band
        if i%7 == 3:
            print raster
            #print "R:\Shiklomanov Research\Ziqi-Norilsk\New_Clipped\LST_"+ str(year) +'_'+ month[j] + ".tif"
            arcpy.Clip_management(raster, "#", r"R:\Shiklomanov Research\Ziqi-Norilsk\New_Clipped_Day\LST_"+ str(year) +'_'+ month[j] + ".tif",clipTo, "0", "ClippingGeometry")
            j = j + 1
        i = i + 1
    year = year + 1
print "done!"