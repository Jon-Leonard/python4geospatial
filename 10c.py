"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 10 c Pie CHarts                                     9NOV2021
"""

print('Initializing...')
import arcpy
import numpy as np
import matplotlib.pyplot as plt
import os
dl = 'C:/'
data_path = 'NRE_5585/Data/'
temp_path = 'NRE_5585/Temp/'
res_path = 'NRE_5585/Results/'
arcpy.env.workspace = dl + data_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')
'''
Write a script to produce a pie chart for the winds speeds (m/s) in the three csv files in the
data/weather_data directory. Gather the wind speeds into bins as follows. After you’ve casted the
windspeed to a float…
Compute the bin number by doing an integer division by 1 and casting to an int. The value coming from
the integer division is an integer, like 1.0, but it has a type of float so we want to cast it to an int.
'''

os.chdir('C:/NRE_5585/data/Weather_data')
dir_list = os.listdir()
print("Files in Weather_data =", dir_list, '\n')

# create a variable that will be all the wind speed values
count = 0
lst = []
bin0 = []
bin1 = []
bin2 = []
bin3 = []
bin4 = []
bin5 = []

## . Have an outer for-loop iterating over the list of file names
## Have an inner loop to group-by day, as discussed next. (Remember to skip header rows.)
for fn in dir_list:
    fh = open(fn)
    for data in fh:
        fl = data[0]
        if not fl.isnumeric():
            continue
        values = data[:-1].split(',')
        ws = values[2]
        if ws == "NAN":
            continue
        ws = float(values[2])
        v = int(ws // 1)
        lst.append(v)

        if vel == 5:
            count += 1
        '''
        if lst in lst == 4:
            bin4.append(lst)
        if lst in lst == 3:
            bin3.append(lst)
        if lst in lst == 2:
            bin2.append(lst)
        if lst in lst == 1:
            bin1.append(lst)
        if lst in lst == 0:
            bin0.append(lst)
        '''
print('lst =', lst)

'''
labels = ['0', '1', '2', '3', '4', '5']
colors = ['b', 'r', 'y', 'g', 'k', 'orange']
xplode = [0, 0.2, 0, 0]
plt.pie(lst, labels=labels, colors=colors, explode=xplode)
plt.show()
'''
#jpl17019
#Fangjian206265?