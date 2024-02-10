"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 8 IA   Spatially joining point to raster            25OCT2021
"""

'''
In this exercise, we will join the features of a point shapefile to a raster. This join will allow us to
perform an accuracy evaluation of the pixel values that correspond to each point feature to the
shapefile attribute table. In our scenario, we want to validate a digital elevation model (DEM) using
point locations that have been surveyed in the field with a total station. We will compare the elevations
measured in the field to the elevation values in the DEM cells. For this assignment, you will use the
surveyPts.shp and DEM.img datasets, both in the NRE_5585/data directory.
'''

'''
The term “spatial join” is a GIS term that has its origins in the data base world. It means to take the
features from two or more feature classes and match them in some way, then compare their attribute
values in some way. Here we're joining a point feature class to a raster, so find the cell in the raster in
which each point resides (spatially), and we’ll take the difference of the elevations.
'''
print('Initializing...')
import arcpy
import lib5585 as L
import numpy as np
import os
dl = 'C:/'
data_path = 'NRE_5585/Data/'
temp_path = 'NRE_5585/Temp/'
res_path = 'NRE_5585/Results/'
arcpy.env.workspace = dl + res_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')

'''
The objectives of this exercise are to…
Develop a script that evaluates the error of the DEM using the surveyed points…

1. For each survey point, identify the corresponding DEM cell and get its elevation.
2. Calculate the error, as the difference between the DEM and ground truth, and add to a list of errors.
3. Calculate and print the average and standard deviation of the errors.
'''
dem_ct = dl + data_path + "DEM.img"
surveyPts = dl + data_path + "surveyPts.shp"

# I'm feeling anxious about this IA and disturbing the originals. So let's Make copies
arcpy.CopyFeatures_management(surveyPts, dl + temp_path + 'surveyPts_copy.shp')
arcpy.management.CopyRaster(dem_ct, dl + temp_path + 'dem_copy.img')
survey_pts = dl + temp_path + "surveyPts_copy.shp"
DEM = dl + temp_path + "dem_copy.img"

# Need to get the raster information using Describe
desc = arcpy.da.Describe(DEM)
#print(desc)

spat_ref = desc['spatialReference']
left = arcpy.management.GetRasterProperties(DEM, 'LEFT')
top = arcpy.management.GetRasterProperties(DEM, 'TOP')

cell_size = desc['meanCellHeight']
#print(cell_size)

# Project to match the DEM
points_proj = dl + temp_path + 'points_proj.shp'
arcpy.management.Project(survey_pts, points_proj, spat_ref)

#print(DEM)
origin = [float(left.getOutput(0)), float(top.getOutput(0))]

# Matching points to pixels.
# We need to get the raster’s cells into an array of numbers so we can work with them. See
#arcpy.RasterToNumPyArray(in_raster, {lower_left_corner}, {ncols}, {nrows}, {nodata_to_value})

#This method returns a two-dimensional numpy array whose rows hold the columns of the raster.
#Suppose we have
DEM_array = arcpy.RasterToNumPyArray(DEM)

## create an empty list to hold the errors
errors = []

## for each survey point in the re-projected layer…

# get the e,n coordinates from the cursor, eg, SHAPE@XY
# get the elevation of the survey point from the cursor (it’s in the column named FIELD_ELEV)
with arcpy.da.SearchCursor(points_proj, ['SHAPE@XY', 'FIELD_ELEV']) as sc:
    for row in sc:
        e, n = row[0]
        elev = float(row[1])

        # use en2rc to get row, col index values into the numpy array, so dem[row][col] is the elevation of
        # the dem at this point
        DEM_elev = DEM_array[L.en2rc([e, n], origin, cell_size)]

        # cast the DEM elevation to a float…
        error = float(DEM_elev) - elev

        # compute the error of this DEM elevation and store it in list of errors
        errors.append(error)
#print(error)
#print(errors)

# compute and print mean and standard deviation of the errors to three significant digits
print(f'Mean = {np.std(errors):0.3f}')
print(f'Standard deviation = {np.mean(errors):0.3f}')
print('\nFinished!   .. Oh my! My code runs!!!')