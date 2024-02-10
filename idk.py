"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 12     Numpy                                        2NOV2021
"""

print("DON'T PANIC!\n")
#'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.' -Douglas Adams

## INITIALIZE YOUR SCRIPT WITH IMPORTS, DRIVE LETTER, PATHS, ETC.
print('Beginning initialization. . .\n')
#'A beginning is the time for taking the most delicate care that the balances are correct' - Frank Herbert

## PART 1: CREATE TWO 3-D POINT DATA SETS ##
print('Importing modules. . .')
# import numpy as np. . .
import numpy as np

# import the normal random number method as 'normal'
from numpy.random import normal
print('Modules imported.\n')

print('initiation successful!\n')

# create a variable n_pts that holds the number of points to create = 20
n_pts = 20

# create and print two unit normal 3-D point sets in column orientation, so shape=(3, n_pts)
#I got stuck here for about an hour. shape=  returns errors, so I googled the literature and found
#that it wasn't necessary, apparently. Putting 3 in the first position and n_pts in the 2md gave me 3 20D point sets,
# instead of 20 3D point sets.
#by switching them, I get 20 rows of 3 coulmns.. I'm not sure if this is correct but it is the only thing that
#looks at all like the video.
p1_long = normal(0, 1, (n_pts, 3))
print(f'p1 long:\n{p1_long}\n')
p2_long = normal(0, 1, (n_pts, 3))
print(f'p2 long:\n{p2_long}\n')
## PART 2: COMPUTE THE HORIZONTAL (2-D) DISTANCES BETWEEN THE POINT PAIRS ##
p1 = normal(0, 1, (3, n_pts))
print(f'p1 wide:\n{p1}\n')
p2 = normal(0, 1, (3, n_pts))
print(f'p2 wide:\n{p2}\n')

#point variables
x1 = p1[0]
y1 = p1[1]
z1 = p1[2]
x2 = p2[0]
y2 = p2[1]
z2 = p2[2]

# dH involves only the x- and y-coordinates
#always look at the full instructions before typing the code.
dH = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'dH:\n{dH}\n')


## PART 3: COMPUTE THE SLOPE (3-D) DISTANCES BETWEEN THE POINT PAIRS ##
## Extra credit (1 pt) Write a single line that will work properly regardless of how
## many dimensions the points have (i.e., it works correctly--without modification-- for
## 2-d, 3-d, 69-d, etc., points.

# dS involves the x-, y-, and z-coordinates
dS = np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
print(f'dS:\n{dS}\n')


# assert that all the slope distances are greater than the horizontal distances

#It's highlighting the assert in yellow, but runs with it. The Value Error is why I'm using all.
#ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
assert all(dS > dH), "You might want to go check your math..."

## PART 4: COMPUTE THE SLOPES (DD) BETWEEN THE POINT PAIRS ##
## SLOPE IS RISE / RUN. dH ALREADY HOLDS THE 'RUN', WHICH IS CONVENIENT

# assert that all the dH values are not zero so that dividing by them doesn't cause a crash
#all dH are not equal to zero.
assert (all(dH != 0)), "Someone tried to divide by zero..."

## compute the slope as arctangent of change-in-z divided by change-in-horizontal distance between the points.
## this is a single statement
slope = (y2 - y1) / dH
slopeDD = np.rad2deg(slope)

## print slope in decimal degrees
print(f'slope:\n{slopeDD}\n')


## PART 5: COMPUTE THE AZIMUTHS BETWEEN THE POINT PAIRS IN THE RANGE[0, 360) ##
## RECALL THAT AZIMUTH = ARCTAN2( dx, dy )

#calculate teh last two points for point 1
p1coords = [p1[0, -1], p1[1, -1]]
#calculate the last two points for point 2
p2coords = [p2[0, -1], p2[1, -1]]
#calculate the azimuth
az = np.arctan2(p2coords[0] - p1coords[0], p2coords[1] - p1coords[1])

## PRINT THE AZIMUTHS AND THE X-, Y- COORDINATES OF THE LAST TWO POINTS OF YOUR DATA SETS. MAKE
## SURE YOUR ANSWER LOOKS RIGHT

print(f'the X and Y coordinates of the last two  points in P1 are: {p1coords}')
print(f'the X and Y coordinates of the last two  points in P2 are: {p2coords}')
print(f'The azimuth of the two last points in the datasets is: {az:0.04f}\n')

print('\n\nIndependent activity 12 complete!\n\n"The best error message is the one that never shows up." - Thomas Fuchs.')


#"Everything not saved will be lost." -Nintendo Quit screen