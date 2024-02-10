"""
Jonathan Leonard                                           NRE 5585 Python Scripting for Geospatial Analysis
Week 7 b Multi-level Grouping                              15OCT2021
"""
## INITIALIZE YOUR SCRIPT WITH IMPORTS, DRIVE LETTER, PATHS, ETC.
print('Initializing...')
import arcpy
dl = 'C:/'
data_path = 'NRE_5585/Data/'
temp_path = 'NRE_5585/Temp/'
res_path = 'NRE_5585/Results/'
arcpy.env.workspace = dl + res_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')

"""
Open eop.shp in ArcPro and label the points with the expression 
$feature.road + '-' + $feature.group
and turn on the labels. You'll see that the 'road' attribute identifies
which road a point is on (unsurprisingly), and that the 'group' attribute
puts each point into a group according to the mapper's own thinking.

Remove eop from the contents pane to release the lock ArcPro put on it.

In this exercise will we gather the points in eop.shp into multi-level 
groups in preparation for writing multipoint features later on.
"""

# create an empty dictionary named 'roads'
roads = {}

#create a SearchCursor for eop.shp, reading in the SHAPE@XY, road, and group attributes
with arcpy.da.SearchCursor(dl + data_path + 'eop.shp', ['SHAPE@XY', 'group', 'road']) as sc:
    # iterate over the search cursor
    for row in sc:
        # extract the x,y coordinates
        x, y = row[0]
        # extract the road name
        road_nm = row[-1]
        # extract the group
        group = row[1]
        # if we haven't seen this road name before..
        if road_nm not in roads:
            # associate that road name in 'roads' with an empty dictionary
            roads[road_nm] = {}
        # if we haven't seen this road-name|group before...
        if group not in roads[road_nm]:
            # associate that group with an empty list
            roads[road_nm][group] = []
        # add the x,y coordinates to the list associated with roads[road_nm][group]
        roads[road_nm][group].append(x)
        roads[road_nm][group].append(y)

# Print the results:
print(f'Results by group = {roads}')

# for each road...
print('\nRoad: Name, Group, and  XY coordinates...\n')
for road_nm in roads:
    # for each group in this road...
    for group in roads[road_nm]:
        # print the road, group, and coordinates of the point
        print(road_nm, group, roads[road_nm][group])
print('\nFinished! Alert The Sun!')