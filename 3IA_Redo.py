"""
Jonathan Leonard                         NRE 5585 Python Scripting for Geospatial Analysis
Module 3 Independant Assignment          20SEP2021
"""
## Set up data paths and workspace
print('Initializing...')
import arcpy
import os
import matplotlib.pyplot as plt

dl = "C:/"
data_path = "NRE_5585/data/Weather_data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.overwriteOutput = True
arcpy.env.workspace = dl + temp_path
print('Ready to go!\n')

##
os.chdir('C:/NRE_5585/data/Weather_data')
dir_list = os.listdir()
print("Files in Weather_data =", dir_list, '\n')

# create a variable that will count the number of data records in the files
count = 0

# create a variable that will be the sum of all the wind speed values
sum_ws = 0

# windspeed[day] = []  # holds a list of all wind speeds for this day
date = {}
ws = []

## . Have an outer for-loop iterating over the list of file names
## Have an inner loop to group-by day, as discussed next. (Remember to skip header rows.)
for fn in dir_list:
    fh = open(fn)
    print('File is opened...')

    for data in fh:
        fl = data[0]
    if not fl.isnumeric():
        continue
    values = data[:-1].split(',')

    # split the line into a list of values
    date1 = values[0]
    wind_speed = float(values[2])
    time_stamp = values[0].split()
    day = date1.split(',')
    day = day[0]
    if day not in date:
        date[day] = []
    rn = values[1]

    # cast the element of the value-list holding day and the wind speed
    ws = values[2]
    if ws == "NAN":
        continue
    ws = float(values[2])
    if ws > 100:
        continue
    date[day].append(ws)

print(date.keys(), '\n')
for day in date:
    count = 0
    sum_ws = 0
    ws_list = date[day]
    for ws in ws_list:
        # increment the variable above you're counting data records with
        count += 1

        # add the wind speed value to your variable above that is summing the wind speeds
        sum_ws += ws

    # avg = wind_sum/count_sum
    ave = sum_ws / count
    print("Average wind speed on", day,f'= {ave:0.3f} m/s')
#bin1 = int(ave // 1)
labels = ['0', '1', '2', '3', '4', '5']
colors = ['b', 'r', 'y', 'g', 'k', 'orange']
xplode = [0, 0.2, 0, 0]
# this if-statement does not have an else-clause; it's just the if-statement and its body, so there's
# nothing else in the for-loop
# print()
print("\nFinally done!    ....Do not alert the press!!! They knew about the news a week ago.")
plt.pie(bin1, labels=labels,  colors=colors, explode=xplode)
plt.show()
