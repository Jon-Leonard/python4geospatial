"""
Jonathan Leonard                                         NRE 5585 Python Scripting for Geospatial Analysis
Week 11 IA     Pandas: Data frames & series              28NOV2021
"""

## Setup up your drive letter and path variables. (We won't be using arcpy in this exercise.)
## Import pandas as pd and matplotlib.pyplot as plt
print('Initializing...')
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.colors as c
import numpy as np
from tabulate import tabulate
dl = 'C:/'
data_path = 'NRE_5585/data/'
temp_path = 'NRE_5585/temp/'
res_path = 'NRE_5585/results/'
print('Ready to go!\n')

## Set up

trez_csv = dl + data_path + 'uconn_woody_plants.csv'
df = pd.read_csv(trez_csv)
print(df)
'''
trez_xl = dl + data_path + 'uconn_woody_plants.xlsx'
with pd.ExcelFile(trez_xl) as xlsx:
    df = pd.read_excel(xlsx, 'woody_plants', index_col='TAG_NO')
print(df)
'''
'''
The correlation coefficient r is zero when the data are uncorrelated, meaning there is no pattern at all
linking the independent variable and the dependent variable. If there is a perfect linear relationship,
meaning knowing a value of the independent variable allows us to know exactly the corresponding value of
the dependent variable, then r = 1. If r = -1, then there is, again, perfect knowledge between the 
independent and dependent variables; however, they have an inverse relationship: when one increases the
other decreases. The correlation coefficient r is calculated like this:
'''
''' 
We need the following quantities
 (∑ 𝑥) is summing the Tree_Height column, name this variable sum_x.
 (∑ 𝑥^2) is summing Tree_Height**2, name this variable sum_x_sq
'''
sum_x = sum(df.Tree_Height)
sum_x_sq = sum(df.Tree_Height**2)
#print('Tree Height sum =', sum_x)
#print('Tree Height^2 =', sum_x_sq)

'''
• (∑ 𝑦) is summing the Crown_Radius column, name this variable sum_y
• (∑ 𝑦^2) is summing Crown_Radius**2, name this variable sum_y_sq
• (∑ 𝑥 𝑦) is summing Tree_Height * Crown_Radius, name this variable sum_x_y, and
• n is the output of the len() operator on the data frame. Name this variable n.
'''

'''
There are three more variables: one for m, b, and r. We’ll need
• (∑ 𝑥)^2    is sum_x**2
• (∑ 𝑦)^2    is sum_y**2
'''
sum_y = sum(df.Crown_Radius)
sum_y_sq = sum(df.Crown_Radius ** 2)
sum_x_y = sum(df.Tree_Height * df.Crown_Radius)   # sum_x_y = sum(sum_x * sum_y) was incorrect!
n = len(df)
sum_x2 = sum_x ** 2
sum_y2 = sum_y ** 2

'''
Create the plot shown using matplotlib.pyplot by calculating m, b, and r as shown. The
regression indicates that crown radius increases by m = 0.26 m per meter-of-height on average. The
regression line is plotted from the point (0, b) to (max tree height, b + m * max tree height).
Extra credit (2 points) Plot each genus in a different color and/or symbol.
Then, using the df.groupby(‘Genus’) method, compute m, b, r for each genus that has at least 20 trees and
print the result in a table, partially shown below.
'''
'''
𝑏 =  (∑ 𝑦)(∑ 𝑥^2) −(∑ 𝑥)(∑ 𝑥 𝑦) / 𝑛(∑ 𝑥^2)− (∑ 𝑥)^2
'''
b = (sum_y * sum_x_sq - sum_x * sum_x_y) / ((n * sum_x_sq) - sum_x2)
'''
𝑚 = 𝑛(∑ 𝑥 𝑦) −(∑ 𝑥)(∑ 𝑦) / 𝑛(∑ 𝑥^2)− (∑ 𝑥)^2
'''
m = (n * sum_x_y - sum_x * sum_y) / (n * sum_x_sq - sum_x2)
'''
𝑟 = 𝑛(∑ 𝑥 𝑦)−(∑ 𝑥)(∑ 𝑦) / √(𝑛(∑ 𝑥^2)− (∑ 𝑥)^2)(𝑛(∑ 𝑦^2)− (∑ 𝑦)^2)
'''
r = (n * sum_x_y - sum_x * sum_y) / np.sqrt((n * sum_x_sq - sum_x2) * (n * sum_y_sq - sum_y2))

plt.title("Crown Width (m) given Tree Height (m)", loc="center", size=12, color="black")
plt.legend(['m', 'b', 'r'], edgecolor='black')
plt.xlabel("Tree Height (m)", size=10)
plt.ylabel("Crown Radius (m)", size=10)
plt.text(-0.5, 15, f"m = {m:.2f}, b={b:.2f}, r = {r:0.2f}", fontsize=10, verticalalignment="top")

color_or = 0
colors = ['b', 'g', 'k', 'c', 'm', 'y']  ##Really want to figure out how to import more colors for next time'

all_colors = len(colors)
for TAG_NO, genus in df.groupby('Genus'):
    plt.plot(genus['Tree_Height'], genus['Crown_Radius'], colors[color_or]+".", marker="+", markersize=1)
    color_or = (color_or + 1) % all_colors  # include all colors
plt.plot([0, max(df.Tree_Height)], [b, m*max(df.Tree_Height)], color='red', linewidth=2.0)
plt.show()

dataset = []
for TAG_NO, genus in df.groupby('Genus'):
    if len(genus) > 20:
        sum_x = sum(genus.Tree_Height)
        sum_x_sq = sum(genus.Tree_Height ** 2)
        sum_y = sum(genus.Crown_Radius)
        sum_y_sq = sum(genus.Crown_Radius ** 2)
        sum_x_y = sum(genus.Tree_Height * genus.Crown_Radius)   # again, sum_x_y = sum(sum_x * sum_y) was incorrect!
        sum_x2 = sum_x ** 2
        sum_y2 = sum_y ** 2
        n = len(genus)

        b = (sum_y * sum_x_sq - sum_x * sum_x_y) / (n * sum_x_sq - sum_x2)
        m = (n * sum_x_y - sum_x * sum_y) / (n * sum_x_sq - sum_x2)
        r = (n * sum_x_y - sum_x * sum_y) / (((n * sum_x_sq - sum_x2) * (n * sum_y_sq - sum_y2)) ** 0.5)
        dataset.append([TAG_NO, m, b, r])

table = pd.DataFrame(np.array(dataset), columns=['Genus', 'Slope', 'Intercept', 'r'])
print(tabulate(table, headers='keys'))
print('\nFinished! Alert Facebook News!')