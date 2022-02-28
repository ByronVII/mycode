#!/usr/bin/env python3

import csv
import random
from time import sleep as sleep
import os
from os import system, name

#map maker- Vertical gaps are 1 space high, horizontal gaps are 3 spaces wide. 
#           Player moves 2 spaces verticaally at time or 4 horizontally.
#           Player will start where the X is.  X will be replaced with a blank space during map creation.
#              0   1   2   3   4   5   6   7   8   9  10   1   2   3   4   5   6   7   8   9  20   1   2   3   4   5   6   7   8   9  30   1   2   3   4   5   6   7   8   9  40   1   2   3   4   5   6   7   8
MapGrid=[['###############################################################################################################################################################################################################'],
         ['###############################################################################################################################################################################################################'],
         ['###############################################################################################################################################################################################################'],
         ['####                                                                                                                                                                                                       ####'],
         ['####                                                                                                                                                                                                       ####'],
         ['####                                                                                                                                                                                                       ####'],
         ['####                                                                                                                                                                                                       ####'],
         ['####                                                                                                                                                                                                       ####'],
         ['####                                                                                                                                                                                                       ####'],
         ['####                                                                                                                                                                                                       ####'],
         ['####                                                                                                 #   #   #################                                                                             ####'],
         ['####                                                                                 #   #           #   #                   #                                                                             ####'],
         ['####                                                                                 #   #           #   #####   #####   #   #                                                                             ####'],
         ['####                                                                                 #   #           #       #       #   #   #                                                                             ####'],
         ['####                                                                                 #   #############       #####   #   #   #                                                                             ####'],
         ['####                                                                                 #               #           #   #   #   #                                                                             ####'],
         ['####                                                                                 #   #####   #   #########   #   #   #   #                                                                             ####'],
         ['####                                                                                 #       #   #               #   #   #                                                                                 ####'],
         ['####                                                                                 #   #   #   #########   #########   #####                                                                             ####'],
         ['####                                                                                 #   #   #           #                   #                                                                             ####'],
         ['####                                                                                 #####   #   #####   #   #############   #                                                                             ####'],
         ['####                                                                                 #       #   #       #   #               #                                                                             ####'],
         ['####                                                                                 #       #   #   #####   #########   #####                                                                             ####'],
         ['####                                                                                 #       #   #           #               #                                                                             ####'],
         ['####                                                                                 #   #####   #########   #   #############                                                                             ####'],
         ['####                                                                                                     # X #                                                                                             ####'],
         ['##########################################################################################################   ##################################################################################################'],
         ['##########################################################################################################/O\##################################################################################################'],
         ['###############################################################################################################################################################################################################']]
#              0   1   2   3   4   5   6   7   8   9  10   1   2   3   4   5   6   7   8   9  20   1   2   3   4   5   6   7   8   9  30   1   2   3   4   5   6   7   8   9  40   1   2   3   4   5   6   7   8   9 

#set variables
def setvars():
    #player stats
    player= {"stats":{"name":"Bryan", "hp":25, "atk":4, "def":2,"xp":[0,300]},"equipment":{"weapon":"Sword","head":"Hat","chest":"Shirt","legs":"Pants"},"inventory":{"gold":0,"potion":0}}
    #creature stats
    monsters= {"goblin":{"name":"goblin","hp":20, "atk":3}}
    #items
    items= {"weapons":{"Sword":{"atk":3}},"armor":{},"items":{}}
    #loot
    loot= {}
    #spells
    spells= {}
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
    for y in range(len(MapGrid)):            #for each vertical line in the map template
        templist= []
        maptemp= split(MapGrid[y][0])       #splits horiontal string into a list of characters
        for x in range(len(maptemp)):       #for each character in the in the horizontal string creates a list withe [0] being an enable bit to 0 or 1 and [1] being the tile ( ex. [0," "] or [0,"#"] )
            if maptemp[x][0] == "X":
                templist.append([0," "])    #clears the starting point 'X' from the map
                MapLoc= [y,x]
            elif maptemp[x][0] in ["O","/","\\"]:       #sets the cave entrance tiles to enabled '1'
                templist.append([1,maptemp[x][0]])
            else:                                       #sets all other tiles to disabled '0'
                templist.append([0,maptemp[x][0]])
        maplist.append(templist)

    maxy=len(maplist)
    maxx=len(maplist[0])
    mapvars= [maplist,MapLoc,maxy,maxx]
    return mapvars
    exit()

