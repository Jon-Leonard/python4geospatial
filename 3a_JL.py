"""
Jonathan Leonard                        NRE 5585 Python Scripting for Geospatial Analysis
Module 3 a                              16SEP2021
"""
## WORKING WITH FILES

## IN THIS EXERCISE, YOU WILL PERFORM THE FOLLOWING...
##      OPEN A FILE IN WRITE MODE
##      WRITE TO A FILE
##      CLOSE A FILE
##      OPEN A FILE IN READ MODE
##      READ FROM A FILE
## Set up...
print('Initializing...')
import arcpy
import numpy as np

dl = "C:/"
data_path = "NRE_5585/data/"
temp_path = "NRE_5585/temp/"
res_path = "NRE_5585/results/"
arcpy.env.workspace = res_path
arcpy.env.overwriteOutput = True
print('Ready to go!')

##-------------------------------------------------------------
## PART 1: WRITING TO A FILE

# define variable for a new file (use "C:\NRE_5585\Results" as the location)...
fn = 'new_file.txt'

# open file, from previous statement, in write mode...
fh = open(dl + res_path + fn, mode='w')

# define a variable for the line that will be written to the file...
line = "100 250 500\n"      ##  WHY IS THE \n NEEDED?

# write line, from previous statement, to the file...

fh.write(line)

# define a variable for the next line that will be written to the file...
line = "1000 1250 1500\n"         ## NOTE: VARIABLES CAN BE REUSED BY ASSIGNING THEM TO NEW VALUES

# write line to the file...
fh.write(line)

# close the file...
fh.close()

## OPEN THE FILE IN NOTEPAD AND CONFIRM THAT IT CONTAINS THE APPROPRIATE DATA. THEN CLOSE NOTEPAD.
print("Lines written to new_file. Part 1 finished \n")

##-------------------------------------------------------------
## PART 2: READ FROM A FILE

##-----------
## OPEN FILE AND READ LINE...

# open the file from PART 1 in read mode...
fh = open(dl + res_path + fn, mode='r')

# read first line from the file and assign to variable...
line = fh.readline()

#print line...
print('First line in the file =', line)

## WHAT SEPARATES THE VALUES IN THE LINE?
##Commas seperate the values in the line

##-----------
## SEPARATE THE VALUES IN THE LINE AND STORE IN A LIST...

# split the line, by the appropriate character, to separate the values into a list...

line = line[:-1]
line = line.split(',')

# print line...
print('First line split =', line)

fh.close()
## WHAT IS THE DATA TYPE FOR THE VALUES IN THE LIST?
## Looks like a string
##-----------
## CONVERT VALUES TO NUMBERS...

fh = open(dl + res_path + fn, mode='r')

# read first line from the file and assign to variable...
line = fh.readline()


# assign variable to first value in the list...
for line in fh:
    first_val = line[:3]
    # convert the value, from line above, to an integer... (not in lecture, learn by example)
    int_val = int(first_val)      ## int( ) IS A COMMAND THAT CONVERTS STRINGS TO INTEGERS
    print("First value as an integer =", int_val)

    # convert the value, from line above, to a decimal number... (not in lecture, learn by example)
    float_val = float(first_val)      ## float( ) IS A COMMAND THAT CONVERTS STRINGS OR INTEGERS TO DECIMAL NUMBERS
    print('First value as a float =', float_val)

##-----------
## GET NEXT LINE FROM FILE...

# read second line from the file and assign to variable...
fh = open(dl + res_path + fn, mode='r')
line2 = fh.readline()

for line2 in fh:
    sec_line = line2[0:]
    # print line
    print("Second line from the file =", sec_line)

##-----------
## GET NEXT LINE FROM FILE...

# read the next line from the file and assign to variable...
fh = open(dl + res_path + fn, mode='r')
third_line = fh.readline()

for line3 in fh:
    third_line = line3[2]
    print('Third line =', third_line)

print("Got all three lines I think. Part 2 finished")

## IN THE PYTHON SHELL, TYPE IN LINE AND HIT ENTER. NOTICE THAT THE LINE IS NOW JUST AN EMPTY STRING - THIS INDICATES YOU HAVE REACHED THE END OF THE FILE.

# close the file...
fh.close()
## A LOOP IS VERY USEFUL WHEN YOU NEED TO READ THROUGH FILES SINCE IT IS A REPETITIVE PROCESS.

print("All done. Alert 'The Day'!!")