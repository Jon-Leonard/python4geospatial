"""
Your comment block goes here
"""
## BASIC COMPUTATIONS

## IN THIS EXERCISE, YOU WILL PERFORM THE FOLLOWING...
##      CREATE VARIABLES HOLDING UNIT-CONVERSION FACTORS
##		USE THOSE VARIABLES TO PERFORM SOME UNIT CONVERSIONS
##		USING THE FORMULA d = R theta, COMPUTE SOME DISTANCES ON A SPHERICAL EARTH

# Import numpy as np

import numpy as np

##-------------------------------------------------------------
## PART 1: LINEAR UNIT CONVERSIONS

one_mile = 5280  # number of feet per mile

USFt = 3937 / 1200   # multiply a distance in US Feet by this value to convert to meters

# Multiply meters by 1 / (2.54 cm/in * 12 in/ft * 1 m / 100 cm) to get International Feet

IntFt = 1.0 / (2.54 * 12 * 1 / 100)  # (2.54 cm/in * 12 in/ft * 1 m / 100 cm)

## multiply meters by these factors to get feet.

km = 1000.0  # one kilometer is 1000 m

ift_per_km = km * IntFt

# Print to the millimeter the number of International Feet per km...

print(f"There are {ift_per_km:0.3f} International Feet per km")

## divide feet by these factors to get meters

m_per_US_mile = one_mile / USFt

# Print to the millimeter the number of meters per mile of US Feet...
print(f"There are {m_per_US_mile :0.3f} meters per mile of Us Feet")

# Print to the millimeter the number of meters per mile of IntFt...
intfeet_mile = m_per_US_mile * IntFt          # very confused on this one : /
print(f"There are {intfeet_mile:0.3f} meters per mile of International Feet")

"""
THE GENERALLY ACCEPTED VALUE FOR EARTH'S EQUATORIAL RADIUS IS 6,378,137 METERS
Mortiz, H. (1980) "Geodetic reference system 1980 (GRS80)." Bulletin Geodesique 54.
"""

a = 6378137  # meters, Equatorial radius

"""
The following is one value, among many other reasonable choices,
for Earth's mean radius taking into account its spheroidal shape
"""

aAvg = 6367449.145771048  # meters, mean value

## TREATING A MERIDIAN AS A CIRCLE WHOSE RADIUS IS EARTH'S MEAN RADIUS,
## COMPUTE THE DISTANCE FROM THE EQUATOR TO THE POLES USING THE MEAN EARTH RADIUS VALUE.
# The formula for the circumference of a circle is 2 * pi * r, where r is the 
# radius of the circle. The distance from the Equator to either pole is 1/4 of a circle.
# Get the value for pi from np.pi

circ = 2 * np.pi * aAvg
hq = 1/4 * circ
print(f"Distance from the Equator to either Pole is {hq:0.3f} meters")

# Print to the millimeter the distance from the Equator to either Pole in International Feet
print(f"Distance from the Equator to either Pole is {hq* IntFt:0.3f} International feet")

# Print to the millimeter the distance from the Equator to either Pole in US Feet
print(f"Distance from the Equator to either Pole is {hq* USFt:0.3f} US feet")

## NOTICE THAT THE DISTANCE IS VERY NEARLY 10,000,000 m. THIS IS THE ORIGINAL
## DEFINITION OF THE METER: 1/10,000,000 THE DISTANCE FROM THE EQUATOR TO THE POLES

#######################################################################################################
## Extra credit: do the following for one addition point of credit.
## One nautical mile is 2025 yards, and there are three feet per yard (of course).
## Geographic coordinates (longitude and latitude) are often given in units of Degrees-Minutes-Seconds (DMS).
## There are 60 arc minutes in a degree, same as 60 minutes in an hour.
## There are 60 arc seconds in a minute, same as 60 seconds in a minute of time.
## The distance along a circular arc is given by d = r theta where theta is the subtended angle in radians.
## Convert one minute of arc into nautical miles. Print to two significant digits.
## (When you see the answer, you will now understand how the nautical mile is defined)
#yard = 3 # feet per yard
#naut_mile = 2025 # yards in nauticle mile

#print('One arc-minute along the Equator or a meridian equals {:0.2f} nautical miles'.format(d_nm))

#######################################################################################################

