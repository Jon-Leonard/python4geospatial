"""
Jonathan Leonard                                    NRE 5585 Python Scripting for Geospatial Analysis
Week 6 c Reading Polylines                          8OCT2021
"""

## INITIALIZE YOUR SCRIPT WITH IMPORTS, DRIVE LETTER, PATHS, ETC.
print('Initializing...')
import arcpy
import lib5585 as L
dl = "C:/"
data_path = "NRE_5585/data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.workspace = dl + data_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')

# Create a search cursor for 'curbs.shp', retrieving the geometry object (SHAPE@) and FID...
with arcpy.da.SearchCursor('curbs.SHP', ['SHAPE@', 'FID']) as sc:
    # for each curb feature...
    for row in sc:
        # Print FID...
        FID = row[-1]

        # assign the geometry object to a variable named polyline...
        polyline = row[0]

        # get the Array of parts using the getPart() method...
        polyline_array = polyline.getPart()

        # initialize a variable to the integer zero. This variable will hold the total length of each curb
        curblen = 0
        partlen = 0

        # for each point_array in the array of parts
        for point_array in polyline_array:
            # create an empty list xy to hold the x- and y-coordinates
            xy = []

            # for each point in the part array..
            for point in point_array:
                #  print the X- and Y-coordinate to three significant digits...
                x, y = point.X, point.Y
                #print(f'X = {x:0.03f} Y = {y:0.03f}')
                #  append the coordinates to the xy list
                xy.append([x, y])

            # calculate the length of this part
            for dist in range(len(xy)-1):

            # print the length
                partlen = L.distance(xy[dist], xy[dist + 1], 1)
                curblen += L.distance(xy[dist], xy[dist + 1], 1)
            #print('Length =', partlen)
        #print('\n')
            # add the length of this part to the total

        # print the total length to 3 sig. digits (311.063, 133.706, 104.025)
        print(f'Total curb length = {curblen:0.03f}')

print("\nFinished! Alert ABC News!")