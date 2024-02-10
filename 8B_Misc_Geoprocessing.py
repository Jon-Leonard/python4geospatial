"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 8 b Geoprocessing                                   24OCT2021
"""

## INTRO TO GEOPROCESSING

## IN THIS EXERCISE, YOU WILL ACCOMPLISH THE FOLLOWING...
##      1) SET UP ARCPY; DEFINE VARIABLES FOR INPUT DATA
##      2) USE ARCTOOLS TO PERFORM GEOPROCESSING

##---------------------------------------------------------------------

## PART 1: SET UP A GEOPROCESSING SCRIPT ##

## IMPORT MODULES, CREATE AND SET UP ARCPY...
print('Initializing...')
import arcpy
dl = 'C:/'
data_path = 'NRE_5585/Data/'
temp_path = 'NRE_5585/Temp/'
res_path = 'NRE_5585/Results/'
arcpy.env.workspace = dl + data_path
arcpy.env.overwriteOutput = True
print('Ready to go!\n')

# assign variables to "middlesexsoils.shp" and "towns.shp" in the Data folder...
soils = dl + data_path + "middlesexsoils.shp"
towns = dl + data_path + "towns.shp"
town_soils = dl + res_path + 'town_soils.SHP'

# set the default geoprocessor workspace to your "Results" folder... 
arcpy.env.workspace = dl + res_path

### ---------------------------------------------------------------------
## PART 2: WORKING WITH ARCTOOLS...

##---------------------
## CREATE LAYER CONTAINING TOWN OF HADDAM...
# lyr = 'HADDAM.SHP'
# selection expression for the following Make Feature Layer tool statement...
expression = "TOWN = 'Haddam'"

# Make Feature Layer tool: use towns for input; "town_lyr" for output; variable in previous line for expression...
lyr = arcpy.MakeFeatureLayer_management(towns, 'town_lyr', expression)

##---------------------
## CLIP THE SOILS FILE TO THE "town_lyr" FILE...

# Clip tool: use soils (input); "town_lyr" (clip file); "town_soils.shp" (output) 
arcpy.analysis.Clip(soils, 'town_lyr', 'town_soils.shp')

##---------------------
## CREATE LAYER CONTAINING HYDRIC SOILS FROM "town_soils.shp"

# selection expression for the following Make Feature Layer tool statement...
hydric = "Hydric = 'Yes'"

# Make Feature Layer tool: "town_soils.shp" (input); "town_wetland_lyr" (output); variable in previous line for expression... 
arcpy.management.MakeFeatureLayer(town_soils, "town_wetland_lyr", hydric)

##---------------------
## BUFFER "town_wetland_lyr" BY 100 FEET...

# Buffer tool: "town_wetland_lyr" (input); "wetland_buf.shp" (output); "100 FEET" (distance); "ALL" (dissolve option)... 
arcpy.analysis.Buffer('town_wetland_lyr', "wetland_buf.shp", "100 FEET", "FULL")  # 'ALL' is not acceptable.

##---------------------
## ADD "Area" FIELD TO "wetland_buf.shp"...

# Add Field tool: "wetland_buf.shp" (input); "Area" (field name); "DOUBLE" (field type)... 
arcpy.management.AddField("wetland_buf.shp", 'Area', 'DOUBLE')

##---------------------
## ADD "Area" and "Perimeter" FIELDS TO "wetland_buf.shp"...
arcpy.management.AddField("wetland_buf.shp", 'Perimeter', 'DOUBLE')

## Use arcpy.management.CalculateGeometryAttributes() to add an attribute column named 'area' that holds the polygon's
## area (AREA) in hectares and 'perimeter' that holds the polygon's perimeter's length (PERIMETER_LENGTH) in meters.
arcpy.management.CalculateGeometryAttributes("wetland_buf.shp", [['AREA', 'AREA'], ['Perimeter', 'PERIMETER_LENGTH']],
                                             length_unit='METERS', area_unit='HECTARES')
##---------------------
## INDICATE THAT SCRIPT HAS FINISHED...

# print message to interactive window...
print("Finished!\nAlert my fellow Geoprocessors!")