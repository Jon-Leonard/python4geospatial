"""
Jonathan Leonard                            NRE 5585 Python Scripting for Geospatial Analysis
Week 5 Update cursors                       1OCT2021
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
lyr = arcpy.CopyFeatures_management('LWDS.shp', dl+temp_path+'LWDS_CT.SHP')

# See the manual page for arcpy.Clip_analysis()
# Assign <lyr> the value returned by arcpy.Clip_analysis(). Use <lyr> as the input features,
# TOWNS.SHP as the clip features, and LWDS_CT_clip as the output features...
lyr = arcpy.Clip_analysis(lyr, 'TOWNS.SHP', 'LWDS_CT_clip')

fields = [f.name for f in arcpy.ListFields(lyr)]
print(fields) # kept getting errors so went back to verify the field exists. Turns out I simply misspelled DESCRIP later on

# In a with-statement, create a variable <uc> that is an UpdateCursor for <lyr>, with DESCRIP for the field_name...
with arcpy.da.UpdateCursor(lyr, 'DESCRIP') as uc:

    #  for each row in <uc>...
    for row in uc:
        #  strip the description of white space using the string strip() method
        if row[0].strip() == '':
        #  if the description is the empty string...

            #  update the description to the value '--none--'
            uc.updateRow(['--none--'])

## Open the layer in arcpro to verify that the values have been changed
print("Finished. Alert the New Haven Register! ")
