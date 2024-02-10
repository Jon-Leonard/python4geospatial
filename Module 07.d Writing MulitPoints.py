"""
Jonathan Leonard                                           NRE 5585 Python Scripting for Geospatial Analysis
Week 7 d Writing multipoints                               16OCT2021
"""

## INITIALIZE YOUR SCRIPT WITH IMPORTS, DRIVE LETTER, PATHS, ETC.
print('Initializing...')
import arcpy
dl = 'C:/'
data_path = 'NRE_5585/Data/'
temp_path = 'NRE_5585/Temp/'
res_path = 'NRE_5585/Results/'
arcpy.env.workspace = dl + temp_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')

"""
In this exercise we will be creating multipoint features using the eop.shp feature class as input.
eop stands for 'edge of pavement,' and it is a term using by surveyors to denote a point on the
edge of a road. Roads are usually mapped by collecting eop points and then "connecting the dots",
using the eop attribute information to group the points into roads and into segments of roads.

eop.shp has attributes 'road' and 'group' that create a two-level grouping: first by road, and
then groups within road.

Let's start with creating the multi-level groupings
"""

# Create an empty dictionary to hold the road groupings.
roads = {}
eop = dl + data_path + "eop.shp"
eop_copy = dl+temp_path + 'eop_copy.shp'
arcpy.management.CopyFeatures(eop, eop_copy)

# Create a search cursor on eop.shp extracting the 'SHAPE@XY','road','group' attributes
with arcpy.da.SearchCursor(eop_copy, ['SHAPE@XY', 'group', 'road']) as sc:
    # for each row in the cursor...
    for row in sc:

        # extract the attributes and put them into variables.
        x, y = row[0]
        road_nm = row[-1]
        group = row[1]
        if road_nm not in roads:
            roads[road_nm] = {}
        ## if the road's name isn't in the dictionary, associate an empty dictionary with this road name
        if group not in roads[road_nm]:
            roads[road_nm][group] = []
        ## if the group's name isn't in the road-name's dictionary, associate an empty list with this group name
        xy = x, y
        ## append the x,y coordinates to this road|group list
        roads[road_nm][group].append(xy)

"""
Now we'll create a new feature class to hold the multipoint features. Call the new MULTIPOINT feature class 
eop_grouped.shp and create it in your results directory. Use State Plane 1983 Connecticut meters FIP 0600 for the spatial
reference. Then add text attribute fields named 'road' and 'group'.
"""
WKID = 6433
eop_grouped = 'eop_grouped.shp'

## Create the feature class
arcpy.management.CreateFeatureclass(dl+temp_path, eop_grouped, 'MULTIPOINT',  spatial_reference=WKID)
## use arcpy.management.AddField to add the text field named 'road' to the attribute table
arcpy.AddField_management(eop_grouped, 'road', 'TEXT')
## use arcpy.management.AddField to add the text field named 'group' to the attribute table
arcpy.AddField_management(eop_grouped, 'group', 'TEXT')

"""
Now we create the multipoint features
"""

## create an InsertCursor for your new feature class with attribute list ['SHAPE@', 'ROAD', 'GROUP']
with arcpy.da.InsertCursor(eop_grouped, ['SHAPE@', 'ROAD', 'GROUP']) as ic:
    ## for each road name in roads...
    for road_nm in roads:
        ## for each group in roads[road_nm]
        for group in roads[road_nm]:
            ## create an arcpy.Array to hold the multipoint feature's points
            point_lst = arcpy.Array()

            ## for each x,y pair in roads[road_nm][group]
            for x, y in roads[road_nm][group]:

            ## create an arcpy.Point object with the x,y pair
                p = arcpy.Point(x, y)
            ## append the Point to point_lst
                point_lst.append(p)

            ## create an arcpy.Multipoint object from point_lst
            mp = arcpy.Multipoint(point_lst)
            print("There are ", len(mp), "points in this category")
            ## use the insertRow() method of the insert cursor to insert the new feature
            ic.insertRow([mp, road_nm, group])

## Turn in this script, the shapefile you created, and a screenshot of it in ArcPro
print('\nFinished! Look Mom, ...no hands!!!')