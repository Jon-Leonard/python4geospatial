"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 10 d     Histograms                                 2NOV2021
"""

print('Initializing...')
import arcpy
import numpy as np
import matplotlib.pyplot as plt
dl = 'C:/'
data_path = 'NRE_5585/Data/'
temp_path = 'NRE_5585/Temp/'
res_path = 'NRE_5585/Results/'
weather_path = dl + data_path + 'Weather_data/'
arcpy.env.workspace = dl + res_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')

rover1 = open(weather_path + 'Rover_TI_3_1h.csv', 'r')
rover2 = open(weather_path + 'Rover_TI_3_4h.csv', 'r')
rover3 = open(weather_path + 'Rover_TI_3_8h.csv', 'r')

wind_speed = []
for records in rover1:
    fl = records[0]
    if not fl.isnumeric():
        continue
    values = records[:-1].split(',')
    date1 = values[0]
    days = date1.split(' ')
    day = days[0]
    ws = values[2]
    if ws == 'NAN':
        continue
    ws = float(values[2])
    if ws >= 10:
        continue
    wind_speed.append(ws)
for records in rover2:
    fl = records[0]
    if not fl.isnumeric():
        continue
    values = records[:-1].split(',')
    date1 = values[0]
    days = date1.split(' ')
    day = days[0]
    ws = values[2]
    if ws == 'NAN':
        continue
    ws = float(values[2])
    if ws >= 10:
        continue
    wind_speed.append(ws)

for records in rover3:
    fl = records[0]
    if not fl.isnumeric():
        continue
    values = records[:-1].split(',')
    date1 = values[0]
    days = date1.split(' ')
    day = days[0]
    ws = values[2]
    if ws == 'NAN':
        continue
    ws = float(values[2])
    if ws >= 10:
        continue
    wind_speed.append(ws)
wind_speed = np.array(wind_speed)
plt.hist(wind_speed, bins=10, density=1, edgecolor='k')
plt.title('Wind speed (m/s)', size=16)
plt.show()
print("Finished!  Send out a tweet to all my followers!")