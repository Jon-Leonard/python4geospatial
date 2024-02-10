"""
Jonathan Leonard                        NRE 5585 Python Scripting for Geospatial Analysis
Week 4 Defining functions               25SEP2021
"""
###########################################################
## PART 1: INITIALIZATION

# import whatever modules you need
print('Initializing...')
import arcpy
import numpy as np
import random
dl = "C:/"
data_path = "NRE_5585/data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.workspace = res_path
arcpy.env.overwriteOutput = True
print('Ready to go!')

###########################################################
## PART 2: WRITE A FUNCTION TO COMPUTE GRID AZIMUTHS

## Write a function to compute grid azimuths. You can just implement the code you
## saw in the video, including the testing code.
twopi = 2 * np.pi


def azimuth(p_from: list, p_to: list, converg=0.0) -> float:
    """
    computes the azimuth in range [0,2pi] between points <p_from> to <p_to>
    p_from : [float, float] =[easting, northing] coordinates of starting pint.
        Any additional elenmtas in list are ignored
    p_to : [float, float] =[easting, northing] coordinates of starting pint.
        Any additional elements in list are ignored.
    Converg: float = optional, the grid declination of map projection.
        If not zero, <converg> is added to grid azimuth to convert to a geodetic azimuth.
    return: [0, 2pi] = azimtuh between the points
    """

    if p_from == p_to:
        print("p_from cannot be equal to p_to")
        return None
    az = (np.arctan2(p_to[0] - p_from[0], p_to[1] - p_from[1]) + converg) % twopi
    return az


if __name__ == '__main__':
    help(azimuth)
    print(azimuth([0, 0], [0, 0]))

    angles = np.linspace(0, twopi, 20, endpoint=False)
    print('testing angles')
    for angle in angles:
        e = np.sin(angle)
        n = np.cos(angle)
        az = azimuth([0, 0], [e, n])
        residual = abs(az - angle)
        if residual > 1e-12:
            print(angle, az, residual)

###########################################################
## PART 3: WRITE A FUNCTION TO COMPUTE GRID DISTANCES

## Write a function to compute grid distances. Include a proper documentation
## string, type hints for the arguments and the return type, and testing
## code guarded with the if __name__... statement. The optional third
## argument <two_D> controls whether this is a 2-d or a 3-d distance. Ie, if
## <two_D> is True, compute a 2-d distance; otherwise computer a 3-d distance.
# Your testing code needs to exercise both cases.

def distance(p_from: list, p_to: list, two_D: True) -> float:

    '''
        computes the distance in range between points <p_from> to <p_to>
    p_from : [float, float] =[easting, northing] coordinates of starting pint.
        Any additional elenmtas in list are ignored
    p_to : [float, float, float] =[easting, northing] coordinates of end pint.
        Any additional elements in list are ignored.
    2D: float = optional, the grid declination of map projection.
         If not zero, if 2 D is .
    return: [0, 2pi] = distance between the points
    '''

    if p_from == p_to:
        print("p_from cannot be equal to p_to")
        return None
    if two_D == True:
        distance = (((p_from[0] - p_to[0])**2) + ((p_from[1] - p_to[1])**2))**0.5
        return distance
    #print("2D distance is,", distance)
    if two_D == False:
        distance = (((p_from[0] - p_to[0])**2) + (p_from[1] - p_to[1])**2 + ((p_from[2] - p_to[2])**2))**0.5
        return distance
    #print("3D distance is,", distance)

print('On the testing code...')
print(azimuth([0, 0], [0, 0], 0))
print(distance([0, 0, 0], [0, 0, 0], 0))
print("\nRoot2 is,")
print(distance([1, 0, 0], [0, 1, 0], 0))

if __name__ == '__main__':
    help(distance)
    print(distance([0, 0], [0, 0], [0, 0]))
    lengths = np.linspace(10, 100, 9, endpoint=False)
    print('\n   Testing 2D distance...')
    for two_D in lengths:
        x = random.randrange(int(two_D))
        y = random.randrange(int(two_D))
        dist = distance([0, 0], [x, y], True)
        print(x, y, dist)
    print('\n   Testing 3D distance...')
    for three_d in lengths:
        x = random.randrange(int(three_d))
        y = random.randrange(int(three_d))
        z = random.randrange(int(three_d))
        dist = distance([0, 0, 0], [x, y, z], False)
        print(x, y, z, dist)
print("\nFinished! Alert the Boston Herald!")