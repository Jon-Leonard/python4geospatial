"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 11 b     Pandas: Data frames & series               28NOV2021
"""

## Setup up your drive letter and path variables. (We won't be using arcpy in this exercise.)
## Import pandas as pd and matplotlib.pyplot as plt
print('Initializing...')
import pandas as pd
import matplotlib.pyplot as plt
dl = 'C:/'
data_path = 'NRE_5585/data/'
temp_path = 'NRE_5585/temp/'
res_path = 'NRE_5585/results/'
#arcpy.env.workspace = dl + data_path
#arcpy.env.overwriteOutput = True
print('Ready to go!\n')

## Create variables to hold the path+filename for uconn_woody_plants.xlsx. It seems that the Excel file
## has better data in it, so we'll use it.
trez_xl = dl + data_path + 'uconn_woody_plants.xlsx'

# create a pandas ExcelFile handle xlsx
with pd.ExcelFile(trez_xl) as xlsx:

    ## use pd.read_excel(xlsx, 'woody_plants', index_col='TAG_NO') to create a DataFrame.
    pd.read_excel(xlsx, 'woody_plants', index_col='TAG_NO')

    ## Using TAG_NO as the index column allows us to select plants by their TAG_NO using df.loc[tag_no],
    ## which is similar to how things work with relational databases: selection by primary-key value.
    df = pd.read_excel(xlsx, 'woody_plants', index_col='TAG_NO')
print(df)

## Print the names of the genera (no duplicates) sorted ascending
## (the plural of 'genus' is 'genera')
print('\nGenus names are...\n', (sorted(df.Genus.unique())))

## Print the number of memorial apple trees (maple is genus Acer) (8)
print('Number of apple trees =', len(df.Genus == 'Acer'))

## Print the index values (df.index)
print('The index values =', df.index)

## Print the record associated with tag number 6000
print('Records associated with Tag No. 6000 =', df.loc[6000])

## Print the last record of the data frame
print('The last record =', df.tail(1))

## Use matplotlib.pyplot to plot in a single plot all the non-memorial trees (df.Memorial == False) as black dots and all
## the memorial trees (df.Memorial == True) as red dots.

non_mem = df[df.Memorial == False]
plt.plot(non_mem.E, non_mem.N, 'k.')
mem = df[df.Memorial == 1]
plt.plot(mem.E, mem.N, 'r.')
plt.title("Forest Coverage Selection", loc="center", size=12, color="black")
plt.legend(['Non-Memorial Trees', 'Memorial Trees'], edgecolor='black')
plt.show()
print("Finished!  Alert the Porcupine's Gazette!!")