"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 9 Station B                                         27OCT2021
"""

from copy import copy
from numpy import sqrt, sin, arcsin, cos, tan, arctan, arctan2, pi, rad2deg
## import your lib5585 as L
import lib5585 as L

## Copy the code from station_A here
## define a class Angle
class Angle:
    ## define its constructor with arguments self, angle_radians: float, sign_strs=('(+)', '(-)')
    def __init__(self, angle_radians: float, sign_strs=('(+)', '(-)')):
        ## assign angle_radians to an attribute
        self.angle = angle_radians  # this saves angle_radians in an attribute local to this object
        ## assign sign_strs to an attribute
        self.sign_strs = sign_strs

    ## define a method __str__(self)
    def __str__(self) -> str:
        ## return a string of self.angle formatted to five digits after the decimal
        return f'{self.angle:0.5f}'

    ## define a method DD(self, ndigits=5)
    def DD(self, ndigits=5) -> str:
        ## return a string of self.angle converted to degrees and formatted to <ndigits> digits after the decimal.
        ## I converted the angle to DD and then used round() to set the number of digits. Make sure you don't
        ## change the value of self.angle, though!
        input = self.angle
        temp = input * 180/pi
        output = round(temp, ndigits)
        return f'{output}'
     #   self.DD = round(self.angle * 180/np.pi, ndigits)
     #   return self.DD

    ## define a method to_dmss(self)
    def to_dmss(self) -> list:
        # return this angle as [degree:int, minute:int, second:float, sign:[1|-1]]
        # call the function in lib5585 to do this, rather than re-implement it. Always think "code reuse"
        dmss = L.to_dmss(self.angle)
        return dmss

    ## define a method DMS(self) that returns a string
    def DMS(self) -> str:
        # Return a string giving this object's angle formatted as 'ddd-mm-ss.sssss S' where
        # ddd is degrees padded with leading zeros so it always has three digits
        # mm is minutes padded with leading zeros so it always has two digits
        # ss.sssss is seconds padded with leading zeros so it always has two digits before the decimal and five after
        # S is self.sign_strs[0] if self.angle >= 0 or self.sign_strs[1] if self.angle < 0
        ddd = int(L.to_dmss(self.angle)[0])
        mm = int(L.to_dmss(self.angle)[1])
        ss = float(L.to_dmss(self.angle)[2])

        if self.angle >= 0:
            S = self.sign_strs[0]
        else:
            S = self.sign_strs[1]
        return f'{ddd:03}-{mm:02}-{ss:08.05f} {S}'

#######################        Station A code end         ###########################

## define a class named Latitude that inherits from Angle
class Latitude(Angle):

    ## define the constructor with arguments self, angle_radians: float, sign_strs = ('N', 'S')
    ## providing this default value for sign_strs means the user has a good default, but can
    ## change them if so desired
    def __init__(self, angle_radians: float, sign_strs = ('N', 'S')):
        if isinstance(angle_radians, Angle):
            assert -pi/2 <= angle_radians <= pi/2, f'-pi/2 <= {angle_radians} <= pi/2 not met'
            Angle.__init__(self, angle_radians.angle, sign_strs)

        else:
            assert -pi/2 <= angle_radians <= pi/2, f'-pi/2 <= {angle_radians} <= pi/2 not met'
            ## call Angle.__init(...
            Angle.__init__(self, angle_radians, sign_strs)

## define a class named Longitude that inherits from Angle
class Longitude(Angle):
    ## define the constructor with ('E', 'W') as the default sign_strs value
    def __init__(self, angle_radians: float, sign_strs=('E', 'W')):
        if isinstance(angle_radians, Angle):
            assert -pi <= angle_radians <= pi, f'-pi <= {angle_radians} <= pi not met'
            Angle.__init__(self, angle_radians.angle, sign_strs)

        else:
        ## provide the appropriate assertion, recalling that longitude has a different valid range than latitude
            assert -pi <= angle_radians <= pi, f'-pi <= {angle_radians} <= pi not met'
            ## call Angle.__init(...
            Angle.__init__(self, angle_radians, sign_strs)

## define a base class named Coordinates
class Coordinates:
    ## define the constructor that takes a dictionary called coords and a str named nm as arguments.
    def __init__(self, coords: dict, nm: str):
        ## create an attribute named coords that is a copy of the argument coords
        self.coords = copy(coords)
        self.nm = nm

    # define a method named __sub__(self, other)
    def __sub__(self, other):
        pass  # every method must have something in its body

## define a class GeodeticCoordinates that inherits from Coordinates
class GeodeticCoordinates(Coordinates):

    ## define the constructor that takes a dictionary called coords and nm='NAD83(2011)' as its arguments
    def __init__(self, coords: dict, nm='NAD83(2011)'):
        ## assert that the key 'lat' is in coords
        assert 'lat' in coords
        assert isinstance(coords['lat'], Latitude)
        ## assert that the key 'lon' is in coords and assert it is an object of type Longitude
        assert 'lon' in coords
        assert isinstance(coords['lon'], Longitude)
        ## call Coordinate's constructor with coords and nm
        Coordinates.__init__(self, coords, nm)
        ## create an attribute named lon that holds the longitude
        self.lon = coords['lon']
        ## create an attribute named lat that holds the latitude
        self.lat = coords['lat']
        ## these are some constants we need below. They define the NAD83(2011) reference ellipsoid: GRS 80
        self.a = a = 6_378_137  # GRS 80
        f = 1.0/298.257222101
        b = a - a * f
        self.e = a**2 / b**2 - 1
        self.e_sq = 2 * f - f*f

    ## define a method overloading __str__
    def __str__(self):
        ## if 'h' is one of self.coords keys, then there's a geodetic height
        if 'h' in self.coords:
            ## return a string with longtitude, latitude, height, and nm in DMS, DMS, 0.3f, str format
            return f'{self.lon.DMS()}, {self.lat.DMS()}, {self.coords["h"]:0.3f} {self.nm}'
        ## else (there is no height given)
        else:
            ## return a string with longtitude, latitude, and nm in DMS, DMS, str format
            return f'{self.lon.DMS()}, {self.lat.DMS()}, {self.nm}'

    ## define a method __sub__(self, other)
    def __sub__(self, other):
        ## assert other is of type GeodeticCoordinates
        assert isinstance(other, GeodeticCoordinates)
        ## this code implements Bowring 1981's indirect method. It computes geodetic distance an azimuths
        ## from self to other
        L1, B1 = other.lon.angle, other.lat.angle
        L2, B2 = self.lon.angle, self.lat.angle
        A = sqrt(1 + self.e * cos(B1) ** 4)
        B = sqrt(1 + self.e * cos(B1) ** 2)
        C = sqrt(1 + self.e)
        w = A * (L2 - L1) / 2
        del_lat = B2 - B1
        D = del_lat/(2*B) * (1 + 3*self.e/(4*B**2) * del_lat * sin(2*B1 + (2/3)*del_lat))
        E = sin(D)*cos(w)
        F = sin(w)*(B*cos(B1)*cos(D) - sin(B1)*sin(D)) / A
        G = arctan2(F, E)
        sig = 2.0 * arcsin(sqrt(E*E + F*F))
        H = arctan( (sin(B1) + B * cos(B1) * tan(D)) * tan(w) / A)
        alp1 = (G - H) % (2*pi)
        alp2 = (G + H + pi) % (2*pi)
        s = self.a * C * sig / B**2
        return s, Angle(alp1), Angle(alp2)  # notice returning azimuths as Angle objects

## define a class GeocentricCoordinates that inherits from Coordinates
class GeocentricCoordinates(Coordinates):
    ## define the constructor that takes a dictionary called coords and nm='NAD83(2011)' as its arguments
    def __init__(self, coords: dict, nm='NAD83(20011)'):

        ## assert that X, Y, and Z are keys in the dictionary
        assert 'X' in coords
        assert 'Y' in coords
        assert 'Z' in coords

        ## call the parent class's constructor
        Coordinates.__init__(self, coords, nm)

        ## create attributes named X, Y, and Z to hold the three coordinates
        self.X = coords['X']
        self.Y = coords['Y']
        self.Z = coords['Z']

    ## overload __str__ to print the three coordinates to 3 sig. digits using comma separators, and then nm
    def __str__(self):
        return f'{self.X:,.3f}, {self.Y:,.3f}, {self.Z:,.3f} {self.nm}'

    ## define a method __sub__(self, other)
    def __sub__(self, other):
        ## assert other is an instance of GeocentricCoordinates
        assert isinstance(other, GeocentricCoordinates)

        ## substract self - other for the three coordinates
        dX = self.X - other.X
        dY = self.Y - other.Y
        dZ = self.Z - other.Z

        ## compute and return the distance
        dist = (dX**2 + dY**2 + dZ**2)**0.5
        return dist

## define a class GridCoordinates that inherits from Coordinates
class GridCoordinates(Coordinates):
    ## define the constructor that takes a dictionary called coords and a string named nm as its arguments
    def __init__(self, coords: dict, nm: str):

        ## assert 'e' and 'n' are keys in coords
        assert 'e' in coords
        assert 'n' in coords

        ## call the parent's constructor
        Coordinates.__init__(self, coords, nm)
        ## store coords['e'] and coords['n'] in attributes named 'e' and 'n', respectively
        self.e, self.n = coords['e'], coords['n']

    ## overload __str__ to print the two coordinates to 3 sig. digits using comma separators, and then nm
    def __str__(self):
        return f'{self.e:,.3f}, {self.n:,.3f}, {self.nm}'

    ## define a method __sub__(self, other)
    def __sub__(self, other):

        ## assert other is an instance of GridCoordinates
        assert isinstance(other, GridCoordinates)

        ## compute and return grid distance and grid azimuth
        de = self.e - other.e
        dn = self.n - other.n
        dist = (de**2 + dn**2)**0.5
        from_az = [self.e, self.n]
        to_az = [other.e, other.n]
        az = L.azimuth(from_az, to_az)
        return dist, Angle(az)

## define a base class named Station
class Station:
    def __init__(self, PID=None, designation='station', geodetic=None, XYZ=None, grid=None, heights=None):
        self.PID = PID
        self.designation = designation
        self.geodetic = copy(geodetic)
        self.XYZ = copy(XYZ)
        self.grid = copy(grid)
        self.heights = copy(heights)

    def __repr__(self):
        """
        called as: repr(object)
        returns a more complete set of information than __str__
        """
        if self.PID:
            return f'{self.designation} ({self.PID}) {self.geodetic}'
        else:
            return f'{self.designation} {self.geodetic}'

    def __str__(self):
        if self.PID:
            return f'{self.designation} ({self.PID}) {self.geodetic}'
        else:
            return f'{self.designation} {self.geodetic}'