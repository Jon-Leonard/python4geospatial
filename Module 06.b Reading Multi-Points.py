"""
Jonathan Leonard                                    NRE 5585 Python Scripting for Geospatial Analysis
Week 6 b Reading Multi-Points                       5OCT2021
"""

## INITIALIZE YOUR SCRIPT WITH IMPORTS, DRIVE LETTER, PATHS, ETC.
print('Initializing...')
import arcpy
dl = "C:/"
data_path = "NRE_5585/data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.workspace = dl + data_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')

# Create a search cursor for 'bldg_corners.shp', retrieving the geometry object (SHAPE@) and FID so ['SHAPE@', 'FID']...

with arcpy.da.SearchCursor('bldg_corners.shp', ['SHAPE@', 'FID']) as sc:
    # for each building feature...
    for row in sc:
        # Print FID
        FID = row[-1]
        print(FID)
        # assign a variable named mp, for "multi-part", the SHAPE@ element in row
        mp = row[0]
        # get the Array of Points by calling mp.getPart()..
        points = mp.getPart()
        # for each point in the part..
        for point in points:

            #  print the X- and Y-coordinate to three significant digits
            x, y = point.X, point.Y
            print(f' {x:0.03f}, {y:0.03f}')
print("\nFinished!  Alert Fox News!!! ")