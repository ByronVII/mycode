#!/usr/bin/env python3

import csv
import random
import os
from os import system, name


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
         ['##                                                              #   #   #   #########   #########   #####                                                                                             ##'],
         ['##                                                              #   #   #           #                   #                                                                                             ##'],
         ['##                                                              #####   #   #####   #   #############   #                                                                                             ##'],
         ['##                                                              #       #   #       #   #               #                                                                                             ##'],
         ['##                                                              #       #   #   #####   #########   #####                                                                                             ##'],
         ['##                                                              #       #   #           #               #                                                                                             ##'],
         ['##                                                              #   #####   #########   #   #############                                                                                             ##'],
         ['##                                                                                  # X #                                                                                                             ##'],
         ['#####################################################################################/ \################################################################################################################'],
         ['########################################################################################################################################################################################################']]
#              0   1   2   3   4   5   6   7   8   9  10   1   2   3   4   5   6   7   8   9  20   1   2   3   4   5   6   7   8   9  30   1   2   3   4   5   6   7   8   9  40   1   2   3   4   5   6   7   8

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def split(word):
    return [char for char in word]

def createmap():
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
    mapvars= [maplist,MapLoc,maxy,maxx]
    return mapvars

def displaymap(MapLoc,maplist):
    for y in range(MapLoc[0]-1,MapLoc[0]+2):            #reveals nearby map sections
        for x in range(MapLoc[1]-2,MapLoc[1]+3):
            maplist[y][x][0] = 1

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

def makemove(action,maplist,MapLoc):
    while True:
        if action in ["w"]:
            if maplist[MapLoc[0]-1][MapLoc[1]][1] == "#":
                return MapLoc
            else:
                MapLoc[0] -= 2
                return MapLoc
        elif action == "s":
            if maplist[MapLoc[0]+1][MapLoc[1]][1] == "#":
                return MapLoc
                break
            else:
                MapLoc[0] += 2
                return MapLoc
        elif action in ["d"]:
            if maplist[MapLoc[0]][MapLoc[1]+2][1] == "#":
                return MapLoc
                break
            else:
                MapLoc[1] += 4
                return MapLoc
        elif action in ["a"]:
            if maplist[MapLoc[0]][MapLoc[1]-2][1] == "#":
                return MapLoc
                break
            else:
                MapLoc[1] -= 4
                return MapLoc
        else:
            continue

mapvars= createmap()
maplist= mapvars[0]
MapLoc= mapvars[1]
maxy= mapvars[2]
maxx= mapvars[3]

def main():

    mapvars= createmap()
    maplist= mapvars[0]
    MapLoc= mapvars[1]
    maxy= mapvars[2]
    maxx= mapvars[3]

    while True:
        clear()

        print(MapLoc)
        displaymap(MapLoc,maplist)

        while True:
            action = input("Where would you like to go? \n>")
            if action in ["w","a","s","d"]:
                MapLoc= makemove(action,maplist,MapLoc)
                break
            else:
                continue

main()
