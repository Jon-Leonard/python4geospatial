"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 10 a              Bar Charts                        2NOV2021
"""

'''
Write a script to produce a bar plot for the mountain-lion data in PumaPositions.csv. Group the data by
study area and then by sex. Count the number of records in each group and plot them as shown below.
The groupings are CO(FM), Patagonia(FM), WY(FM) from left-to-right. Match these orderings so the
heights of your bars appear as mine do.
'''

## Initialize script and set data paths
print('Initializing...')
import arcpy
import matplotlib.pyplot as plt
dl = 'C:/'
data_path = 'NRE_5585/Data/'
temp_path = 'NRE_5585/Temp/'
res_path = 'NRE_5585/Results/'
arcpy.env.workspace = dl + data_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')

cats = dl + data_path + "PumaPositions.csv"
fh = open(cats)
print(fh)
hdr_row = fh.readline()
print(hdr_row)
groups = {}

with open(cats) as ss:
    for line in ss:
        values = line[:-1].split(',')
        if values[0] == "ID":
            continue ## bypass hdr
        area = values[4]
        if area not in groups:
            groups[area] = {}
        sex = values[3]
        #print(sex)
        #print(groups)
        if sex not in groups[area]:
            groups[area][sex] = 0
        groups[area][sex] += 1
print(groups)

d = 0
shft = 1
for area in sorted(groups.keys(), reverse=False):
    s_x = d
    for sex in sorted(groups[area].keys(), reverse=False):
        print(sex)

        plt.bar(s_x, groups[area][sex], width=0.3)
        #plt.bar(d, groups[area][sex], width=0.3)
        #plt.bar(d, groups[area][sex], width=0.3)
        s_x += 0.3
    d += shft   # for unstacked bars!
plt.show()
print("Finished! That took some trial & error!")