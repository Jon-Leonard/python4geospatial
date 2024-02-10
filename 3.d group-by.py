"""
Jonathan Leonard                         NRE 5585 Python Scripting for Geospatial Analysis
Module 3 d    Nested loops: group by     20SEP2021
"""
## NESTED LOOPS

## IN THIS EXERCISE, YOU WILL PERFORM THE FOLLOWING...
##      READ AND PARSE A FILE HOLDING INFORMATION COLLECTED BY
##      GPS COLLARS ON MOUNTAIN LIONS (PUMAS)...
##      GROUP THE RECORDS BY STUDY AREA...
##      FIND EACH AREA'S BOUNDING BOX AND...
##      COMPUTE THE AREA OF EACH BOUND BOX IN HECTARES.
##-------------------------------------------------------------
## PART 1: INITIALIZE YOUR SCRIPT WITH VARIABLES FOR PATHS, ETC
#
print('Initializing...')
import arcpy
import numpy as np

dl = "C:/"
data_path = "NRE_5585/data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.overwriteOutput = True

# set the workspace to the temp directory
arcpy.env.workspace = dl + temp_path
print('Ready to go!''\n')

# create a variable that holds PumaPositions.csv's path and name
puma_strng = dl + data_path + 'PumaPositions.csv'

##-------------------------------------------------------------
## PART 2: GROUP BY STUDY AREA
# create an empty dictionary to hold the groups by study area
study_area = {}

# open PumaPositions.csv and read the first line, which contains the column names
puma = "PumaPositions.csv"
fh = open(puma_strng)
print(fh)
hdr_row = fh.readline()
print(hdr_row)

# for each row after the first...
for row in fh:  # for each row in the file
    first_char = row[0]
    if not first_char.isnumeric():
        continue
    values = row[:-1].split(',')
    id = int(values[0])
    cougarID = (values[1])
    cllrID = (values[2])
    sex = (values[3])
    area = (values[4])
    date = (values[5])
    date_num = (values[6])
    e = float(values[7])
    n = float(values[8])
    cougar = [id, cougarID, cllrID, sex, area, date, date_num, e, n]
    if area not in study_area:
        study_area[area] = []
    study_area[area].append(cougar)
lst = list(study_area)
print(lst, '\n')

    # parse the row.
    #     Extra credit: instead of putting each row into a list, put each row into its own dictionary.
    #     So far, our parsing has been to cast each value in the row to its proper type
    #     and then the place them in a list for storage in the dictionary we're using for grouping.
    #     This is fine but it requires us to know the place in the array each value has when we want to
    #     use that value downstream, which is annoying and error prone. Putting the values into another
    #     dictionary is a more elegant solution, a dictionary that maps value_name to value.
    #     For example, the first row would be this dictionary:
    #     {'ID': 1, 'CougarID': 'P01', 'CllrID': '2905', 'Sex': 'M', 'StudyArea': 'CO',
    #     'DateTime': '3/1/2011 0:00', 'DateTimeNumber': 40603.91, 'Easting': 727905.67, 'Northing': 4373142.03}
    #     Doing so lets us extra values by name instead of by position.

##-------------------------------------------------------------
## PART 3: FIND EACH STUDY AREA'S BOUNDING BOX
# A bounding box (bb) is a set of four spatial coordinates that enclose the data set. For example, the bb's
# north border is the largest northing in the group, and the bb's south border is the smallest northing in the group.
# Similar for east and west. Study the initial values to understand why those are good choices
bb = {}  # create an empty dictionary to hold the bounding boxes
for area in study_area.keys():
    bb[area] = {'n': 0, 's': float('inf'), 'e': 0, 'w': float('inf')}  # initialize the borders

#  for each study area...
for area in study_area:
    #  for each cat in the study area...
    for cougar in study_area[area]:
        #  set local variables to hold this cat's easting and its northing coordinates
        e = cougar[7]
        n = cougar[8]
        #  if the northing is greater than this study area's current north border, set the bb's north border
        #  to this cat's northing coordinate
        if n > bb[area]['n']:
            bb[area]['n'] = n
        #  if the northing is less than this study area's current south border, set the bb south border
        #  to this cat's northing coordinate
        if n < bb[area]['s']:
            bb[area]['s'] = n
        #  similar for the east and west borders
        if e > bb[area]['e']:
            bb[area]['e'] = e

        if e < bb[area]['w']:
            bb[area]['w'] = e

    #  add another element to this study area's bb so that the key 'area' is associated with the area of the bb
    bb[area]['key'] = (bb[area]['n'] - bb[area]['s']) * (bb[area]['e'] - bb[area]['w']) / 10**4

# Print the study areas' areas in hectares using scientific notation, 3 sig. digits. The format string is 0:3e
# CO has 7.785e+05 hectares
# WY has 1.179e+06 hectares
# Patagonia has 1.977e+06 hectares
for area in study_area:
    places = bb[area]['key']
    print(f"{area} is {places:0.3e} hectares")