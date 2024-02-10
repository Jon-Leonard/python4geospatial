## Your title block goes here

# import your station_B module as station and lib5585 as L
import station_B as station
import lib5585 as L
import numpy as np

## These statements exercise all the methods in station_A. My answers appear
## as comments after the print statement

## Use lib5585 to convert DMS from the data sheet to radians for LX3030 latitude
LX3030_lat_rad = L.from_dmss([41, 48, 44.78429, 1])

## Create an angle in radians for LX3030 latitude
LX3030_lat = station.Latitude(LX3030_lat_rad,sign_strs=('N', 'S'))

## Use lib5585 to convert DMS from the data sheet to radians for LX3030 longitude
LX3030_lon_rad = L.from_dmss([72, 15, 02.04187, -1])

## Create an angle in radians for LX3030 longitude
LX3030_lon = station.Longitude(LX3030_lon_rad,sign_strs=('E', 'W'))

## print longitude, latitude in radians using the __str__ method
print('radians:', LX3030_lon, LX3030_lat)  # radians: -1.26101 0.72976

## print longitude, latitude in DD using the DD method
print('DD:', LX3030_lon.DD(1), LX3030_lat.DD(1))  # DD: -72.3 41.8
print('DD:', LX3030_lon.DD(2), LX3030_lat.DD(2))  # DD: -72.25 41.81
print('DD:', LX3030_lon.DD(3), LX3030_lat.DD(3))  # DD: -72.251 41.812
print('DD:', LX3030_lon.DD(4), LX3030_lat.DD(4))  # DD: -72.2506 41.8124
print('DD:', LX3030_lon.DD(), LX3030_lat.DD())  # DD: -72.25057 41.81244

## print longitude, latitude in DMS using the DMS method
print('DMS:', LX3030_lon.DMS(), LX3030_lat.DMS())  # DMS: 072-15-02.04187 W 041-48-44.78429 N

## print longitude, latitude in DMS using the DMS method
print('DMS list:', LX3030_lon.to_dmss(), LX3030_lat.to_dmss())  # DMS list: [72.0, 15.0, 2.0418700000050194, -1] [41.0, 48.0, 44.784289999993646, 1]

## construct a GeodeticCoordinates object for LX3030
gc_LX3030 = station.GeodeticCoordinates({'lon': LX3030_lon, 'lat': LX3030_lat, 'h': 157.285})

print('gc LX3030:', gc_LX3030)  # gc LX3030:  072-15-02.04187 W, 041-48-44.78429 N, 157.285 NAD83(2011)

## construct a GeodeticCoordinates object for STORRS
gc_STORRS = station.GeodeticCoordinates({
    'lon': station.Longitude(L.from_dmss([72, 15, 32.96838, -1])),
    'lat': station.Latitude(L.from_dmss([41, 48, 53.35690, 1]))})

print('gc STORRS: ', gc_STORRS)  # gc STORRS:  072-15-32.96838 W, 041-48-53.35690 N NAD83(2011)

s, alp1, alp2 = gc_LX3030 - gc_STORRS  # to - from: LX3030 to STORRS
print(f's = {s:0.3f}, alp1 = {alp1.DMS()}, {alp2.DMS()}')  # s = 761.243, alp1 = 110-19-41.10700 (+), 290-20-01.72601 (+)

# fun fact: the forward and reverse azimuths aren't different by 180d!
print(f'difference of forward and reverse azimuths: {np.rad2deg(alp2.angle - alp1.angle):0.7f}')  # 180.0057275

s, alp1, alp2 = gc_STORRS - gc_LX3030  # to - from: to STORRS from LX3030
print(f's = {s:0.3f}, alp1 = {alp1.DMS()}, {alp2.DMS()}')  # s = 761.243, alp1 = 290-20-01.72601 (+), 110-19-41.10700 (+)

## construct a GeodeticCoordinates object for CTMA
gc_CTMA = station.GeodeticCoordinates({
    'lon': station.Longitude(L.from_dmss([72, 12, 38.87706, -1])),
    'lat': station.Latitude(L.from_dmss([41, 43, 52.91739, 1])),
    'h': 55.165})
print('\n gc_CTMA = ', gc_CTMA)
## construct a GeocentricCoordinates object for CTMA
xyz_CTMA = station.GeocentricCoordinates({'X': 1_456_379.709,'Y': -4_539_030.816,'Z': 4_223_420.349})
print('xyz_CTMA:', xyz_CTMA)  # xyz_CTMA: 1,456,379.709, -4,539,030.816, 4,223,420.349 NAD83(2011)

## construct a GeocentricCoordinates object for LX3030
xyz_LX3030 = station.GeocentricCoordinates({'X': 1_451_423.349,'Y': -4_534_399.850,'Z': 4_230_204.304})
print('xyz_LX3030:', xyz_LX3030)  # xyz_LX3030: 1,451,423.349, -4,534,399.850, 4,230,204.304 NAD83(2011)

## construct a SPC83 object for LX3030
spc83_LX3030 = station.GridCoordinates({'e': 346_299.846,'n': 261_260.194}, 'SPCS83')
print('spc83_LX3030:', spc83_LX3030)  # 346,299.846, 261,260.194 SPCS83

## construct a SPC83 object for CTMA
spc83_CTMA = station.GridCoordinates({'e': 349_660.425,'n': 252_275.490}, 'SPCS83')
print('spc83_CTMA:', spc83_CTMA)  # 349,660.425, 252,275.490 SPCS83

d, az1, az2 = gc_CTMA - gc_LX3030
print(f'geodetic distance: {d:0.3f}, az: {az1.DMS()}')  # geodetic distance: 9592.700, az: 159-49-25.00856 (+)
d = xyz_CTMA - xyz_LX3030
print(f'XYZ distance: {d:0.3f}')  # XYZ distance: 9593.404
d, az1 = spc83_CTMA - spc83_LX3030
print(f'SPC83 distance: {d:0.3f}, az: {az1.DMS()}')  # SPC83 distance: 9592.622, az: 159-29-33.09550 (+)

## create Station objects for the three stations.
## in a professional-grade implementation, we'd give the Station constructor only one set of coordinates,
## and it would compute all the rest for us.
LX3030 = station.Station(PID='LX3030', designation='Y88', geodetic=gc_LX3030, XYZ=xyz_LX3030, grid=spc83_LX3030)
print(LX3030)  # Y88 (LX3030) 072-15-02.04187 W, 041-48-44.78429 N, 157.285 NAD83(2011)
CTMA = station.Station(PID='DH5835', designation='CTMA', geodetic=gc_CTMA, XYZ=xyz_CTMA, grid=spc83_CTMA)
STORRS = station.Station(PID='LX4976', designation='STORRS', geodetic=gc_STORRS)

## Here's how we use the Station objects. It's very clean.
d, az1, az2 = CTMA.geodetic - STORRS.geodetic
print(f'geodetic distance: {d:0.3f}, az: {az1.DMS()}')  # geodetic distance: 9592.700, az: 159-49-25.00856 (+)