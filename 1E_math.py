"""
Your comment block goes here
"""
## DISTANCE AND AZIMUTH COMPUTATIONS

## IN THIS EXERCISE, YOU WILL PERFORM THE FOLLOWING...
##      CREATE VARIABLES HOLDING UNIT-CONVERSION FACTORS
##		USE THOSE VARIABLES TO PERFORM SOME UNIT CONVERSIONS
##		USING THE FORMULA d = R theta, COMPUTE SOME DISTANCES ON A SPHERICAL EARTH

# Import numpy as np...

import numpy as np

# Copy your variables defining the conversions from USFt to meters and IntFt to meters here

##-------------------------------------------------------------
## PART 1: PLANIMETRIC DISTANCE COMPUTATIONS
## THESE ARE THE COORDINATES FOR TWO SURVEY
## CONTROL MARKERS, Y88 AND STORRS, ON THE UCONN STORRS CAMPUS.
## THEY ARE GIVEN IN BOTH THE STATE PLANE COORDINATE SYSTEM 1983 (SPC83) AND
## UNIVERSAL TRANSVERSE MERCATOR (UTM)
## CREATE AN ARCPRO PROJECT WITH A SURVEY MARKER POINT FEATURE CLASS IN
## SPC83, THEN PUT THESE TWO FEATURES INTO THE FEATURE CLASS SO YOU CAN
## VISUALIZE THEIR SPATIAL RELATIONSHIP AND GEOGRAPHIC SETTING.

Y88_e_SPC   = 346299.846  # m
Y88_n_SPC   = 261260.194  # m

STORRS_e_SPC   = 345584.527  # m
STORRS_n_SPC   = 261520.587  # m

Y88_e_UTM   =  728378.807  # m
Y88_n_UTM   = 4632606.690  # m

STORRS_e_UTM   =  727656.729  # m
STORRS_n_UTM   = 4632848.294  # m

"""
Grid distances
"""

# USING PYTHAGORAS'S FORMULA, COMPUTE THE SPC DISTANCE (METERS) BETWEEN Y88 AND STORRS...
de_spc = STORRS_e_SPC - Y88_e_SPC
dn_spc = STORRS_n_SPC - Y88_n_SPC
d_YS_SPC =(de_spc**2 + dn_spc**2)**0.5

# PRINT THE DISTANCE TO THE MILLIMETER

print(f"There are {d_YS_SPC:0.3f} meters from Storrs to Y88")
# COMPUTE THE UTM DISTANCE (METERS) BETWEEN Y88 AND STORRS...
de_utm = STORRS_e_UTM - Y88_e_UTM
dn_utm = STORRS_n_UTM - Y88_n_UTM

d_YS_UTM =(de_utm**2 + dn_utm**2)**0.5

# PRINT THE DISTANCE TO THE MILLIMETER
print(f"There are {d_YS_UTM:0.3f} meters from Storrs to Y88")

########################################################################################################
## Extra credit: do the following for one addition point of credit.
## It happens that UTM northings given (approximately) the number of meters
## from the Equator along a meridian to the point.
## Get the value for Earth's Equatorial radius, stored in the variable <a> in the previous assignment.
## Using a spherical Earth model and the radius value given above <a>, what is Y88's latitude?
## lat = northing / a
## is the right formula. lat will be in radians. Use np.rad2deg() to convert to decimal degrees.
## NGS gives Y88's latitude as 041-48-44.78429 == 41.81244 deg.
## One source of difference between our approximation the NGS value is that meridians are ellipses, not circles,
## so lat = northing / a isn't quite the right formula. Still this is a handy way to get an approximate latitude
## very easily from a UTM northing

#######################################################################################################

##-------------------------------------------------------------
## PART 2: PLANIMETRIC AZIMUTH COMPUTATIONS

"""
Grid azimuths
"""

# Compute the change in eastings and the change in northings from Y88 to STORRS in SPC83...
deSPC = STORRS_e_SPC - Y88_e_SPC
dnSPC = STORRS_n_SPC - Y88_n_SPC
print("Change in easting, ", deSPC)
print("Change in northing, ", dnSPC)


# Use the np.arctan2() function to compute the azimuth from Y88 to STORRS. NB np.arctan2() returns radians...
az = az_YS_SPC_r = np.arctan2(deSPC, dnSPC)
print("(SPC), The azimuth is, ", az, "radians")
az = np.rad2deg(az)
# Use np.rad2deg() to conver to decimal degrees. Use the mod operator to map to [0..360]...
az_YS_SPC = np.rad2deg(az_YS_SPC_r) % 360
# Print the azimuth to four significant digits...
print(f"(SPC), The azimuth is,  {az_YS_SPC:0.4f} degrees ")
# Repeat for the UTM coordinates

# Compute the change in eastings and the change in northings from Y88 to STORRS in utm...
deUTM = STORRS_e_UTM - Y88_e_UTM
dnUTM = STORRS_n_UTM - Y88_n_UTM
print("Change in easting, ", deUTM)
print("Change in northing, ", dnUTM)


# Use the np.arctan2() function to compute the azimuth from Y88 to STORRS. NB np.arctan2() returns radians...
azUTM = az_YS_UTM_r = np.arctan2(deUTM, dnUTM)
print("(UTM), The azimuth is, ", az, "radians")
azUTM = np.rad2deg(azUTM)
# Use np.rad2deg() to conver to decimal degrees. Use the mod operator to map to [0..360]...
az_YS_UTM = np.rad2deg(az_YS_UTM_r) % 360
# Print the azimuth to four significant digits...
print(f"(UTM), The azimuth is,  {az_YS_UTM:0.4f} degrees ")