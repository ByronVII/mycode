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
         ['####                                                                                 #########---#####   #   #################                                                                             ####'],
         ['####                                                                                 |       #       #   #                   #                                                                             ####'],
         ['####                                                                                 #   #   #####   #   #####   #####   #   #                                                                             ####'],
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


#ASCII Tombstone credit to Ray Woof(?).  Grabbed from https://www.theregister.com/2004/06/24/bemer_dead_at84/
#Text generated by patorjk.com   http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
def splash2():
    clear()
    blank= (maxx-56)//2
    print("\n"*5)
    print(" "* blank,'                                                      ')
    print(" "* blank,'   /""""""/"\"""""..                                  ')
    print(" "* blank,'  /      /  /\      \            __                   ')
    print(" "* blank,' /      /        /\  \           ||                   ')
    print(" "* blank,'/_____ /  /\  |  |/   \          ||                   ')
    print(" "* blank,'|     |  |_/  | .|    |          ||                   ')
    print(" "* blank,'|     |  | \ .|       |          ||                   ')
    print(" "* blank,'|   _/|  |            |          ||                   ')
    print(" "* blank,'| _/  |               |          ||                   ')
    print(" "* blank,'|/ \_ |     * *   * * |         _||_                  ')
    print(" "* blank,'|    \|     *\/* *\/* |        |    |                 ')
    print(" "* blank,'|     |     *_\_  /   ...""""""| || |.""....""""""".."')
    print(" "* blank,'|     |    *    \/ ..""""..."""\ || /."""......""""...')
    print(" "* blank,'|     |...."""""""........""""""^^^^......."""""""".."')
    print(" "* blank,'|......"""""""""""""""........"""""...."""""..""....""')
    print()
    print(" "* blank,'                Press  Enter  to  Play                ')

def splash():
    clear()
    blank= (maxy-18)//2
    print("\n"*(blank-1))
    blank= (maxx-201)//2
    print(" "* blank,'     ***** **                                                                           /""""""/"\"""""..                                              * ***                                          ')
    print(" "* blank,'  ******  ***                                                                          /      /  /\      \            __                             *  ****  *                                       ')
    print(" "* blank,' **   *  * **                                                        ***              /      /        /\  \           ||                            *  *  ****                                        ')
    print(" "* blank,'*    *  *  **                                                        **              /_____ /  /\  |  |/   \          ||                           *  **   **                                         ')
    print(" "* blank,'    *  *   *    ***  ****    **   ****                               *   ****        |     |  |_/  | .|    |          ||                          *  ***                                              ')
    print(" "* blank,'   ** **  *      **** **** *  **    ***  *     ****    ***  ****        * **** *     |     |  | \ .|       |          ||                         **   **             ****    *** **** ****       ***  ')
    print(" "* blank,'   ** ** *        **   ****   **     ****     * ***  *  **** **** *    **  ****      |   _/|  |            |          ||                         **   **   ***      * ***  *  *** **** ***  *   * *** ')
    print(" "* blank,'   ** ***         **          **      **     *   ****    **   ****    ****           | _/  |               |          ||                         **   **  ****  *  *   ****    **  **** ****   *   ***')
    print(" "* blank,'   ** ** ***      **          **      **    **    **     **    **      ***           |/ \_ |     * *   * * |         _||_                       **   ** *  ****  **    **     **   **   **   **    ***')
    print(" "* blank,'   ** **   ***    **          **      **    **    **     **    **        ***         |    \|     *\/* *\/* |        |    |                      **   ***    **   **    **     **   **   **   ******** ')
    print(" "* blank,'   *  **     **   **          **      **    **    **     **    **          ***       |     |     *_\_  /   ...""""""| || |.""....""""""".."      **  **     *    **    **     **   **   **   *******  ')
    print(" "* blank,'      *      **   **          **      **    **    **     **    **     ****  **       |     |    *    \/ ..""""..."""\ || /."""......""""...       ** *      *    **    **     **   **   **   **       ')
    print(" "* blank,'  ****     ***    ***          *********    **    **     **    **    * **** *        |     |...."""""""........""""""^^^^......."""""""".."        ***     *     **    **     **   **   **   ****    *')
    print(" "* blank,' *  ********       ***           **** ***    ***** **    ***   ***      ****         |......"""""""""""""""........"""""...."""""..""....""         *******       ***** **    ***  ***  ***   ******* ')
    print(" "* blank,'*     ****                             ***    ***   **    ***   ***                                                                                   ***          ***   **    ***  ***  ***   *****  ')
    print(" "* blank,'*                               *****   ***                                                          Press  Enter  to  Play                                                                           ')
    print(" "* blank,' **                           ********  **                                                                                                                                                            ')
    print(" "* blank,'                             *      ****                                                                                                                                                              ')
                                                                                                                                                          
