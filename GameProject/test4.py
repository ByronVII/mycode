#!/usr/bin/env python3

import csv
import random
import os
from os import system, name

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#              0   1   2   3   4   5   6   7   8   9  10   1   2   3   4   5   6   7   8   9  20   1   2   3   4   5   6   7   8   9  30   1   2   3   4   5   6   7   8   9  40   1   2   3   4   5   6   7   8
MapGrid=[['########################################################################################################################################################################################################'],
         ['########################################################################################################################################################################################################'],
         ['##                                                                                                                                                                                                    ##'],
         ['##                                                                                                                                                                                                    ##'],
         ['##                                                                                                                                                                                                    ##'],
         ['##                                                                                                                                                                                                    ##'],
         ['##                                                                                                                                                                                                    ##'],
         ['##                                                                                                                                                                                                    ##'],
         ['##                                                                                                                                                                                                    ##'],
         ['##                                                                              #   #   #################                                                                                             ##'],
         ['##                                                              #   #           #   #                   #                                                                                             ##'],
         ['##                                                              #   #           #   #####   #####   #   #                                                                                             ##'],
         ['##                                                              #   #           #       #       #   #   #                                                                                             ##'],
         ['##                                                              #   #############       #####   #   #   #                                                                                             ##'],
         ['##                                                              #               #           #   #   #   #                                                                                             ##'],
         ['##                                                              #   #####   #   #########   #   #   #   #                                                                                             ##'],
         ['##                                                              #       #   #               #   #   #                                                                                                 ##'],
         ['##                                                              #   #   #   #####################   #####                                                                                             ##'],
         ['##                                                              #   #   #           #                   #                                                                                             ##'],
         ['##                                                              #####   #   #####   #   #############   #                                                                                             ##'],
         ['##                                                              #       #   #       #   #               #                                                                                             ##'],
         ['##                                                              #       #   #   #####   #########    ####                                                                                             ##'],
         ['##                                                              #       #   #           #               #                                                                                             ##'],
         ['##                                                              #   #####   #########   #   #############                                                                                             ##'],
         ['##                                                                                  # X #                                                                                                             ##'],
         ['#####################################################################################/ \################################################################################################################'],
         ['########################################################################################################################################################################################################']]
#              0   1   2   3   4   5   6   7   8   9  10   1   2   3   4   5   6   7   8   9  20   1   2   3   4   5   6   7   8   9  30   1   2   3   4   5   6   7   8   9  40   1   2   3   4   5   6   7   8

def split(word):
    return [char for char in word]

print(len(MapGrid))
maplist= []
for y in range(len(MapGrid)):
    templist= []
    maptemp= split(MapGrid[y][0])
    for x in range(len(maptemp)):
        templist.append([0,maptemp[x][0]])
    maplist.append(templist)
for y in range(len(maplist)):
    for x in range(len(maplist[y])):
        if maplist[y][x][1] == "X":
            MapLoc = [y,x]
            maplist[y][x][1] = " "

maxy=len(maplist)
maxx=len(maplist[0])

while True:
    clear()

    for y in range(MapLoc[0]-1,MapLoc[0]+2):            #reveals nearby map sections
        for x in range(MapLoc[1]-2,MapLoc[1]+3):
            maplist[y][x][0] = 1

            
#    if MapLoc[0]-8 < 0:
#        print(2)
#        if MapLoc[1]-30 <0:
#            print(3)
#            for y in range(0,16):
#                print(4)
#                for x in range(0,16):
#                    print(5)
#                    if MapLoc[0] == y and MapLoc[1] == x:
#                        print("o",end="")
#                    else:
#                        if maplist[y][x][0] == 1:
#                            print(maplist[y][x][1],end="")
#                        else:
#                            print(" ", end="")
#    else:
    print(1)
    print(os.get_terminal_size())
    for y in range(len(maplist)):
        for x in range(len(maplist[y])):
            if MapLoc[0] == y and MapLoc[1] == x:
                print("o",end="")
            else:
                if maplist[y][x][0] == 1:
                    print(maplist[y][x][1],end="")
                else:
                    print(" ", end="")

        print()

    while True:
        action = input("Where would you like to go? \n>")
        if action in ["w"]:
            if maplist[MapLoc[0]-1][MapLoc[1]][1] == "#":
                print("Can't move north.")
                continue
            else:
                MapLoc[0] -= 2
                break
        elif action == "s":
            if maplist[MapLoc[0]+1][MapLoc[1]][1] == "#":
                print("Can't move south.")
                continue
            else:
                MapLoc[0] += 2
                break
        elif action in ["d"]:
            if maplist[MapLoc[0]][MapLoc[1]+2][1] == "#":
                print("Can't move east.")
                continue
            else:
                MapLoc[1] += 4
                break
        elif action in ["a"]:
            if maplist[MapLoc[0]][MapLoc[1]-2][1] == "#":
                print("Can't move west.")
                continue
            else:
                MapLoc[1] -= 4
                break
        else:
            continue


