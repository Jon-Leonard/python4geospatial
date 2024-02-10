"""
Jonathan Leonard                            NRE 5585 Python Scripting for Geospatial Analysis
Week 5 Search Cursors                       1OCT2021
"""

## INITIALIZE YOUR SCRIPT WITH IMPORTS, DRIVE LETTER, PATHS, ETC.
print('Initializing...')
import arcpy
dl = "C:/"
data_path = "NRE_5585/data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.workspace = dl + data_path
arcpy.env.overwriteOutput = True
print('Ready to go!')

## SOME OF THE POINTS IN THE LWDS FEATURE CLASS LAY OUTSIDE OF CONNECTICUT.
## WE WILL CLIP LWDS TO THE TOWNS FEATURE CLASS TO REMOVE THE POINTS OUTSIDE
## CONNECTICUT.

#  See the manual page for arcpy.CopyFeatures_management().
#  We must not make changes to anything in the Data directory, so we start by making a
#  copy of LWDS.shp.
#  Create a variable named <lyr> that holds a copy of LWDS.shp.
#  Use LWDS.shp as the value for in_features, and name the out_feature_class LWDS_CT.SHP
#  and put it in the TEMP directory...
lyr = arcpy.CopyFeatures_management('LWDS.shp', dl+temp_path+'LWDS_CT.SHP')

# See the manual page for arcpy.Clip_analysis()
# Re-assign <lyr> to be the value returned by arcpy.Clip_analysis(). Use <lyr> as the input features,
# TOWNS.SHP as the clip features, and LWDS_CT_clip as the output features...
lyr = arcpy.Clip_analysis(lyr, dl+data_path+'TOWNS.SHP', dl+temp_path+'LWDS_CT_clip')

# Create a dictionary to group AV_LEGEND values by the values in LWFLOW ...
grp = {'GROUND': [], 'SURFACE': []}

# In a with-statement, create a variable <sc> that is a SearchCursor for <lyr> with 'AV_LEGEND','LWFLOW' for the field names...
with arcpy.da.SearchCursor(lyr, ['AV_LEGEND', 'LWFLOW']) as sc:

    #  for each row in <sc>, append the AV_LEGEND value to the list in the dictionary...
    for row in sc:
        grp[row[1]].append(row[0])

# Print the number of AV_LEGEND values in each LWFLOW group...
print("\nGround values = ", len(grp['GROUND']))
print("Surface values = ", len(grp['SURFACE']))
print("\nFinished! Alert The New York Times!")