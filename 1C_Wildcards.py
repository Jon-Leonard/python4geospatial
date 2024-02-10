"""
NRE5585 Module 1B
WILD CARDS AND ARCPY.LISTFEATURES
"""

## IN THIS EXERCISE, YOU WILL PERFORM THE FOLLOWING...
##      USE ARCPY.LISTFEATURECLASS WITH AND WITHOUT WILDCARDS

##-------------------------------------------------------------
## PART 1: CREATE THE GEOPROCESSOR...

# import the arcpy module...
print('begin initialization')
import arcpy
# create variables for the drive letter and the path to the Data directory

dl = 'C:/'
data_path = dl + 'NRE_5585/data/'

# set the arcpy environmental variables for overwriting as True...
# and the workspace is the data directory...
arcpy.env.overwriteOutput = True
arcpy.env.workspace = data_path
# use arcpy.ListFeatureClasses() to get a list of the names in the Data directory
# for feature classes...

fc_lst = arcpy.ListFeatureClasses()

# print the list
print("Files that are feature class are as follows.\n", fc_lst)

# use arcpy.ListFeatureClasses() with a wildcard string to get a list of the
# names in the Data directory for feature classes whose name begins with the letter t
fc_t_lst = arcpy.ListFeatureClasses('t*')
# print the list
print("Files that begin with the letter 't' are as follows.\n", fc_t_lst)
