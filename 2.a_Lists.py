## WORKING WITH LISTS

## IN THIS EXERCISE, YOU WILL PERFORM THE FOLLOWING...
##      CREATE A LIST
##      RETRIEVE ELEMENTS FROM A LIST
##      ADD ELEMENTS TO A LIST
##      SORT A LIST
##      DELETE ELEMENTS FROM A LIST
##
## BE MINDFUL WHEN YOU'RE WORKING WITH THE LAST ELEMENT
## AND USE THE -1 INDEXING CONVENTION TO ACCESS ELEMENTS
## AT THE END. (-2 FOR THE PENULTIMATE, ELEMENT, ETC.)

##-------------------------------------------
## CREATE A LIST...

# create a list that contains the following numbers: 300,900,150,600,1000,250...
list1 = [300, 900, 150, 600, 1000, 250]
list1
##-------------------
## RETRIEVE ELEMENTS FROM A LIST...

# print the first element from the list... 
frst = list1[0]
print(frst)
# print the last element from the list using the -1 index value...
last = list1[:-1]
print(last)
# print the 3rd element from the list... 
thrd = list1[2]
print(thrd)

# use a slice to print the first 3 elements from the list...
slice = list1[0:3]

# print list... 
print(slice)

##-------------------
## ADD ELEMENTS TO A LIST...

# add the number 100 to the end of the list... 

list1.append(100)

# insert the number 450 at the beginning of the list...

list1.insert(0, 450)

# insert the number 100 at position 2 in the list, which means make it the third element...
list1.insert(2, 100)

# insert a value of 50 at position 4 in the list, which means make it the fifth element...
list1.insert(4, 50)

# print list... 
print(list1)

##-------------------
## SORT A LIST...

# sort the list in ascending order. use the built-in function sorted(list)
x = sorted(list1)

# print list... 
print(x)

##-------------------
## DELETE ELEMENTS FROM A LIST...

# delete the last element from the list... 
del list1[-1]

# print list... 
print(list1)

##-------------------
## NESTED LISTS...

# create a nested list...
XY_list = [[500,1000],[750,1500]]

# print the first sublist in XY_list... 
print(XY_list[0])

# print the first element in the first sublist... 
print(XY_list[0][0])

# print the first element in the second sublist... 
print(XY_list[1][0])

# delete the second element in the second sublist... 
del (XY_list[1][1])

# add the number 2000 to the end of the second sublist... 
XY_list.append(2000)

# print list... 

print(XY_list)