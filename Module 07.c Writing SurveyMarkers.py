"""
Jonathan Leonard                                           NRE 5585 Python Scripting for Geospatial Analysis
Week 7 c Writing survey markers                            16OCT2021
"""

## INITIALIZE YOUR SCRIPT WITH IMPORTS, DRIVE LETTER, PATHS, ETC.
##
## SET THE WORKSPACE TO THE TEMP DIRECTORY
print('Initializing...')
import arcpy
import os
import numpy as np
dl = "C:/"
data_path = "NRE_5585/data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.workspace = dl + temp_path
arcpy.env.overwriteOutput = True

# import your lib5585 module
from lib5585 import *
print('Ready to go!\n')

## Download storrs_markers.csv. Open it in Excel or similar and examine its contents.
'''
The columns have the these meanings:
PID: str = permanent identifier code
DESIG: str = the 'common name' of this marker

LATD: int = latitude degrees
LATM: int = latitude minutes
LATS: float = latitude seconds
LATH: int = hemisphere code where 1 is for northern latitudes and -1 is for southern latitudes

LOND: int = longitude degrees
LONM: int = longitude minutes
LONS: float = longitude seconds
LONH: int = hemisphere code where 1 is for eastern longitudes and -1 is for western longitudes
'''

fn = 'survey_markers.shp'
outpath = dl + temp_path

# Create a point feature class in your TEMP directory named survey_markers.shp referred to NAD83(2011) WKID= 6318
WKID = 6318 # SPC 83 CT (meters)
arcpy.management.CreateFeatureclass(outpath, fn, "POINT", spatial_reference=WKID)

# Add a column for PID
arcpy.management.AddField(fn, 'PID', 'TEXT')

# Add a column for DESIG
arcpy.management.AddField(fn, 'DESIG', 'TEXT')

# Create an insert cursor for survey_markers.shp with field list [SHAPE@', PID, Desig]
count = 0
with arcpy.da.InsertCursor(fn, ['SHAPE@', 'PID', 'DESIG']) as ic:

    # Open storrs_markers.csv in read-only mode
    storrs_markers = open(dl + data_path + 'storrs_markers.csv', "r")

        # for each line in storrs_markers.csv
    for line in storrs_markers:

            # split the line apart on commas
        values = line[:-1].split(',')
        print(values)
            # skip the header line

        if count == 0:    # can't use not is numeric
            count = count + 1
            continue

        # assign each element in parts to a variable, and cast them to the proper types
        PID = str(values[0])
        DESIG = str(values[1])
        LATD = int(values[2])
        LATM = int(values[3])
        LATS = float(values[4])
        LATH = int(values[5])
        LOND = int(values[6])
        LONM = int(values[7])
        LONS = float(values[8])
        LONH = int(values[9])

        # lib5585.from_dmss() takes a list [d, m, s, h] as its first argument and
            # a string as its second argument. The list holds degrees, minutes, second, hemisphere-code.
            # The string is either 'radians' or 'DD'.
            # Use from_dmss() to convert the latitude to decimal degrees
        lat_dmss = [LATD, LATM, LATS, LATH]
        lon_dmss = [LOND, LONM, LONS, LONH]
        latdd = from_dmss(lat_dmss, 'dd')

            # Use from_dmss() to convert the longitude to decimal degrees
        londd = from_dmss(lon_dmss, 'dd')

            # create pnt = arcpy.Point(lon, lat)
        pnt = arcpy.Point(londd, latdd)

            # use the insertRow([pnt, PID, DESIG]) method of the insert cursor to create a feature for this marker.
        ic.insertRow([pnt, PID, DESIG])

## WE CREATED THIS SHAPEFILE IN NAD83(2011) GEOGRAPHIC COORDINATES (LON, LAT). LET'S PROJECT IT TO
## SPC83(0600), WHICH IS THE STATE PLANE COORDINATE SYSTEM FOR CONNECTICUT. WKID = 6433
# Call arcpy.management.Project(in_featureclass, out_featureclass, new_spatial_reference)
# in_featureclass is the feature class you just created.
# out_featureclass is the name of the projected feature class, and its name must be different than in_featureclass
# The new_spatial_reference for SPC83_0600 is 6433
fn_rprjct = dl + data_path + 'survey_markers.shp'
SPC = 6433
arcpy.management.Project(fn, fn_rprjct, SPC)
print(fn, fn_rprjct, SPC)
print("\nSurvey markers has been reprojected.")

# take a screenshot of your feature class in arcpro labeling the points with their designations.
# submit this script, your control_markers.shp, and the screenshot