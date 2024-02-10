"""
Jonathan Leonard                                    NRE 5585 Python Scripting for Geospatial Analysis
Week 6 a Reading Points                             5OCT2021
"""

## INITIALIZE YOUR SCRIPT WITH IMPORTS, DRIVE LETTER, PATHS, ETC.
print('Initializing...')
import arcpy
dl = "C:/"
data_path = "NRE_5585/data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.workspace = dl + res_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')

## COMPUTE THE CENTROID OF THE LWDS FEATURE CLASS USING SHAPE@XY
#inf = float('inf')
# create a search cursor named <sc> for the LWDS feature class with 'SHAPE@XY' as the field_name
with arcpy.da.SearchCursor(dl+data_path+'LWDS.SHP', ['SHAPE@', 'SHAPE@X', 'SHAPE@Y', 'SHAPE@XY']) as sc:  #

    # set up variable to allow you to compute the average for the x- and y-coordinates...
    #bb = {'minx': inf, 'miny': inf, 'maxx': -inf, 'maxy': -inf}
    ycen = []
    xcen = []
    for row in sc:

        #  get the x- and y-coordinates from row
        x, y = row[-1]
        #print(x, y)
        xcen.append(x)
        ycen.append(y)
avex = sum(xcen)/len(xcen)
avey = sum(ycen)/len(ycen)

print(f'\nAverage x bar = {avex:0.02f}')
print(f'Average y bar = {avey:0.02f}')
print("\nFinished!  Alert Breitbart!!! ")
