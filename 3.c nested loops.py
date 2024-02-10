"""
Jonathan Leonard                        NRE 5585 Python Scripting for Geospatial Analysis
Module 3 c    Nested loops              19SEP2021
"""
## NESTED LOOPS

## IN THIS EXERCISE, YOU WILL PERFORM THE FOLLOWING...
##      CONVERT A RASTER DIGITAL ELEVATION MODEL (DEM) (dem.img) TO AN ASCII TEXT FILE,
##      CREATE A DICTIONARY TO HOLD THE RESULTS,
##      ITERATE OVER THE CELLS, WHICH ARE ELEVATIONS,
##      ROUND THE ELEVATIONS TO THE NEAREST INTEGER,
##      AND COUNT THE NUMBER OF CELLS HAVE THAT (ROUNDED) ELEVATION...
##      USING THE DICTIONARY

##-------------------------------------------------------------
## PART 1: INITIALIZE YOUR SCRIPT: IMPORT arcpy AND CREATE VARIABLES FOR PATHS, ETC
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
print('Ready to go!')

# create a variable that holds the DEM's path and name
dem = dl + data_path + "dem.img"

# create a variable that holds the converted DEM's path and name. Put it in the 
# temp directory and use a .txt extension
dem_converted = dl + data_path + "dem_converted.txt"
print(dem_converted)

# convert the raster to an ASCII text file, putting the result in the temp directory. 
# Do NOT put it in the data directory
arcpy.conversion.RasterToASCII(dem, "dem_converted.txt")
dem_txt = "dem_converted.txt"
# create an empty dictionary to hold the counts of how many heights are in a particular contour interval
contours = {}  # dictionary mapping elevation -> count

# for each row in the ASCII raster file...
for row in open(dl + temp_path + dem_txt):
    #  skip over the header lines
    fl = row[0]
    if not fl.isnumeric():   # skip header
        continue
    #  split <row> into cell values (heights) omitting the terminating \n character
    values = row[:-1].split()

    # for each value in the list of values
    for value in values:
        # value is a string so cast it to a float
        values = float(value)
        #print(values)

        # round value to the nearest int. round() returns a float, so cast to an int
        values = round(values)
        #print(values)
        h = int(round(values))
        #print(h)

        # if h is not in your dictionary
        if h not in contours:
            # add it to the dictionary with a count of zero
            contours[h] = 0

        # now your dictionary definitely has an entry for h, so increment the count for that h
        else:
            contours[h] += 1
print(f"DEM has {contours}")
## PRINT THE RESULTS. eg There are 18102 cells at height 159
#(contours)
for height, count in contours.items():
    print(f"There are {count} cells at height {height}")

## Now we will determine which contour interval has the most cells, and print the contour interval and the count

# create a variable to hold the maximum count seen so far, which, right now, is zero
max_count = 0

# for each height, count pair in the dictionary:
for height, count in contours.items():
    # if the count is greater than max_count,
    if count > max_count:
        # set max_count to the count
        max_count = count
        # set h to the height
        h = height
print(f"Elevation {h} has the most cells: {max_count}")

## Here's some code that will plot your results to the screen, which is a much better way to understand
## the results. We'll learn more about plotting later on, so this is a bit of foreshadowing

# Create a list of the contour intervals, which are the dictionary's key values
intervals = list(contours.keys())

# Create a list of the contour interval counts, which are the dictionary's values
counts = list(contours.values())

import matplotlib.pyplot as plt
plt.plot(intervals, counts, 'r+')
plt.title("Distribution of heights")
plt.xlabel("height (m)")
plt.ylabel("number of cells")
plt.show()