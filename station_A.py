"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 9 Station A                                         27OCT2021
"""

# import lib5585 as L and numpy as np
import lib5585 as L
import numpy as np


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
        temp = input * 180/np.pi
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