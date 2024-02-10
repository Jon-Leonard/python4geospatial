"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 9 IA                                                27OCT2021
"""

# import modules
print('Initializing...')
import arcpy
import station_B as station
import lib5585 as L
import numpy as np
dl = 'C:/'
data_path = 'NRE_5585/Data/'
temp_path = 'NRE_5585/Temp/'
res_path = 'NRE_5585/Results/'
arcpy.env.workspace = dl + data_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')

'''
The TOL_CT.shp shapefile in the NRE5585/Data directory comes from the National Geodetic Survey.
Please open the shapefile in arcpro and have a look at it. It contains all the survey markers in Tolland
county, Connecticut.
Looking at the attribute table reveals a lot of columns, including these, which we use to create our Station
objects.
'''

'''
Using the subtraction operator for our objects, answer these questions.
1. Which is the south-most, north-most, east-most, and west-most? Print the stations and indicate
which is which.
'''

#with arcpy.da.SearchCursor(survey_markers, ['DEC_LONG', 'DEC_LAT']) as sc:
markers = dl + data_path + 'TOL_CT.shp'
survey_markers = arcpy.CopyFeatures_management(markers, dl + temp_path + 'survey_markers.shp')
cs = {}

north = 0
south = 10**9
east = -10**9
west = 0
with arcpy.da.SearchCursor(survey_markers, ['DEC_LONG', 'DEC_LAT', 'PID', 'NAME', 'QUAD', 'POS_DATUM',
                                               'DATUM_TAG', 'ELEVATION']) as sc:
    for row in sc:
        lon = float(row[0]) #* np.pi/180  # radians
        lat = float(row[1]) #* np.pi/180  # radians
        PID = str(row[2])
        NAME = row[3]
        POS_DATUM = row[5]
        DATUM_TAG = row[6]
        ELLIP_HT = row[7]
        lat_lon = lat, lon
        if PID not in cs:
            cs[PID] = []
            cs[PID].append(lat_lon)
        else:
            print('Houston, we have a problem...')

north_PID = PID
south_PID = PID
east_PID = PID
west_PID = PID
north_cs = 0
south_cs = 0
east_cs = 0
west_cs = 0

for PID in cs:
    for lat, lon in cs[PID]:
        if lat > north:
            north = lat
            north_cs = lat, lon
            north_PID = PID
        if lat < south:
            south = lat
            south_cs = lat, lon
            south_PID = PID
        if lon > east:
            east = lon
            east_cs = lat, lon
            east_PID = PID
        if lon < west:
            west = lon
            west_cs = lat, lon
            west_PID = PID
        else:
            continue

print('Northern most station PID =',north_PID, ', lat-lon =', north_cs)
print('Southern most station PID =',south_PID, ', lat-lon =', south_cs)
print('Eastern most station PID =',east_PID, ', lat-lon =', east_cs)
print('Western most station PID =',west_PID, ', lat-lon =', west_cs)

'''
2. In terms of geodetic distance, which stations are closest? Don’t consider stations with zero
distance, such as distance from a station to itself, or a reset marker with identical coordinates to
an older marker. Print the stations and the distance.
3. In terms of geodetic distance, which stations are furthest apart? Print the station pairs and the
distance.
'''
survey_stations = []

with arcpy.da.SearchCursor(survey_markers, ['DEC_LONG', 'DEC_LAT', 'PID', 'NAME', 'QUAD', 'POS_DATUM',
                                               'DATUM_TAG', 'ELEVATION']) as sc:
    for row in sc:
        lon = np.deg2rad(float(row[0]))  # * np.pi/180
        lat = np.deg2rad(float(row[1]))  # * np.pi/180
        PID = str(row[2])
        NAME = row[3]
        POS_DATUM = row[5]
        DATUM_TAG = row[6]
        latitude = station.Latitude(lat)
        longitude = station.Longitude(lon)
        coords = station.GeodeticCoordinates({'lat': latitude, 'lon': longitude})
        stations = station.Station(PID, NAME, coords)
        survey_stations.append(stations)
        #dist = sin(latd / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lond / 2) ** 2
        #dist = 2 * arcsin(sqrt(dist))
d_min = 10**9 #  Dont forget which is which next time : D
d_max = 0
#print('\nsurvey_stations geodetic object =', survey_stations)
for i1 in survey_stations:
    for i2 in survey_stations:
        if i1 == i2:
            continue
        d, f_az, r_az = i2.geodetic - i1.geodetic
        if d < d_min and d > 0:
            d_min = d
            close = i1, i2
        if d > d_max:
            d_max = d
            far = i1, i2
print(d, f_az, r_az)
far1 = far[0]
far2 = far[1]
close1 = close[0]
close2 = close[1]

print('\n--The stations closest to each other are:\n')
print(far1)
print(far2)
print(f' ...Separation = {d_min:0.3f} feet')

print('\n--The stations furthest from each other are:\n')
print(close1)
print(close2)
print(f' ...Separation = {d_max:0.3f} feet')
print("\nSacre bleu!   I'm finished with Module 9!!")