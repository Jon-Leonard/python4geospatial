"""
Module 1b
"""
## WORKING WITH STRINGS

## IN THIS EXERCISE, YOU WILL PERFORM THE FOLLOWING...
##      ASSIGN VARIABLES TO FILES AND WORKSPACES
##      USE VARIABLE SUBSTITUTION TO DEFINE A FILE
##      USE VARIABLE SUBSTITUTION TO CREATE A SELECTION EXPRESSION
##      PERFORM A SELECTION WITH THE SELECT TOOL

##-------------------------------------------------------------
## PART 1: IMPORT MODULES...

# import the arcpy module...
print('begin initialization')
import arcpy

##-------------------------------------------------------------
## PART 2: DEFINE INPUT FILE USING VARIABLE SUBSTITUTION

# assign a variable to hold your drive letter...
dl = 'C:/'

# assign variables to hold the path to the data folder, temp folder, and results folder...
data_path = dl + 'NRE_5585/data/'
temp_path = dl + 'NRE_5585/temp/'
res_path = dl + 'NRE_5585/results/'

print('path', data_path)
arcpy.env.workspace = data_path  # set the working directory to the data directory

features_fns = arcpy.ListFeatureClasses()  # produce a list of file names for the feature classes
print(features_fns)

# assign a variable to hold the full path and filename for towns.shp.
towns_fn = data_path + 'towns.shp'  # full path to towns.shp

# allow outputs to be overwritten...
arcpy.env.overwriteOutput = True

##-------------------------------------------------------------
## PART 3: PERFORM SELECTION ON towns.shp

##----------------
## DEFINE VARIABLES FOR THE FIELD NAME AND FIELD VALUE...

##----------------
## CREATE SELECTION EXPRESSION

# create variable holding a template string for a SQL equality where-clause.
# Equality where-clauses for strings have the form "<attribute_name> = '<value>'"
# See slides for an example

where_template = "{} = '{}'"

# field name variable...
field = "Town"

# field value variable...
town_nm = "Haddam"

# using string substitution (.format()) with the template variable above, create a variable holding a string
# for the expression Town = 'Haddam'

where = where_template.format(field, town_nm)
print(where)
arcpy.SelectLayerByAttribute_management(towns_fn, where_clause=where)

# write a Select_analysis ArcTool statement with...
#   1) <towns_fn> as in_features (remember to use variable defined above)
#   2) use your variables to create output file name with ".shp" extension in the results folder
#   3) use <where> for selection parameter.
#   n.b. this is arcpy.Select_analysis(...), not SelectLayerByAttribute; see documentation for details
arcpy.Select_analysis(towns_fn, res_path + 'haddam.shp', where)

##-----------------
## DEMONSTRATING THE BENEFITS OF VARIABLE SUBSTITUTION

# change the value of <town_nm> to Mansfield, change <where> to the new value, and execute the selection again.
town_nm = "Mansfield"
where = where_template.format(field, town_nm)
arcpy.Select_analysis(towns_fn, res_path + 'mansfield.shp', where)

## CHECK THE RESULTS IN ARCPRO. Submit screenshots of the two outputs.
## LATER, WE WILL SEE HOW THE SCRIPT CAN REQUEST VALUES FOR VARIABLES WHEN IT IS RUN