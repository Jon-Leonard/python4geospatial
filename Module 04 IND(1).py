"""
Jonathan Leonard                        NRE 5585 Python Scripting for Geospatial Analysis
Week 4 IA                               25SEP2021
"""
print('Initializing...')
import arcpy
import numpy as np
import random
dl = "C:/"
M4 = dl + "NRE_5585/Module4/"
data_path = "NRE_5585/data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.workspace = M4
arcpy.env.overwriteOutput = True
print('Ready to go!')
twopi = np.pi
#import lib5585
from lib5585 import *

## Repeat the independent assignment from Module 2 below (copy and paste is fine),

    # Y88 Northing :
Y88_GCS_n = {'degrees': 41, 'minutes': 48, 'seconds': 44.78429, 'hemisphere': 'n', 'DD': 41+(48/60)+(44.78429/3600),
             'radians': (41+(48/60)+(44.78429/3600))*(np.pi/180)}
    # Y88 Easting :
Y88_GCS_e = {'degrees': -72, 'minutes': 15, 'seconds': 02.04187, 'hemisphere': 'w', 'DD': -(72+(15/60)+(02.04187/3600)),
             'radians': (-72+(15/60)+(02.04187/3600))*(np.pi/180)}
    #Y88 GCS dictionary

Y88_GCS = {'n': Y88_GCS_n, 'e': Y88_GCS_e}

    ## Double check y88 dictionary
print('Y88 Dictionary =', Y88_GCS)

    #STORRS Northing dictionary:
STORRS_GCS_n = {'degrees': 41, 'minutes': 48, 'seconds': 53.35690, 'hemisphere': 'n', 'DD': 41+(48/60)+(53.35690/3600),
             'radians': (41+(48/60)+(53.35690/3600))*(np.pi/180)}
    #STORRS Easting dictionary:
STORRS_GCS_e = {'degrees': -72, 'minutes': 15, 'seconds': 32.96838, 'hemisphere': 'w', 'DD': -(72+(15/60)+(32.96838/3600)),
             'radians': -(72+(15/60)+(32.96838/3600))*(np.pi/180)}
    #STORRS GCS dictionary
STORRS_GCS = {'n': STORRS_GCS_n, 'e': STORRS_GCS_e}

    ## Double check Storrs dictionary
print('Storrs Dictionary =', STORRS_GCS)

## 3. a : XYZ dictionaries
Y88_XYZ = {'X': 1451423.349, 'Y': -4534399.850, 'Z': 4230204.304}

## 4. Heights dictionary
    #Y88 Heights:
Y88_h = {'ELLIP_HT': 157.285, 'ORTHO_HEIGHT': 186.843, 'GEOID_HEIGHT': -29.575, 'DYNAMIC_HEIGHT': 186.779}

    #STORRS heights:

STORRS_h = {'ORTHO_HEIGHT': 224.9, 'GEOID_HEIGHT': -29.558}   #  BN: Storrs only has 2 heights

## 5. a-c Grid coordinates
    #Y88 grid dictionaries:
Y88_grid_n = {'SPC': 261260.194, 'UTM': 4632606.690}
Y88_grid_e = {'SPC': 346299.846, 'UTM': 728378.807}
Y88_grid_ConvergeAngle_DD = {'SPC': 0+(19/60)+(52.2/3600), 'UTM': 1+(50/60)+(1.8/3600)}
Y88_grid_combinedFactor = {'SPC': 0.99997028, 'UTM': 1.00021719}
    #Y88 grid dictionary
Y88_grid = {'n': Y88_grid_n, 'e': Y88_grid_e,
            'converg': Y88_grid_ConvergeAngle_DD, 'combFac': Y88_grid_combinedFactor}

    #STORRS Grid dictionaries:
STORRS_grid_n = {'SPC': 261520.587, 'UTM': 4632848.294}
STORRS_grid_e = {'SPC': 345584.527, 'UTM': 727656.729}
STORRS_grid_Converge_DD = {'SPC': 0+(19/60)+(31.6/3600), 'UTM': 1+(49/60)+(41.4/3600)}
STORRS_grid_combinedFactor = {'SPC': 0.99996451, 'UTM': 1.00020716}
    #STORRS Grid dictionary complete
