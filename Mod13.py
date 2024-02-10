import pandas as pd
import time
import fibonacci_lattice as fl
import arcpy
from numpy import radians, pi
start = time.time()
data_path = 'C:/NRE_5585/data/'
res_path = 'C:/NRE_5585/results/'
arcpy.env.workspace = res_path
arcpy.env.overwriteOutput = 1

lonmin, lonmax, latmin, latmax, n = radians(-73.0 - 44.0 / 60.), radians(-71.0 - 47.0 / 60.), radians(40.0 + 58.0 / 60.),\
                              radians(42.0 + 3.0 / 60.), 20_000_000
lon, lat = fl.fibLatticeFiltered(n, lonmin, lonmax, latmin, latmax)
lon, lat, WKID, out = lon*180/pi, lat*180/pi, 6318, 'CT_lattice.shp'

arcpy.CreateFeatureclass_management(res_path, out, 'POINT', spatial_reference=WKID)
lattice = "".join([res_path, out])

with arcpy.da.InsertCursor('CT_lattice.shp', 'SHAPE@XY') as ic:
    for xy in zip(lon, lat):
        ic.insertRow([xy])

out, WKID, EN = 'CT_latticeSPC.shp', 6434, []
latticeSPC = arcpy.management.Project(lattice, out, WKID)
with arcpy.da.SearchCursor(out, 'SHAPE@XY') as sc:
    for row in sc:
        e, n = row[0]
        EN.append([e, n])
apawell = "".join([data_path, 'APAWELL.shp'])
csv = []
with arcpy.da.SearchCursor(apawell, ['SHAPE@XY', 'FID']) as sc:
    for row in sc:
        FID = row[1]
        e, n = row[0]
        close = 10.0**10
        closest = []
        for coord in EN:
            dist = ((e - coord[0]) ** 2 + (n - coord[1]) ** 2)**0.5
            if dist < close:
                close = dist
                closest = [coord[0], coord[1]]
        csv.append([FID, closest[0], closest[1]])
df_forCSV = pd.DataFrame(csv)
hdr = ['FID', 'E', 'N']
df_forCSV.to_csv(res_path + 'closest_mod13.csv', header=hdr)
end = time.time()
t = end - start
print(t, 's')