def displaymap(MapLoc,maplist,stats,maxx,list_w):
#reveals nearby map sections
    head= f" Player: {stats['player']['stats']['name']}       Location: ({MapLoc[1]}/{MapLoc[0]})"
    print(" "*int((maxx-len(head)-2)/2),head," "*int((maxx-len(head)-2)/2))
    for y in range(MapLoc[0]-1,MapLoc[0]+2):           
        for x in range(MapLoc[1]-2,MapLoc[1]+3):
            maplist[y][x][0] = 1
#creates map
    for y in range(2,len(maplist)-1):                      
        print(" "*int(((maxx-list_w)-2)/2),end="")
        for x in range(len(maplist[y])):
            if MapLoc[0] == y and MapLoc[1] == x:
                print("o",end="")
            else:
                if maplist[y][x][0] == 1:
                    print(maplist[y][x][1],end="")
                else:
                    print(" ", end="")

        print()

def makemove(action,maplist,MapLoc,maxx,list_w):
    while True:
        if action in ["w"]:
            if maplist[MapLoc[0]-1][MapLoc[1]][1] == "#":
                return MapLoc
            elif maplist[MapLoc[0]-1][MapLoc[1]][1] == "O":
                print("You can't leave the cave yet.")
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

#player menu
def pmenu(stats):
    while True:
        clear()
        pmenu= input("Pleayer Menu:\n\n  1: Stats \n  2: Equipment \n  3: Inventory \n  4: Return \n")
        clear()
        if pmenu == "1":
#            print(f"Player Stats: \n\n -Name: {stats['player']['stats']['name']}\n -Hit Points: {stats['player']['stats']['hp']}\n -Attack: {stats['player']['stats']['atk']}\n -Defense: {stats['player']['stats']['def']}\n -XP: {stats['player']['stats']['xp'][0]} / {stats['player']['stats']['xp'][1]}\n")
            print(f"Player Stats: \n\n  Name: {stats['player']['stats']['name']}\n  Hit Points: {stats['player']['stats']['hp']}\n  Attack: {stats['player']['stats']['atk']}\n  Defense: {stats['player']['stats']['def']}\n  XP: {stats['player']['stats']['xp'][0]} / {stats['player']['stats']['xp'][1]}\n")
            _= input()
        elif pmenu == "2":        
#            print(f"Player Equipment: \n\n -Weapon: {stats['player']['equipment']['weapon']} \n -Head: {stats['player']['equipment']['head']} \n -Chest: {stats['player']['equipment']['chest']} \n -Legs: {stats['player']['equipment']['legs']}")
            print(f"Player Equipment: \n\n  Weapon: {stats['player']['equipment']['weapon']} \n  Head: {stats['player']['equipment']['head']} \n  Chest: {stats['player']['equipment']['chest']} \n  Legs: {stats['player']['equipment']['legs']}")
            _= input()
        elif pmenu == "3":
            print(f"Inventory")
            _= input()
        elif pmenu == "4":
            return
        else:
            continue

#attack results
def combat(stats):
#    clear()
    print("Good")
    plife= stats["player"]["stats"]["hp"]
    patk= stats["player"]["stats"]["atk"]
    mname= stats["monsters"]["goblin"]["name"]
    mlife= stats["monsters"]["goblin"]["hp"]
    matk= stats["monsters"]["goblin"]["atk"]
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
    list_h= mapvars[2]
    list_w= mapvars[3]
    maxy= split(os.get_terminal_size())[1]
    maxx= split(os.get_terminal_size())[0]
    stats= setvars()
    if maxx < list_w+4:
        print(f"ERROR: Terminal size too small.  Please ensure terminal is at least {list_w+4} wide and {list_h+10} high.  Terminal is currently {maxx} x {maxy}.  Thank you.")
        exit()
    elif maxy < list_h+10: 
        print(f"ERROR: Terminal size too small.  Please ensure terminal is at least {list_w+4} wide and {list_h+10} high.  Terminal is currently {maxx} x {maxy}.  Thank you.")
        exit()


    while True:
        clear()

        while True:
            clear()
            displaymap(MapLoc,maplist,stats,maxx,list_w)           
            temp= round(((maxx-len(MapLoc))/2))
#            print(split(os.get_terminal_size()))
#            print(maxx, " , ", maxy)
#            print(temp)
#            print(" " * temp, MapLoc)
            action = input("Where would you like to go? \n>")
            if action in ["w","a","s","d"]:
                MapLoc= makemove(action,maplist,MapLoc,maxx,list_w)
                clear()
                displaymap(MapLoc,maplist,stats,maxx,list_w)
#                combat(stats)
            elif action in ["c","m"]:
                pmenu(stats)
            else:
                continue

main()