STORRS_grid = {'n': STORRS_grid_n, 'e': STORRS_grid_e,
               'converg': STORRS_grid_Converge_DD, 'combFac': STORRS_grid_combinedFactor}

## Nested dictionaries from previous dictionaries, -combined Y88 and Storrs-
Y88 = {'GCS': Y88_GCS, 'grid': Y88_grid, 'heights': Y88_h, 'XYZ': Y88_XYZ}
STORRS = {'GCS': STORRS_GCS, 'grid': STORRS_grid, 'heights': STORRS_h}

## 6 Distances
print('\n', "Distance from Y88 to Storrs")
    #a
    #UTM
de_UTM = STORRS['grid']['e']['UTM'] - Y88['grid']['e']['UTM']
dn_UTM = STORRS['grid']['n']['UTM'] - Y88['grid']['n']['UTM']
d_YS_UTM = (de_UTM**2 + dn_UTM**2)**0.5
print('\n' f"UTM grid distance = {d_YS_UTM:0.3f} meters")

#combUTM = mod4UTM_gridic/
    #SPC
de_SPC = STORRS['grid']['e']['SPC'] - Y88['grid']['e']['SPC']
dn_SPC = STORRS['grid']['n']['SPC'] - Y88['grid']['n']['SPC']
d_YS_SPC = (de_SPC**2 + dn_SPC**2)**0.5
print(f"SPC grid distance = {d_YS_SPC:0.3f} meters")

    #b
SPC_avgCombFact = (Y88['grid']['combFac']['SPC']+STORRS['grid']['combFac']['SPC'])/2
UTM_avgCombFact = (Y88['grid']['combFac']['UTM']+STORRS['grid']['combFac']['UTM'])/2
SPC_geodeticDistance = d_YS_SPC/SPC_avgCombFact
print(f"SPC geodetic distance = {SPC_geodeticDistance:0.3f} meters")
UTM_geodeticDistance = d_YS_UTM/UTM_avgCombFact
print(f"UTM geodetic distance = {UTM_geodeticDistance:0.3f} meters")

## 7 Directions
print('\n', "Direction from Y88 to Storrs")
    # a
az_YS_SPC_r = np.arctan2(de_SPC, dn_SPC)
az_YS_SPC = np.rad2deg(az_YS_SPC_r) % 360
print('\n'f"SPC grid azimuth = {az_YS_SPC:0.4f} degrees")

mod4SPC_dir = azimuth([STORRS['grid']['e']['SPC'], STORRS['grid']['n']['SPC']], [Y88['grid']['e']['SPC'], Y88['grid']['n']['SPC']])

az_YS_UTM_r = np.arctan2(de_UTM, dn_UTM)
az_YS_UTM = np.rad2deg(az_YS_UTM_r) % 360
print(f"UTM grid azimuth = {az_YS_UTM:0.4f} degrees")

mod4UTM_dir = azimuth([STORRS['grid']['e']['UTM'], STORRS['grid']['n']['UTM']], [Y88['grid']['e']['UTM'], Y88['grid']['n']['UTM']])

    # b
SPC_avgConvergeAngle = (Y88['grid']['converg']['SPC']+STORRS['grid']['converg']['SPC'])/2
UTM_avgConvergeAngle = (Y88['grid']['converg']['UTM']+STORRS['grid']['converg']['UTM'])/2
SPC_geodeticAzimuth = az_YS_SPC + SPC_avgConvergeAngle
print(f"SPC geodetic azimuth = {SPC_geodeticAzimuth:0.4f} degrees")
UTM_geodeticAzimuth = az_YS_UTM + UTM_avgConvergeAngle
print(f"UTM geodetic azimuth = {UTM_geodeticAzimuth:0.4f} degrees")