def splash3():
    print("\n"*5)
    print(" "* blank,'1   /""""""/"\"""""..                                  ')
    print(" "* blank,'2  /      /  /\      \            __                   ')
    print(" "* blank,'3 /      /        /\  \           ||                   ')
    print(" "* blank,'4/_____ /  /\  |  |/   \          ||                   ')
    print(" "* blank,'5|     |  |_/  | .|    |          ||                   ')
    print(" "* blank,'6|     |  | \ .|       |          ||                   ')
    print(" "* blank,'7|   _/|  |            |          ||                   ')
    print(" "* blank,'8| _/  |               |          ||                   ')
    print(" "* blank,'9|/ \_ |     * *   * * |         _||_                  ')
    print(" "* blank,'0|    \|     *\/* *\/* |        |    |                 ')
    print(" "* blank,'1|     |     *_\_  /   ...""""""| || |.""....""""""".."')
    print(" "* blank,'2|     |    *    \/ ..""""..."""\ || /."""......""""...')
    print(" "* blank,'3|     |...."""""""........""""""^^^^......."""""""".."')
    print(" "* blank,'4|......"""""""""""""""........"""""...."""""..""....""')
    print()
    print(" "* blank,'                Press  Enter  to  Play                ')


#set variables
def setvars():
    #player stats
    player= {"stats":{"name":"Bryan", "hp":{"current":25,"max":25}, "mana":{"current":10,"max":10},"atk":4, "def":0,"xp":[0,300]},"equipment":{"weapon":"","offhand":"","head":"","chest":"","legs":"","accessory":""},"inventory":[{"gold":0,"potion":0},'shirt','pants','hat','sword','stick']}
    #creature stats
    monsters= {"goblin":{"name":"goblin","hp":20, "atk":3}}
    #items
    items= {"gear":{"stick":{'slot':'weapon','stat':'atk',"atk":1},"sword":{'slot':'weapon','stat':'atk',"atk":3},'hat':{"slot":'head','stat':'def',"def":0},'shirt':{'slot':'chest','stat':'def','def':1},'pants':{'slot':'legs','stat':'def','def':1}},"items":{}}
    #loot
    loot= {}
    #spells
    spells= {}
    atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability
    global data
    data= {"player":player, "monsters":monsters, 'items':items, 'loot':loot, 'spells':spells}


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

