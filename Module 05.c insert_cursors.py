"""
Jonathan Leonard                            NRE 5585 Python Scripting for Geospatial Analysis
Week 5 Insert cursors                       1OCT2021
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
#  Create a variable named <lyr> that holds a copy of LWDS.shp. Name the output layer LWDS_CT.SHP
#  and put it in the TEMP directory...
lyr = arcpy.CopyFeatures_management('LWDS.SHP', dl+temp_path+'LWDS_CT.SHP')

# See the manual page for arcpy.Clip_analysis()
# Assign <lyr> the value returned by arcpy.Clip_analysis(). Use <lyr> as the input features,
# TOWNS.SHP as the clip features, and LWDS_CT_clip as the output features...
lyr = arcpy.Clip_analysis(lyr, 'TOWNS.SHP', 'LWDS_CT_clip')

# In a with-statement, create a variable <ic> that is an InsertCursor for <lyr>, with
# AV_LEGEND, LWNAME, LWACTIVE for the field_names...

with arcpy.da.InsertCursor(lyr, ('AV_LEGEND', 'LWNAME', 'LWACTIVE')) as ic:
    # insert a row with your own values--not the ones I gave in the video--for the three fields
    ic.insertRow(('SPILL', 'Willimantic', 'INACTIVE'))

## Open the layer in arcpro to verify that the values have been changed
print('\nFinished!  Alert the Hartford Courant!')
