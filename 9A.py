"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 9 a Object Oriented Programming                     27OCT2021
"""

# import your station_A module as station
# import lib5585 as L
print('Initializing...')
import arcpy
import station_A as station
import lib5585 as L
import numpy as np
dl = 'C:/'
data_path = 'NRE_5585/Data/'
temp_path = 'NRE_5585/Temp/'
res_path = 'NRE_5585/Results/'
arcpy.env.workspace = dl + data_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')

## These statements exercise all the methods in station. My answers appear
## as comments after the print statement. Verify you get the same answers

## Use lib5585 to convert DMS from the data sheet to radians for LX3030 latitude
LX3030_lat_rad = L.from_dmss([41, 48, 44.78429, 1])

## Create an angle in radians for LX3030 latitude
LX3030_lat = station.Angle(LX3030_lat_rad, sign_strs=('N', 'S'))

## Use lib5585 to convert DMS from the data sheet to radians for LX3030 longitude
LX3030_lon_rad = L.from_dmss([72, 15, 02.04187, -1])

## Create an angle in radians for LX3030 longitude
LX3030_lon = station.Angle(LX3030_lon_rad, sign_strs=('E', 'W'))

## print longitude, latitude in radians using the __str__ method
print('radians:', LX3030_lon, LX3030_lat)  # radians: -1.26101 0.72976

## print longitude, latitude in DD using the DD method
print('DD:', LX3030_lon.DD(1), LX3030_lat.DD(1))  # DD: -72.3 41.8
print('DD:', LX3030_lon.DD(2), LX3030_lat.DD(2))  # DD: -72.25 41.81
print('DD:', LX3030_lon.DD(3), LX3030_lat.DD(3))  # DD: -72.251 41.812
print('DD:', LX3030_lon.DD(4), LX3030_lat.DD(4))  # DD: -72.2506 41.8124
print('DD:', LX3030_lon.DD(), LX3030_lat.DD())  # DD: -72.25057 41.81244

## print longitude, latitude in DMS using the DMS method
print('DMS:', LX3030_lon.DMS(), LX3030_lat.DMS())  # DMS: 072-15-02.04187 W 041-48-44.78429 N

## print longitude, latitude in DMS using the DMS method
print('DMS list:', LX3030_lon.to_dmss(), LX3030_lat.to_dmss())  # DMS list: [72.0, 15.0, 2.0418700000050194, -1] [41.0, 48.0, 44.784289999993646, 1]
print("Finished! Alert The Daily Campus!!")