## but then doing the distance and azimuth computations using
## your functions you implemented in lib5585, imported above.
print("\nLet's test to see if it works...")
x = from_dmss([72, 15, 02.04187, -1], 'dd')
print('Drumroll please...........', x)
print('\nMoving on with Module 4\n')

mod4UTM_gridic = distance([STORRS['grid']['e']['UTM'], STORRS['grid']['n']['UTM']], [Y88['grid']['e']['UTM'], Y88['grid']['n']['UTM']], True)
mod4SPC_gridic = distance([STORRS['grid']['e']['SPC'], STORRS['grid']['n']['SPC']], [Y88['grid']['e']['SPC'], Y88['grid']['n']['SPC']], True)

## Distance
storrs_UTM = mod4UTM_gridic
print(f"UTM Storrs to Y88 grid distance = {storrs_UTM:0.3f} meters")

storrs_SPC = mod4SPC_gridic
print(f"SPC Storrs to Y88 grid distance = {storrs_SPC:0.3f} meters")

geodistUTM = storrs_UTM/UTM_avgCombFact
geodistSPC = storrs_SPC/SPC_avgCombFact

print(f"UTM Storrs to Y88 geodetic distance = {geodistUTM:0.3f} meters")
print(f"SPC Storrs to Y88 geodetic distance = {geodistSPC:0.3f} meters")

## Azimuth

###########
'''
print('\n', "Direction from Y88 to Storrs")
    # a
az_YS_SPC_r = np.arctan2(de_SPC, dn_SPC)
az_YS_SPC = np.rad2deg(az_YS_SPC_r) % 360
print('\n'f"SPC grid azimuth = {az_YS_SPC:0.4f} degrees")
'''
## SPC
mod4SPC_dir = azimuth([Y88['grid']['e']['SPC'], Y88['grid']['n']['SPC']],
                      [STORRS['grid']['e']['SPC'], STORRS['grid']['n']['SPC']])
#print(mod4SPC_dir)

storrs_SPCaz = to_dmss(mod4SPC_dir)
#print(storrs_SPCaz)
storrs_SPCaz_dd = from_dmss(storrs_SPCaz, 'decimal degree')
print(" \nSPC grid azimuth =", storrs_SPCaz_dd)
'''
az_YS_UTM_r = np.arctan2(de_UTM, dn_UTM)
az_YS_UTM = np.rad2deg(az_YS_UTM_r) % 360
print("UTM grid azimuth =", az_YS_UTM)
'''
## UTM
mod4UTM_dir = azimuth([Y88['grid']['e']['UTM'], Y88['grid']['n']['UTM']],
                      [STORRS['grid']['e']['UTM'], STORRS['grid']['n']['UTM']])
#print(mod4UTM_dir)

storrs_UTMaz = to_dmss(mod4UTM_dir)
#print(storrs_UTMaz)
storrs_UTMaz_dd = from_dmss(storrs_UTMaz, 'decimal degree')
print("UTM grid azimuth =", storrs_UTMaz_dd)

## geodetic

mod4UTM_dir = azimuth([Y88['grid']['e']['UTM'], Y88['grid']['n']['UTM']],
                      [STORRS['grid']['e']['UTM'], STORRS['grid']['n']['UTM']], converg=UTM_avgConvergeAngle*(np.pi/180))
storrs_UTMaz = to_dmss(mod4UTM_dir)
storrs_UTMaz_dd = from_dmss(storrs_UTMaz, 'decimal degree')
print("UTM Geodetic azimuth =", mod4UTM_dir, "degrees")


mod4SPC_dir = azimuth(p_to=[Y88['grid']['e']['SPC'], Y88['grid']['n']['SPC']],
                      p_from=[STORRS['grid']['e']['SPC'], STORRS['grid']['n']['SPC']], converg=SPC_avgConvergeAngle*(np.pi/180))
storrs_SPCaz = to_dmss(mod4SPC_dir)
storrs_SPCaz_dd = from_dmss(storrs_SPCaz, 'decimal degree')
print("SPC Geodetic azimuth =", mod4UTM_dir, "degrees")

print("Signing off of Module 4 IA")