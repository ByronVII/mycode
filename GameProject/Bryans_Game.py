#!/usr/bin/env python3

import csv
import random
from time import sleep as sleep
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

#set variables
def setvars():
    #player stats
    player= {"name":"Bryan", "life":25, "attack": 4}
    #creature stats
    monsters= {"goblin":{"name":"goblin","life":20, "attack":3}}
    atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability
    stats= {"player":player, "monsters":monsters}
    return stats

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

#attack results
def combat(stats):
#    clear()
    print("Good")
    plife= stats["player"]["life"]
    patk= stats["player"]["attack"]
    mname= stats["monsters"]["goblin"]["name"]
    mlife= stats["monsters"]["goblin"]["life"]
    matk= stats["monsters"]["goblin"]["attack"]
    atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability
    dmg= 0

    while True:
        fight= input("Youn encounter a goblin.  Do you want to 'fight' it or 'run'?").lower()
        if fight.lower() not in ["r", "run", "fight", "f"]:
            print("Command not valid.  Please enter a valid command.  (fight or run): ")
        else:
            break

    if fight.lower() in ["r", "run"]:
        print("Coward...")
        exit()
    elif fight.lower() in ["f", "fight"]:
        clear()
        print(f"You muster your courage and square up against the {mname}.")
    
    while plife > 0 and mlife > 0:
        print()
        dmg = patk + random.choice(atkvar)      #calculates players damage for this round
        mlife -= dmg                            #applies damge to goblins life total
        print(f"You hit the {mname} for {dmg} damage.  It is down to {mlife} life remaining.")
        dmg = matk + random.choice(atkvar)      #calculates goblins damage for this round
        plife -= dmg                            #applies damge to players life total
        print(f"The {mname} hit you for {dmg} damage.  You are down to {plife} life remaining.")
        sleep(1)

#fight results
    if  plife < 1 and mlife < 1:         #both player and creature died
        print(f"You managed to slay the mname, however, your own injuries are too grevious and you too succumb to death.")
        sleep(1)
        print("How embarassing.")
    elif plife < 1:         #only the player died
        print("You have died...")
        sleep(1)
        print("Seriously...")
        sleep(1)
        print(f"You couldn't defeat a single {mname}?")
        sleep(1)
        print("You're parents are very dissapointed in you...")
        sleep(2)
        print("...but more importantly.  So am I...")
    else:               #only goblin dies
        print(f"You managed to slay a {mname}!  Are you proud of yourself?  You really shouldn't be.")

    _= input("Press enter to continue.")





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
    stats= setvars()

    while True:
        clear()

        while True:
            clear()
            displaymap(MapLoc,maplist)
            action = input("Where would you like to go? \n>")
            if action in ["w","a","s","d"]:
                MapLoc= makemove(action,maplist,MapLoc)
                clear()
                displaymap(MapLoc,maplist)
                combat(stats)
                #break
            else:
                continue

main()
