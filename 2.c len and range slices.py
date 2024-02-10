"""
Jonathan Leonard                            NRE 5585 Python Scripting for Geospatial Analysis
Module 2c Length and Range Slices           2SEP2021
"""

## IN THIS EXERCISE YOU WILL USE len(), range() AND SLICES TO
##          IMPORT A DIGITAL ELEVATION MODEL (DEM) AS A NUMPY ARRAY
##          DETERMINE ITS SHAPE (NUMBER OF ROWS AND COLUMNS)
##          FLATTEN THE NUMPY ARRAY
##          CAST THE NUMPY ARRAY INTO A PYTHON LIST
##          COMPUTE THE MEAN HEIGHT IN THE DEM
##          COMPUTE THE MEAN HEIGHT OF EACH ROW IN THE DEM

# import arcpy, set up variables for your drive letter and data path. Set the workspace to the data directory...
import arcpy
dl = 'C:/'
data_path = dl + 'NRE_5585/Data/'
temp_path = dl + 'NRE_5585/Temp/'
res_path  = dl + 'NRE_5585/Results/'
arcpy.env.workspace = data_path
arcpy.env.overwriteOutput = True

#  Open arcpro and look at dem.img. It's always a good idea to visualize your data
#  Use arcpy.RasterToNumPyArray('dem.img') to import the dem into a variable named np_dem...
np_dem = arcpy.RasterToNumPyArray('dem.img')

##  the dem is organized as a two-dimensional array. The rows hold heights that
##  run east-west, and row zero is at the north. So the rows are ordered north to south, and the columns
##  are ordered west to east. Not all dems are organized like this so you need to take care in this regard.
##  How can you determine how a dem is organized by using arcpro?
#  create and print a variable to store len(np_dem), which is the number of rows in the dem...
n_rows = len(np_dem)
print(f' Number of rows = {n_rows}')

#  create and print a variable to store len(np_dem[0]), which is the number of columns per row. (NB this is assuming
#  that every row has the same number of columns...
n_cols = len(np_dem[0])
print(f' Number of columns = {n_cols}')

## Our goal is compute the mean height of the dem. The two-dimensional structure of np_dem complicates this.
## numpy arrays have a method named flatten() that will reshape the array into a one-dimensional list.
# Invoke the flatten() and cast the numpy array into a python list...
dem = list(np_dem.flatten())

#  Print the number of elements in dem. You'll see it's 1,000,000, which verifies that all rows have the
#  same number of columns...
num_of_elem = len(dem)
print(f' Number of rows of flattened dem = {num_of_elem}')

#  Write a for-loop to compute the mean height of the dem. Print the height to 3 digits. (170.121 m)...
total = 0
for i in dem:
    total = total + i
    avgElev = total/len(dem)
print('The average height is {:0.3f} m'.format(avgElev))

## COMPUTE AND PRINT THE MEAN HEIGHT FOR EACH ROW
#  Create a variable named row and initialize it to 0. We'll use this to keep track of which row we're
#  working on in the for-loop we'll write next
row = 0

## HAVING FLATTENED DEM, WE'LL NEED TO PROCESS IT IN SLICES ONE ROW LONG. THE FIRST SLICE IS
## 0..999, THE SECOND IS 1000..1999, ETC. WE'LL USE THE range() FUNCTION TO GENERATE THE PROPER
## STARTING INDEX VALUES, NAMELY, 0, 1000, 2000, 3000, ..., 999000
#  Write a for-statement with index variable r_ndx that iterates over the range starting at zero,
#  ending at len(dem), in steps equal to the number of columns per row...
for r_ndx in range(0, len(dem), n_cols):

    ## COMPUTE THE MEAN FOR DEM ELEMENTS r_ndx through r_ndx+n_cols
    # set total to zero...
    total = 0

    # write a for-statement with index variable h that iterates over dem using a slice starting at
    # r_ndx : r_ndx + n_cols, and add h to total...
    for h in dem[r_ndx: r_ndx + n_cols]:
        total = total + h

    # compute this row's average as total divided by n_cols...
        avg = total / n_cols

    # increment row...
        row = row + 1

    # print row and this row's mean height (1 has 181.300, 2 has 181.316, ..., 1000 has 149.605)...
print(f'{row} has {h}')

print("It's finished. Alert the pre .....Wait a minute...Why are my values not the same as the professor's ??!!")