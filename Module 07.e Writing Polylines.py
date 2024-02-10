"""
Jonathan Leonard                                           NRE 5585 Python Scripting for Geospatial Analysis
Week 7 e Writing polylines                                 18OCT2021
"""

"""
In this exercise we will be creating polyline features using the eop_grouped.shp feature class as input.
"""

## INITIALIZE YOUR SCRIPT WITH IMPORTS, DRIVE LETTER, PATHS, ETC.
print('Initializing...')
import arcpy
import numpy as np
import os
dl = 'C:/'
data_path = 'NRE_5585/Data/'
temp_path = 'NRE_5585/Temp/'
res_path = 'NRE_5585/Results/'
arcpy.env.workspace = dl + res_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')
from lib5585 import *

"""
Create a POLYLINE feature class named curbs_grouped.shp in your results directory. Set 
the spatial reference to SPC83 Connecticut (meters) 0600, then add a TEXT field to the
attribute table named 'ROAD'
"""

## see previous assignment for a code template. Just change MULTIPOINT to POLYLINE
SPC = 6433
res = dl+res_path
curbs = "curbs_grouped.SHP"
arcpy.management.CreateFeatureclass(res, curbs, 'POLYLINE', spatial_reference=SPC)
curbs = res+'curbs_grouped.shp'
arcpy.management.AddField(curbs, 'ROAD', 'TEXT')
print("\nField 'ROAD' created for curbs_grouped.shp")

"""
Now we do the multi-level groupings using the multipoint feature class created in the last assignment
"""
## Create an empty dictionary to hold the groups

roads = {}
eop = dl + temp_path + 'eop_grouped.SHP'
## Create a search cursor on eop_grouped.shp with 'SHAPE@','road','group' for the attribute list
with arcpy.da.SearchCursor(eop, ['SHAPE@', 'group', 'road']) as sc:
    ## for each row in the cursor
    for row in sc:

        ## assign the contents of the row to variables
        mp = row[0]
        road_nm = row[-1]
        #mp, road_nm, group = row
        group = row[1]
        ## if the road name isn't in the dictionary, associate an empty list with it
        if road_nm not in roads:
            roads[road_nm] = []
        ## get the Array of Points in mp by calling the getPart() method on the multipoint object
        parts = mp.getPart()

        ## create an empty list to hold the Points in mp
        #point_lst =
        # for each point in points..
        for point in parts:
            x, y = point.X, point.Y
            ## append the point to point_lst
            roads[road_nm].append([x, y])

        ## append the point_lst to list associated with road_nm
#       roads[road_nm].append(point_lst)
## Create an insert cursor on the new feature class with 'SHAPE@','road' for the attribute list

with arcpy.da.InsertCursor(curbs, ['SHAPE@', 'road']) as ic:
    ## for each road in roads...
    for road_nm in roads:
        ## assign the list in roads[road] to a local variable
        point_lst = roads[road_nm]
        ## create an arcpy.Array from point_lst
        array = arcpy.Array()
        for point in point_lst:
            pnt = arcpy.Point(point[0], point[1])
            array.add(pnt)
        ## create an arcpy.Polyline object from array
        poly = arcpy.Polyline(array)
        ## insert the polyline into the feature class using the insertRow method of the insert cursor
        ic.insertRow([poly, road_nm])

## submit this script, the feature class you created, and a screen shot of it in ArcPro
print("\nFinished! Alert UConn's Department of NRE!!")