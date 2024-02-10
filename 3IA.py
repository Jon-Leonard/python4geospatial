"""
Jonathan Leonard                         NRE 5585 Python Scripting for Geospatial Analysis
Module 3 Independant Assignment          20SEP2021
"""
## Set up data paths and workspace
print('Initializing...')
import arcpy
import numpy as np
import os
dl = "C:/"
data_path = "NRE_5585/data/Weather_data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.overwriteOutput = True
arcpy.env.workspace = dl + temp_path
print('Ready to go!''\n')

##
os.chdir("C:/NRE_5585/data/Weather_data")
dir_list = os.listdir()
print("Files in Weather_data =", dir_list)
ndv = -999
# create a variable that will count the number of data records in the files
count_ws1h = 0
count_ws4h = 0
count_ws8h = 0
# create a variable that will be the sum of all the wind speed values
sum_ws1h = 0
sum_ws4h = 0
sum_ws8h = 0
#windspeed[day] = []  # holds a list of all wind speeds for this day

## . Have an outer for-loop iterating over the list of file names
         ## Have an inner loop to group-by day, as discussed next. (Remember to skip header rows.)
for line in open(dl + data_path + "Rover_TI_3_1h.csv"):
        first_char = line[0]
        if not first_char.isnumeric():
            continue
        values = line[:-1]
        # split the line into a list of values
        values = values.split(',')
        wind_speed = float(values[2])
        time_stamp = values[0].split()
        day = time_stamp[0].split()
        first_chars = day[0]
        sum_ws1h = sum_ws1h + wind_speed

print(values)
print(time_stamp)
print(day)
print(first_chars)
print(sum_ws1h)

###############

for line in open(dl + data_path + "Rover_TI_3_4h.csv"):
        first_char = line[0]
        if not first_char.isnumeric():
            continue
        values = line[:-1]
        # split the line into a list of values
        values = values.split(',')
        wind_speed = float(values[2])
        time_stamp = values[0].split()
        day = time_stamp[0].split()
        first_chars = day[0]
        sum_ws4h = sum_ws4h + wind_speed

print(values)
print(time_stamp)
print(day)
print(first_chars)
print(sum_ws4h)
#########################
for line in open(dl + data_path + "Rover_TI_3_8h.csv"):
        first_char = line[0]
        if not first_char.isnumeric():
            continue
        values = line[:-1]
        # split the line into a list of values
        values = values.split(',')
        wind_speed = float(values[2])
        time_stamp = values[0].split()
        day = time_stamp[0].split()
        first_chars = day[0]
        sum_ws8h = sum_ws8h + wind_speed

print(values)
print(time_stamp)
print(day)
print(first_chars)
print(sum_ws8h)

    # cast the element of the value-list holding day and the wind speed

        # add the wind speed value to your variable above that is summing the wind speeds

        # increment the variable above you're counting data records with

    # this if-statement does not have an else-clause; it's just the if-statement and its body, so there's
    # nothing else in the for-loop

# compute the average wind speed
wind_sum = sum_ws1h + sum_ws4h + sum_ws8h
count_sum = count_ws1h+count_ws4h+count_ws8h

#avg = wind_sum/count_sum
print('the wind sum is,', wind_sum)
print('The count sum is,', count_sum)
#print('The average is,', avg)
print("Do not alert the press!!!")

