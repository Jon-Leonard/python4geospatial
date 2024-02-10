"""
Jonathan Leonard                            NRE 5585 Python Scripting for Geospatial Analysis
Module 2e Dictionaries and Describe         5SEP2021
"""
## WORKING WITH DICTIONARIES AND ARCPY.DA.DESCRIBE()

## IN THIS EXERCISE, YOU WILL PERFORM THE FOLLOWING...
##      USE arcpy.da.Describe() to retrieve the description dictionary of a raster
##      EXTRACT AND PRINT VARIOUS INTERESTING ITEMS FROM THE DESCRIPTION
print("initializing")

## IMPORT ARCPY, SET THE ENVIRONMENTAL VARIABLES AND PATH VARIABLES
import arcpy
dl = 'C:/'
data_path = "NRE_5585/Data/"
arcpy.env.workspace = dl + data_path
arcpy.env.overwriteOutput = True

## INVOKE arcpy.da.Describe ON landcover.img IN THE data DIRECTORY
desc = arcpy.da.Describe("landcover.img")
print(desc)

## EXTRACT THE extent VALUE FROM desc AND STORE IT IN bb (bounding box)
bb = desc['extent']

## PRINT bb. NOTICE THAT IT PRINTS AS A LIST
print(bb)

## PRINT THE XMin VALUE FROM bb. NOTICE THAT WE CANNOT USE SUBSCRIPTING ON bb EVEN THOUGH IT PRINTS AS A LIST
## THE extent VALUE IN THE DESCRIPTION DICTIONARY IS AN OBJECT, NOT A LIST. LATER WE'LL SEE HOW TO CREATE
## CUSTOM PRINTING REPRESENTATIONS LIKE THIS FOR OUR OWN OBJECTS.
print(bb.XMin)

## PRINT height, width. ASSIGN THESE TO nrows AND ncols. ARCPY IS USING THE TERM height TO MEAN THE EXTENT IN THE
## NORTH-SOUTH DIRECTION. RASTERS ARE OFTEN, BUT NOT ALWAYS, STORED IN ROW-MAJOR FORM, SO I PREFER TO CALL THIS
## nrows INSTEAD OF height, WHICH I ASSOCIATE WITH ELEVATION, HEIGHT ABOVE SOME DATUM
nrows = desc['height']
ncols = desc['width']

## PRINT meanCellWidth, meanCellHeight. ASSIGN THESE TO dx AND dy. HERE, "width" MEANS THE PIXELS' SPATIAL EXTENT
## IN THE EASTING DIRECTION, AND "height" IS THE SPATIAL EXTENT IN THE NORTHING DIRECTION. ONE IS TEMPTED TO ADOPT
## MORE SPATIAL AND LESS ABSTRACT NOTATION, LIKE de AND dn. HOWEVER, arcpy IN CONSISTENT IN USING X AND Y NOTATION,
## SO LET'S STICK TO THAT FOR CONSISTENCY'S SAKE. HOWEVER, WE'LL ABANDON THE NOTION THAT "HEIGHT" IS ASSOCIATED WITH
## NORTH-SOUTH AND "WIDTH" WITH EAST-WEST.
dx = desc['meanCellWidth']
dy = desc['meanCellHeight']

## Print number of rows/columns and mean cell width/height
print(f'Number of rows = {nrows}')
print(f'Number of columns = {ncols}')
print(f'meanCellWidth = dx = {dx}')
print(f'meanCellHeight = dy = {dy}')

## PRINT noDataValue AND ASSIGN IT TO ndv. PIXELS WHOSE VALUE IS THE noDataValue HAVE NO VALUE AND USUALLY NEED
## SPECIAL TREATMENT WHEN WE DO THINGS WITH THE RASTER.
ndv = desc['noDataValue']
print(f'noDataValue = dnv = {ndv}')

## PRINT pixelType AND ASSIGN IT TO pixelType. RASTERS OFTEN HAVE NON-PYTHONIC DATA TYPES. IF THEY DO, WE USUALLY
## NEED TO CAST THEM TO A NATIVE PYTHON DATA TYPE BEFORE USING THEM.
pixelType = desc['pixelType']
print(f'pixelType = {pixelType}')

## PRINT spatialReference AND ASSIGN IT TO sr. THE spatialReference OBJECT HAS ALL THE SPATIAL COORDINATE
## SYSTEM INFORMATION ABOUT THIS RASTER. THE spatialReference OBJECT HAS FOUR ATTRIBUTES OF PARTICULAR NOTE
sr = desc['spatialReference']
print(f'spatialReference = sr = {sr}')

## PRINT sr.PCSName. THIS IS THE FULL NAME OF THE COORDINATE SYSTEM. IF THIS IS A GEOGRAPHIC COORDINATE SYSTEM,
## LIKE WGS84 OR NAD83, THEN THAT WILL BE THE NAME. IF THIS IS A PROJECTED COORDINATE SYSTEM, LIKE SPC83, THEN
## THAT WILL BE THE NAME AND THE DATUM IS STORED FURTHER DOWN IN THE sr OBJECT
print(sr.PCSName)

## PRINT sr.PCSCode. THIS IS USEFUL FOR SETTING THE SPATIAL REFERENCE OF NEW OBJECTS
print(sr.PCSCode)

## PRINT sr.linearUnitName. WE MUST ALWAYS BE MINDFUL OF UNITS. SPATIAL DATA COME IN MY DIFFERENT UNITS AND WE MUST
## NOT MIX THEM
print(sr.linearUnitName)

## PRINT sr.metersPerUnit. THIS IS THE ARCPY CONVERSION FROM THE LINEAR UNIT TO METERS. WE ALREADY HAVE DEFINED THE
## PROPER CONVERSION VALUES IN A PREVIOUS EXERCISE, BUT IT CAN BE HANDY TO HAVE THIS HERE.
print(sr.metersPerUnit)