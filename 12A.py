"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 12    Numpy                                         21NOV2021
"""
## INTRO TO NUMPY

## IN THIS EXERCISE, YOU WILL ACCOMPLISH THE FOLLOWING...
##      1) CREATE TWO 3-D POINT DATA SETS
##      2) COMPUTE THE HORIZONTAL DISTANCES BETWEEN THE POINT PAIRS
##      3) COMPUTE THE SLOPE DISTANCES BETWEEN THE POINT PAIRS
##      4) COMPUTE THE SLOPES (PERCENT) BETWEEN THE POINT PAIRS
##      5) COMPUTE THE AZIMUTHS BETWEEN THE POINT PAIRS

##  Import modules
# import numpy
# import the normal random number method as 'normal'
print('Initializing...')
from numpy import rad2deg, arctan2
from numpy.random import normal
print('Ready to go!\n')

'''
## PART 1: CREATE TWO 3-D POINT DATA SETS ##
'''
# create a variable n_pts that holds the number of points to create = 20
n_pts = 20

# create and print two unit normal 3-D point sets in column orientation, so shape=(3, n_pts)
p1_col = normal(0, 1, (3, n_pts))
print('p1 Col =\n', p1_col)
p2_col = normal(0, 1, (3, n_pts))
print('p2 Col =\n', p2_col)

'''
## PART 2: COMPUTE THE HORIZONTAL (2-D) DISTANCES BETWEEN THE POINT PAIRS ##
'''
p1 = normal(0, 1, (3, n_pts))
print('p1 horizontal \n=', p1)
p2 = normal(0, 1, (3, n_pts))
print('p2 horizontal \n=', p2)

# dH involves only the x- and y-coordinates
x1 = p1[0]
y1 = p1[1]
z1 = p1[2]
x2 = p2[0]
y2 = p2[1]
z2 = p2[2]

dH = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print('\ndH =', dH)

'''
## PART 3: COMPUTE THE SLOPE (3-D) DISTANCES BETWEEN THE POINT PAIRS ##
## Extra credit (1 pt) Write a single line that will work properly regardless of how
## many dimensions the points have (i.e., it works correctly--without modification-- for
## 2-d, 3-d, 69-d, etc., points.
'''
# dS involves the x-, y-, and z-coordinates
dS = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5
print('dS =', dS)

# assert that all the slope distances are greater than the horizontal distances
assert all(dS > dH), 'Slope distance must be greater than horizontal distance'

'''
## PART 4: COMPUTE THE SLOPES (DD) BETWEEN THE POINT PAIRS ##
## SLOPE IS RISE / RUN. dH ALREADY HOLDS THE 'RUN', WHICH IS CONVENIENT
'''
# assert that all the dH values are not zero so that dividing by them doesn't cause a crash
assert (all(dH != 0)), 'Can not divide by zero'

## compute the slope as arctangent of change-in-z divided by change-in-horizontal distance between the points.
## this is a single statement
slope = (y2 - y1) / dH
slope_DD = rad2deg(slope)

## print slope in decimal degrees
print('Slope =', slope_DD)

## PART 5: COMPUTE THE AZIMUTHS BETWEEN THE POINT PAIRS IN THE RANGE[0, 360) ##
## PRINT THE AZIMUTHS AND THE X-, Y- COORDINATES OF THE LAST TWO POINTS OF YOUR DATA SETS. MAKE
## SURE YOUR ANSWER LOOKS RIGHT
p1_coords = [p1[0, -1], p1[1, -1]]

#calculate the last two points for point 2
p2_coords = [p2[0, -1], p2[1, -1]]

## RECALL THAT AZIMUTH = ARCTAN2( dx, dy )
az = arctan2(p2_coords[0] - p1_coords[0], p2_coords[1] - p1_coords[1])
print('\n')
print('Point 1 last two coordinates =', p1_coords)
print('Point 2 last two coordinates =', p2_coords)
print("\nAzimuth =", az)
print('\nFinished!  Alert Guido van Rossum!!')
