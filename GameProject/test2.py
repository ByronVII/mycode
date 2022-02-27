#!/usr/bin/env python3


# Python3 program to Split string into characters
def split(word):
    return [char for char in word]
     
# Driver code
word = 'geeks'
print(split(word))

MapGrid= [' ###   #X# #']
print(list(MapGrid))
temp1= MapGrid[0]
temp2= split(temp1)
print(temp1)
print(temp2)
maptemp= MapGrid[0].split()
print(len(maptemp))
for x in range(len(maptemp[0])):
    print(x)
    print(maptemp[x])
