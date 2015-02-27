# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 09:20:10 2015
Created by Ziqi
Get XYZ Table Summary for IDW_Interpolated
@author: Ziqi
"""

"""
Created by Ziqi
Get XYZ Table Summary

"""
import arcpy
import os.path
import numpy
#numpy.set_printoptions(threshold=numpy.inf)
arcpy.CheckOutExtension("Spatial")
from arcpy.sa import *
from arcpy import env

workpath =  r"F:\Nor_100_IDWed"
arcpy.env.workspace = workpath
array = []
first = True

index = 0
rasters = arcpy.ListRasters()
for raster in rasters:
    if first:
        description = arcpy.Describe(raster)
        spatialRef = description.SpatialReference
        ext= description.Extent
        lowerLeft = arcpy.Point(ext.XMin,ext.YMin)
        x = description.width
        y = description.height
        first = False
    array.append(arcpy.RasterToNumPyArray(raster))
    index = index + 1


print x, y 
array = numpy.array(array)
print array.shape

ndArray=array

ndArray[ndArray==0.0]=numpy.nan



x_list=[]
y_list=[]
for i in range(0,x):
    for j in range(0,y):
        x_list.append(i)
        y_list.append(j)


x_list = numpy.array(x_list)
y_list = numpy.array(y_list)
print x_list.shape
print y_list.shape

reshapedArray=ndArray.copy()
reshapedArray = numpy.reshape(reshapedArray,(120,10000), order='C')
print reshapedArray.shape

aa = numpy.vstack((x_list,y_list,reshapedArray))
print aa.shape
aa.transpose()
print aa.shape

numpy.savetxt(r"C:\Users\Ziqi\Desktop\MODI_Matrix_IDWed.csv", aa, delimiter=",",fmt='%.2f')
print "done!"
