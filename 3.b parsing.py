"""
Jonathan Leonard                        NRE 5585 Python Scripting for Geospatial Analysis
Module 3 b Parsing files                17SEP2021
"""
## PARSING FILES

## IN THIS EXERCISE, YOU WILL PERFORM THE FOLLOWING...
##      OPEN A FILE IN READ MODE
##      SKIP THE HEADER LINES
##      READ THE DATA LINES AFTER THE HEADER, PARSING THEM
##      COMPUTE THE AVERAGE WINDSPEED

##-------------------------------------------------------------
## PART 1: INITIALIZE YOUR SCRIPT WITH VARIABLES FOR PATHS, ETC
#
print('Initializing...')
import arcpy
import numpy as np

dl = "C:/"
data_path = "NRE_5585/data/Weather_data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.workspace = res_path
arcpy.env.overwriteOutput = True
print('Ready to go!')

##-------------------------------------------------------------
## PART 2: ITERATE THROUGH THE CSV FILE, SKIPPING THE HEADER RECORDS, AND COMPUTING
##         THE AVERAGE WIND SPEED
#

# The file is in the Weather_data subfolder of the Data directory.
# The file's name is Rover_TI_3_1h.csv
# Open the file with a text editor. Notice that the data records begin with a date. All data records' first character
# is a number, and no header records begin with a number. We can use this to discriminate between header
# records and data records. Which column holds windspeed?
# Exit out of the text editor you're looking at the file with.

# create a variable that will count the number of data records in the file
#count = 0
# create a variable that will be the sum of all the wind speed values
#sum_ws = 0
date = {}
# open the file in a for-loop statement. Name the index variable 'line' as I did in the slides.

for line in open(dl + data_path + "Rover_TI_3_1h.csv"):
    first_char = line[0]

    # if the first character in <line> is numeric (use the isnumeric() method on the first element in <line>)
    if not first_char.isnumeric():
        continue                             # iterated over header rows
        # this is a data record so parse it
        # get rid of the last character in <line>, the newline character, and ...
    values = line[:-1].split(',')
    print(values)
'''
    date1 = values[0]
    day = date1.split(',')
    day = day[0]
    if day not in date:
        date[day] = []
    num = values[1]
        # cast the element of the value-list holding the wind speed to a float
    ws = float(values[2])
    if ws == "NAN":
        continue
    if ws > 100:
        continue
    date[day].append(ws)
print(date.keys())



        # add the wind speed value to your variable above that is summing the wind speeds
#sum_ws = sum_ws + ws
        # increment the variable above you're counting data records with
#count += 1                     # same as count = count + 1    like above
    # this if-statement does not have an else-clause; it's just the if-statement and its body, so there's
    # nothing else in the for-loop

# compute the average wind speed
avg = ws / values
print(avg)

# print the number of records (85779) and the ws avg (1.312) to three sig. digits and with proper units
print('\n'"Number of records =", date)
print("The average wind speed = {:0.3f}".format(avg), "m/s")
print('\n'"Finished. Alert 'The Day'!!")
'''