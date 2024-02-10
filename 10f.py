"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 10 f     Scatterplot                                2NOV2021
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

surveyPts = dl+data_path + "surveyPts.shp"
dem = dl+data_path + "dem.img"

arcpy.CopyFeatures_management(surveyPts, dl+temp_path + "survey,shp")
survey = dl+temp_path + "survey.shp"

'''
Write a script to produce a scatterplot of the DEM-accuracy sample locations as shown below. I bin the
errors into 5 cm bins with
'''
bin = abs(int(error // 0.05))

'''
and I set the bin to 6 if bin > 6, so group first by whether the error is positive or negative, then group the
xy coordinates by bin. The symbols and colors come from
'''
sym = {1: '+', -1: '.'} # 1 is for non-negative errors, and -1 is for negative errors
colors = ['k', 'g', 'm', 'b', 'c', 'y', 'r'] # bin zero is black, one is green, etc.


errors = []

if bin == 0:
    bin0.append(bin)
if bin == 1:
    bin1.append(bin)
if bin == 2:
    bin2.append(bin)
if bin == 3:
    bin3.append(bin)
if bin == 4:
    bin4.append(bin)
if bin == 5:
    bin5.append(bin)
if bin == 6:
    bin6.append(bin)
errors.append(bin)
east.append(e)
north.append(n)
ave = np.average(errors)
std = np.std(errors)

sym = {1: '4', -1: '.'}
colors = ['g','k','m','c','b','y','r']
k = sym, colors
plt.plot(east, north)
plt.show()