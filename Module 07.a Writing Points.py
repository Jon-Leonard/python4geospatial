"""
Jonathan Leonard                                    NRE 5585 Python Scripting for Geospatial Analysis
Week 7 a Writing Points                             13OCT2021
"""

## INITIALIZE YOUR SCRIPT WITH IMPORTS, DRIVE LETTER, PATHS, ETC.
## SET THE WORKSPACE TO THE TEMP DIRECTORY
print('Initializing...')
import arcpy
import numpy as np
dl = "C:/"
data_path = "NRE_5585/data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.workspace = dl + temp_path
arcpy.env.overwriteOutput = True

# import fibonacci_lattice
import fibonacci_lattice as FL
print('Ready to go!\n')

### Open ArcPro and create a point feature class in your temp folder named 'CT_grid.shp'.
### Use NAD 83 (2011) for the XY coordinate system.
### Remove it from the contents pane to release the lock ArcPro puts on the shapefile

# Create variables for minimum, maximum latitude, longitude (total of four variables) for CT
lonMin = np.radians(-73.0 - 44.0 / 60.)
lonMax = np.radians(-71.0 - 47.0 / 60.)
latMin = np.radians(40.0 + 58.0 / 60.)
latMax = np.radians(42.0 + 3.0 / 60.)

# Use fibLatticeFiltered(N, lonMin, lonMax, latMin, latMax) with N = 20_000_000 to create the grid points'
# coordinates
N = 20_000_000
print('Generating Fibonacci lattice for', N, 'inputs...')
lon, lat = FL.fibLatticeFiltered(N, lonMin, lonMax, latMin, latMax)
print('Finished creating lattice\n')

# Convert the longitudes to decimal degrees (DD)
lon = np.rad2deg(lon)
# Convert the latitudes to decimal degrees (DD)
lat = np.rad2deg(lat)

# Create an insert cursor for CT_grid.shp with field-list 'SHAPE@XY'
# Recall that the 2nd argument to arcpy.da.InsertCursor() can be either the name of a single attribute or
# a list of attributes names. Here, we use the single name because there are no other attributes
with arcpy.da.InsertCursor('CT_grid.shp', 'SHAPE@XY') as ic:

    # iterate over zip(lon, lat). Assign the longitude to 'x' and the latitude to 'y'
    for lamphi in zip(lon, lat):

        # use the insertRow([x,y]) method of the insert cursor to create this grid point.
        ic.insertRow((lamphi,))

# use arcpy.analysis.Clip() to clip CT_grid.shp to the Towns.shp shapefile in the data directory. Name
# the output CT_grid_clipped.shp and create it in the temp directory
arcpy.analysis.Clip('CT_grid.shp', dl+data_path+'Towns.shp', 'CT_grid_clipped.shp')

# Open your feature class in Arcpro and take a screenshot of it.
# Submit this script, your CT_grid_clipped.shp, and the screenshot. How far apart are the points (km)?
print('Approximate distance between points = 3.5 km')