def displaymap():

    head= f" Player: {data['player']['stats']['name']}   HP: {data['player']['stats']['hp']['current']}/{data['player']['stats']['hp']['max']}   MP: {data['player']['stats']['mana']['current']}/{data['player']['stats']['mana']['max']}   Location: ({MapLoc[1]}/{MapLoc[0]})"
    print(" "*int((maxx-len(head)-2)//2),head," "*int((maxx-len(head)-2)//2))
    for y in range(MapLoc[0]-1,MapLoc[0]+2):           
        for x in range(MapLoc[1]-2,MapLoc[1]+3):
            maplist[y][x][0] = 1
#creates map
    for y in range(2,len(maplist)-1):                      
        print(" "*int(((maxx-list_w)-2)//2),end="")
        for x in range(len(maplist[y])):
            if MapLoc[0] == y and MapLoc[1] == x:
                print("\33[5;37;40mo\33[0;0m",end="")
            else:
                if maplist[y][x][0] == 1:
                    if maplist[y][x][1] == "#":
                        print(f"\33[0;37;47m{maplist[y][x][1]}\33[0;0m",end="")
                    else:
                        print(f"\33[5;37;40m{maplist[y][x][1]}\33[0;0m",end="")
                else:
                    print(" ", end="")

        print()

def makemove(action):
    while True:
        if action in ["w"]:
            if maplist[MapLoc[0]-1][MapLoc[1]][1] == "#" or maplist[MapLoc[0]-2][MapLoc[1]][1] == "#":
                return MapLoc
            elif maplist[MapLoc[0]-2][MapLoc[1]][1] == "O":
                x= input("Would you like to leave the cave?\n>")
                if x in ["y","yes","yeah","yep"]:
                    print("Thanks for visiting the cave.  Have a great day!")
                    exit()
                else:
                    return MapLoc
            else:
                MapLoc[0] -= 2
                return MapLoc
        elif action == "s":
            if maplist[MapLoc[0]+1][MapLoc[1]][1] == "#" or maplist[MapLoc[0]+1][MapLoc[1]][1] == "#":
                return MapLoc
            elif maplist[MapLoc[0]+2][MapLoc[1]][1] == "O":
                x= input("Would you like to leave the cave?\n>")
                if x in ["y","yes","yeah","yep"]:
                    print("Thanks for visiting the cave.  Have a great day!")
                    exit()
                else:
                    return MapLoc
            else:
                MapLoc[0] += 2
                return MapLoc
        elif action in ["d"]:
            if maplist[MapLoc[0]][MapLoc[1]+2][1] == "#" or maplist[MapLoc[0]][MapLoc[1]+4][1]== "#":
                return MapLoc
            elif maplist[MapLoc[0]][MapLoc[1]+4][1] == "O":
                x= input("Would you like to leave the cave?\n>")
                if x in ["y","yes","yeah","yep"]:
                    print("Thanks for visiting the cave.  Have a great day!")
                    exit()
                else:
                    return MapLoc
            else:
                MapLoc[1] += 4
                return MapLoc
        elif action in ["a"]:
            if maplist[MapLoc[0]][MapLoc[1]-2][1] == "#" or maplist[MapLoc[0]][MapLoc[1]-4][1] == "#":
                return MapLoc
            elif maplist[MapLoc[0]][MapLoc[1]-4][1] == "O":
                x= input("Would you like to leave the cave?\n>")
                if x in ["y","yes","yeah","yep"]:
                    print("Thanks for visiting the cave.  Have a great day!")
                    exit()
                else:
                    return MapLoc
            else:
                MapLoc[1] -= 4
                return MapLoc
        else:
            continue

#player menu
def pmenu():
    while True:
        clear()
        pmenu= input("Pleayer Menu:\n\n  1: Stats \n  2: Equipment \n  3: Inventory \n  4: Settings\n  5: Return \n")
        clear()
        if pmenu == "1":
            print(f"Player Stats: \n\n  Name: {data['player']['stats']['name']}\n  Hit Points: {data['player']['stats']['hp']['current']}/{data['player']['stats']['hp']['max']}\n  Mana:  {data['player']['stats']['mana']['current']}/{data['player']['stats']['mana']['max']}\n  Attack: {data['player']['stats']['atk']}\n  Defense: {data['player']['stats']['def']}\n  XP: {data['player']['stats']['xp'][0]} / {data['player']['stats']['xp'][1]}\n")
            _= input()
        elif pmenu == "2":        
            emenu= input(f"Player Equipment: \n\n  Weapon: {data['player']['equipment']['weapon']} \n  Off-hand: {data['player']['equipment']['offhand']} \n\n  Head: {data['player']['equipment']['head']} \n  Chest: {data['player']['equipment']['chest']} \n  Legs: {data['player']['equipment']['legs']}\n  Accessory: {data['player']['equipment']['accessory']} \n\n  (Press c to change equipmentor Enter to go back)").lower()
            clear()
            if emenu == "c":
                slots= {1:'weapon', 2:'offhand', 3:'head', 4:'chest', 5:'legs', 6:'accessory'} 
                slot= ""
                while True:
                    slot= int(input(f"Which equipment would you like to change?\n\n  1- Weapon\n  2- Off-Hand\n\n  3- Head\n  4- Chest\n  5- Legs\n  6- Accessory\n\n"))
#                    print(type(slot))
                    if slot in [1,2,3,4,5,6]:
                        break
                    else:
                        continue
                slot= slots[slot]
                inv= []
                for i in range(1,(len(data['player']['inventory']))):
                    item= data['player']['inventory'][i]
                    if data['items']['gear'][item]['slot'] == slot:
                        inv.append(item.title())
                if inv == []:
                    print(f"No gear available for the {slot} slot.\n")
                    _=input()
                    continue
                else:
                    if data['player']['equipment'][slot] == "":
                        print("Which item would you like to equip?\n")
                        for i in range(len(inv)):    
                            print(f"  {i+1}- {inv[i]}")
                    else:
                        print(f"Which item would you like to replace {data['player']['equipment'][slot]} with?\n")
                        for i in range(len(inv)):                    
                            print(f"  {i+1}- {inv[i]}")
                        
                item= input()
                item= inv[i].lower()
                equip(item,slot)
                _= input()

            
        elif pmenu == "3":
            print(f"Inventory")
            _= input()
        elif pmenu == "4":
            print(f"Settings")
        elif pmenu == "5":
            return
        else:
            continue

def equipmenu():
    emunu1= input(f"Player Equipment: \n\n  Weapon: {data['player']['equipment']['weapon']} \n  Head: {data['player']['equipment']['head']} \n  Chest: {data['player']['equipment']['chest']} \n  Legs: {data['player']['equipment']['legs']}\n\n  (Press c to change equipmentor Enter to go back)")
    emenu1

#Put on equipment
def equip(item,slot):        #stats
    if item in data['player']['inventory']:        #checks if the item is in the players inventory
        if data['items']['gear'][item]['slot'] == slot:        #check if the item is allowed in that slot
            print(data['player']['equipment'][slot])
            if data['player']['equipment'][slot] != "":
                gear= data['player']['equipment'][slot].lower()
                gstat= data['items']['gear'][gear]['stat']
                data['player']['stats'][gstat] -= data['items']['gear'][gear][gstat] 
                data['player']['inventory'].append(gear)
                print(f"{gear.title()} was removed and put into inventory.")
            data['player']['equipment'][slot] = item.title()       #equips the item on your player 
            data['player']['stats'][data['items']['gear'][item]['stat']] += data['items']['gear'][item][data['items']['gear'][item]['stat']]        #adds item stats to player stats
            print(f"{item.title()} was equipped in the {slot} slot.")
            data['player']['inventory'].remove(item)       #removes the equipped item from inventory
        else:
            print(f"{item.title()} does not go in the {slot} slot.")
    else:
        print(f"{item} not found in inventory")
#attack results
def combat():
#    clear()
    print("Good")
    plife= data["player"]["stats"]["hp"]
    patk= data["player"]["stats"]["atk"]
    mname= data["monsters"]["goblin"]["name"]
    mlife= data["monsters"]["goblin"]["hp"]
    matk= data["monsters"]["goblin"]["atk"]
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
    global maplist,MapLoc,list_h,list_w,maxx,maxy    
    setvars()
    mapvars= createmap()
    maplist= mapvars[0]
    MapLoc= mapvars[1]
    list_h= mapvars[2]
    list_w= mapvars[3]
    maxy= split(os.get_terminal_size())[1]
    maxx= split(os.get_terminal_size())[0]
    splash()
    _=input()

    if maxx < list_w+4:
        print(f"ERROR: Terminal size too small.  Please ensure terminal is at least {list_w+4} wide and {list_h+5} high.  Terminal is currently {maxx} x {maxy}.  Thank you.")
        exit()
    elif maxy < list_h+5: 
        print(f"ERROR: Terminal size too small.  Please ensure terminal is at least {list_w+4} wide and {list_h+5} high.  Terminal is currently {maxx} x {maxy}.  Thank you.")
        exit()
        

    while True:
        clear()

        while True:
            clear()
            displaymap()
            temp= round(((maxx-len(MapLoc))/2))
            action = input("What would you like to do? \n>")
            if action in ["w","a","s","d"]:
                MapLoc= makemove(action)
                clear()
                displaymap()
#                combat()
            elif action in ["c","m"]:
                pmenu()
            elif action == "q":
                exit()
            else:
                continue

main()
