#!/usr/bin/env python3

import csv
import random
import json
import os
from random import randint as randint
from time import sleep as sleep
from os import system, name

#map maker- Vertical gaps are 1 space high, horizontal gaps are 3 spaces wide. 
#           Player moves 2 spaces verticaally at time or 4 horizontally.
#           Player will start where the X is.  X will be replaced with a blank space during map creation.
#               0   1   2   3   4   5   6   7   8   9  10   1   2   3   4   5   6   7   8   9  20   1   2   3   4   5   6   7   8   9  30   1   2   3   4   5   6   7   8   9  40   1   2   3   4   5   6   7   8
MapGrid=[['###############################################################################################################################################################################################################'],
         ['###############################################################################################################################################################################################################'],
         ['###############################################################################################################################################################################################################'],
         ['####                                                                 #               #             6 #           #                                                                                         ####'],
         ['#### #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #############   #############           #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # ####'],
         ['####                                                                 #               #               #           #                                                                                         ####'],
         ['#### #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #########   #############   #           #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # ####'],
         ['####                                                                 #   #                           #     b     #                                                                                         ####'],
         ['#### #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #############################---#####################################   #   #   #   #   #   #   #   #   #   #   #   #   #   # ####'],
         ['####                                                                 #   #   #               #             0                     #               #                                                         ####'],
         ['#### #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #############   #####   #   #################   #   #########   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # ####'],
         ['####                                                                 #       #   #           #       #   #                   #   #   #       #   #                                                         ####'],
         ['#### #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #####   #   #   #   #####   #   #####   #####   #   #   #   #   #####   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # ####'],
         ['####                                                                 #           #   #   #           #       #       #   #   #   #   #           #                                                         ####'],
         ['#### #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #########   #   #############       #####   #   #   #   #   #####   #####   #   #   #   #   #   #   #   #   #   #   #   #   #   # ####'],
         ['####                                                                 #           | 8 #               #           #   #   #   # 5 #       #   #   |                                                         ####'],
         ['#### #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #############   #   #   #####   #   #########   #   #   #   #####   #   #   #   #####   #   #   #   #   #   #   #   #   #   #   #   #   # ####'],
         ['####                                                             #           #   #   #       #   #               # 3 #   #       #   #   #       #                                                         ####'],
         ['#### #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #########   #   #   #   #   #   #########   #########   #####   #   #   #########   #   #   #   #   #   #   #   #   #   #   #   #   #   # ####'],
         ['####                                                                     #       #   # 4 #   #           #                   #   #   #           #                                                         ####'],
         ['#### #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #########   #####   #   #####   #   #############   #   #   #   #####   #####   #   #   #   #   #   #   #   #   #   #   #   #   # ####'],
         ['####                                                                     #           #       #   #       #   #               # 9 |   #   #   #     7 #                                                     ####'],
         ['#### #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #############       #   #   #####   #########   #####   #   #   #   #########   #   #   #   #   #   #   #   #   #   #   #   #   # ####'],
         ['####                                                                                 #       #   #         a #               #   #   #   #       #                                                         ####'],
         ['#### #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #####   #########   #   #############   #   #########   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # ####'],
         ['####                                                                                 #                 1 # X #                 2 #               #                                                         ####'],
         ['##########################################################################################################   ##################################################################################################'],
         ['##########################################################################################################/O\##################################################################################################'],
         ['###############################################################################################################################################################################################################']]
#               0   1   2   3   4   5   6   7   8   9  10   1   2   3   4   5   6   7   8   9  20   1   2   3   4   5   6   7   8   9  30   1   2   3   4   5   6   7   8   9  40   1   2   3   4   5   6   7   8   9 


#ASCII Tombstone credit to Ray Woof(?).  Grabbed from https://www.theregister.com/2004/06/24/bemer_dead_at84/
#Text generated by patorjk.com   http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
def splash(spl):
    clear()
    if spl == 1:
        Line1= "Press  Enter  to  Play    "
        Line2= "                          "
        Line3= "                          "
        Line4= "                          "
    if spl == 2:
        Line1= "1- New Game               "
        Line2= "2- Continue               "
        Line3= "3- Settings               "
        Line4= "4- Quit                   "
    if spl == 3:
        Line1= "You have died...          "
        Line2= "...but will you be missed?"
        Line3= "                          "
        Line4= "                          "
    blank= (maxy-18)//2
    print("\n"*(blank-1))
    blank= (maxx-201)//2
    print(" "* blank,f'     ***** **                                                                           /""""""/"\"""""..                                              * ***                                          ')
    print(" "* blank,f'  ******  ***                                                                          /      /  /\      \            __                             *  ****  *                                       ')
    print(" "* blank,f' **   *  * **                                                        ***              /      /        /\  \           ||                            *  *  ****                                        ')
    print(" "* blank,f'*    *  *  **                                                        **              /_____ /  /\  |  |/   \          ||                           *  **   **                                         ')
    print(" "* blank,f'    *  *   *    ***  ****    **   ****                               *   ****        |     |  |_/  | .|    |          ||                          *  ***                                              ')
    print(" "* blank,f'   ** **  *      **** **** *  **    ***  *     ****    ***  ****        * **** *     |     |  | \ .|       |          ||                         **   **             ****    *** **** ****       ***  ')
    print(" "* blank,f'   ** ** *        **   ****   **     ****     * ***  *  **** **** *    **  ****      |   _/|  |            |          ||                         **   **   ***      * ***  *  *** **** ***  *   * *** ')
    print(" "* blank,f'   ** ***         **          **      **     *   ****    **   ****    ****           | _/  |               |          ||                         **   **  ****  *  *   ****    **  **** ****   *   ***')
    print(" "* blank,f'   ** ** ***      **          **      **    **    **     **    **      ***           |/ \_ |     * *   * * |         _||_                       **   ** *  ****  **    **     **   **   **   **    ***')
    print(" "* blank,f'   ** **   ***    **          **      **    **    **     **    **        ***         |    \|     *\/* *\/* |        |    |                      **   ***    **   **    **     **   **   **   ******** ')
    print(" "* blank,f'   *  **     **   **          **      **    **    **     **    **          ***       |     |     *_\_  /   ...""""""| || |.""....""""""".."      **  **     *    **    **     **   **   **   *******  ')
    print(" "* blank,f'      *      **   **          **      **    **    **     **    **     ****  **       |     |    *    \/ ..""""..."""\ || /."""......""""...       ** *      *    **    **     **   **   **   **       ')
    print(" "* blank,f'  ****     ***    ***          *********    **    **     **    **    * **** *        |     |...."""""""........""""""^^^^......."""""""".."        ***     *     **    **     **   **   **   ****    *')
    print(" "* blank,f' *  ********       ***           **** ***    ***** **    ***   ***      ****         |......"""""""""""""""........"""""...."""""..""....""         *******       ***** **    ***  ***  ***   ******* ')
    print(" "* blank,f'*     ****                             ***    ***   **    ***   ***                                                                                   ***          ***   **    ***  ***  ***   *****  ')
    print(" "* blank,f'*                               *****   ***                                                          {Line1}                                                                       ')
    print(" "* blank,f' **                           ********  **                                                           {Line2}                                                                       ')
    print(" "* blank,f'                             *      ****                                                             {Line3}                                                                       ')
    print(" "* blank,f'                                                                                                     {Line4}                                                                       ')


#set variables
def setvars():
    #player stats
    player= {   "stats":   {"name":"Bryan", 'level':1,  "hp":[25,25],   "mana":[10,10], "atk":4,    "def":0,"xp":[0,30]},
                "equipment":{"weapon":"",   "offhand":"",   "head":"",  "chest":"", "legs":"",  "accessory":""},
                "inventory":[   {"gold":0,"potions":0}], 
                'abilities':{1:['power attack',0,'deals 150% damage with a 75% chance to hit.'],    2:['heal',5,'restores 30% of your max hp'],     3:['poison strike', 15,'inflicts poison on target causing damage each turn'],4:['fireball',15,'shoots a fireball at your enemies dealing damage to all enemies']}}
    #creature stats
    monsters= { 'monsters':['goblin','hobgoblin','orc','gnoll','ogre'],
                "goblin":{  "name":"goblin",  "hp":10,  "atk":3,    'xp':10,'   loot':1},
                'hobgoblin':{"name":"hobgoblin","hp":15, "atk":4,'xp':25,'loot':2},
                'orc':{"name":"orc","hp":30, "atk":7,'xp':40,'loot':3},
                'gnoll':{"name":"gnoll","hp":40, "atk":9,'xp':0,'loot':4},
                'ogre':{"name":"Ogre","hp":150, "atk":10,'xp':150,'loot':5}}
    #items
    items= {"gear":{    "stick":{'slot':'weapon','stat':'atk',"atk":1,'useable':'no'},
                        "sword":{'slot':'weapon','stat':'atk',"atk":3,'useable':'no'},
                        'hat':{"slot":'head','stat':'def',"def":1,'useable':'no'},
                        'shirt':{'slot':'chest','stat':'def','def':1,'useable':'no'},
                        'pants':{'slot':'legs','stat':'def','def':1,'useable':'no'},
                        'weapon':{'slot':'','stat':'atk','atk':1,'useable':'no'},
                        'armor':{'slot':'','stat':'def','def':1,'useable':'no'},
                        'potion':{'slot':'',"useable":"yes"},
                        'scrap1':{'slot':'','useable':'yes'},
                        'scrap2':{'slot':'','useable':'yes'},
                        'scrap3':{'slot':'','useable':'yes'}}}
    #loot
    loot= {1:[],2:[],3:[],4:[]}
    global combatenable
    combatenable = 0
    global data
    data= {"player":player, "monsters":monsters, 'items':items, 'loot':loot, 'boss': '0'}

def loadgame():
    global data, maplist, MapLoc
    savefiles = []
#    with open('savefile.csv', mode='r') as inp:
#        save= csv.DictReader(inp) 
#        print(save)
#        savefiles = {rows[0]:rows[1] for rows in save}
    
    with open('savegames2.txt','r') as savegames:
       savefiles = json.load(savegames) #savegames.readline()    
    print(savefiles)
    data = savefiles[0][0]
    maplist = savefiles[1][0]
    MapLoc = savefiles[2][0]
    _=input()

def savegame():
    global data, maplist, MapLoc

#    dict = {'data' : data, 'maplist' : maplist, 'MapLoc' : MapLoc}
#    w = csv.writer(open("savefile.csv", "w"))
#    for key, val in dict.items():
#        w.writerow([key, val])


    with open("savegames2.txt","w") as savefile:
        json.dump([data,maplist,MapLoc], savefile)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def split(word):
    return [char for char in word]

def createmap():        #creates a list for each map tile as follows maplist[enabled?][display][event]
    maplist= []
    for y in range(len(MapGrid)):            #for each vertical line in the map template
        templist= []
        maptemp= split(MapGrid[y][0])       #splits horiontal string into a list of characters
        for x in range(len(maptemp)):       #for each character in the in the horizontal string creates a list withe [0] being an enable bit to 0 or 1 and [1] being the tile ( ex. [0," "] or [0,"#"] )
            if maptemp[x][0] == "X":
                templist.append([0," ",""])    #clears the starting point 'X' from the map
                MapLoc= [y,x]
            elif maptemp[x][0] in ["/","\\"]:       #sets the cave entrance tiles to enabled '1'
                templist.append([1,maptemp[x][0],""])
            elif maptemp[x][0] in ["O"]:       #sets the cave entrance tiles to enabled '1'
                templist.append([1,"O","z"])
            elif maptemp[x][0] in ["#"]:       #sets the cave entrance tiles to enabled '1'
                templist.append([0,"#",""])    
            else:                                       
                templist.append([0," ",maptemp[x][0]])    #sets all other tiles to disabled '0'
        maplist.append(templist)

    maxy=len(maplist)
    maxx=len(maplist[0])
    mapvars= [maplist,MapLoc,maxy,maxx]
    return mapvars
    exit()

def displaymap():
    clear()
    head= f" Player: {data['player']['stats']['name']}   HP: {data['player']['stats']['hp'][0]}/{data['player']['stats']['hp'][1]}   MP: {data['player']['stats']['mana'][0]}/{data['player']['stats']['mana'][1]}   Location: ({MapLoc[1]}/{MapLoc[0]})"
    print(" "*((maxx-len(head)-2)//2),head," "*((maxx-len(head)-2)//2))
    print("\n"* ((maxy-list_h)//2))
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
            if maplist[MapLoc[0]-1][MapLoc[1]][1] == " " and maplist[MapLoc[0]-2][MapLoc[1]][1] == " ":
                MapLoc[0] -= 2
                return MapLoc
            elif maplist[MapLoc[0]-2][MapLoc[1]][1] == "O":
                x= input("Would you like to leave the cave?\n>")
                if x in ["y","yes","yeah","yep"]:
                    print("Thanks for visiting the cave.  Have a great day!")
                    exit()
                else:
                    return MapLoc
            else:
                return MapLoc

        elif action == "s":
            if maplist[MapLoc[0]+1][MapLoc[1]][1] == " " and maplist[MapLoc[0]+2][MapLoc[1]][1] == " ":
                MapLoc[0] += 2
                return MapLoc
            elif maplist[MapLoc[0]+2][MapLoc[1]][1] == "O":
                events('cave1')
                return MapLoc
#                x= input("Would you like to leave the cave?\n>")
#                if x in ["y","yes","yeah","yep"]:
#                    print("Thanks for visiting the cave.  Have a great day!")
#                    exit()
#                else:
#                    return MapLoc
            else:
                return MapLoc

        elif action in ["d"]:
            if maplist[MapLoc[0]][MapLoc[1]+2][1] == " " and maplist[MapLoc[0]][MapLoc[1]+4][1]== " ":
                MapLoc[1] += 4
                return MapLoc
            elif maplist[MapLoc[0]][MapLoc[1]+4][1] == "O":
                x= input("Would you like to leave the cave?\n>")
                if x in ["y","yes","yeah","yep"]:
                    print("Thanks for visiting the cave.  Have a great day!")
                    exit()
                else:
                    return MapLoc
            else:
                return MapLoc

        elif action in ["a"]:
            if maplist[MapLoc[0]][MapLoc[1]-2][1] == " " and maplist[MapLoc[0]][MapLoc[1]-4][1] == " ":
                MapLoc[1] -= 4
                return MapLoc
            elif maplist[MapLoc[0]][MapLoc[1]-4][1] == "O":
                x= input("Would you like to leave the cave?\n>")
                if x in ["y","yes","yeah","yep"]:
                    print("Thanks for visiting the cave.  Have a great day!")
                    exit()
                else:
                    return MapLoc
            else:
                return MapLoc
        else:
            continue
    
def intros(intro):
    if intro == 1:
        clear()
        print("\n"* ((maxy-8)//2))
        tlen= 154
        gap= " " * ((maxx-int(tlen)-2)//2)
        player= input(f"{gap}Welcome adventurer.  By what name are you known?\n\n{gap}")
        if player != "":
            data['player']['stats']['name']= player
        clear()
        print("\n"* ((maxy-8)//2))
        tlen= 154
        gap= " " * ((maxx-int(tlen)-2)//2)       
        print(f"{gap}Welcome {data['player']['stats']['name']}.\n{gap}", end="")
        sleep(2)
        print(f"You live in a small village in the middle of nowhere.\n{gap}", end="")
        sleep(2)
        print(f"Life is boring and you often find yourself dreaming about leaving the village for a more exciting life.\n{gap}", end="")
        sleep(3)
        print(f"One day while shirking chores and wandering around the outskirts of town with your dog Rusty you come across a cave entrance that you've never seen before.\n{gap}", end="")
        sleep(4)
        print(f"At first you are excited to explore, but then you hear a growl echo from the cave causing you to change your mind.\n{gap}", end="")
        sleep(4)
        print(f"As you start to back away Rusty starts barking at the entrance and then suddenly darts off into the darkness.\n{gap}", end="")
        sleep(3)
        print(f"You call Rusty's name a few times as you edge towards the opening, but the barks you hear are getting softer.\n{gap}", end="")
        sleep(3)
        print(f"You think about going to get help, but don't want to leave Rusty.  Reluctantly you enter the cave...\n\n{gap}", end="")      
        sleep(3)
        print(f"Continue...?\n{gap}", end="")
        _=input()
    if intro == 'h':
        print("Adenture Screen (screen with map):\n -To move: press w, a, s, or d and then Enter.  To pull up you character menu: press c or m followed by Enter.  For help: press h followed by enter.")
        print("Equipment Page:\n - To equip gear press the number of the slot you want to change and then Enter. (i.e. 1 is the number for your Weapon slot.).")
        _=input()
        


def events(event):
    displaymap()
    if event == '1':
        print("You found a scrap of paper.  You can check the paper again from your inventory.")
        print(f"  __________\n /  _____  /\n/  |  ___| \\\n\\  | |__   /\n/  |__  \\  \\\n\\   __)  | /\n \\ |____/ / \n/________\\\n(Press Enter to Continue.")
        data['player']['inventory'].append("scrap1")
        maplist[MapLoc[0]][MapLoc[1]][2] = ""
        _=input()
    if event == '2':
        print("You found a scrap of paper.  You can check the paper again from your inventory.")
        print(f" ___________\n|  _   _   /\n| | | | | / \n| | |_| | \\ \n| |___  | / \n|     | | \\ \n|     |_|  \\\n|__________/\n(Press Enter to Continue.")
        data['player']['inventory'].append("scrap2")
        maplist[MapLoc[0]][MapLoc[1]][2] = ""
        _=input()
    if event == '3':
        print("You found a scrap of paper.  You can check the paper again from your inventory.")
        print(f"  _________\n /   ___   |\n \\  / _ \\  |\n / | (_) | |\n \\  > _ <  |\n / | (_) | |\n/   \___/  |\n\\__________|\n(Press Enter to Continue.")
        data['player']['inventory'].append("scrap3")
        maplist[MapLoc[0]][MapLoc[1]][2] = ""
        _=input()
    if event == '4':        
        print("You found a chest.  There are three dials on front numbered 0 through 9.\nEnter the combo or press Enter to Continue.\n(Hint: perhaps the combo can be found elsewhere in the cave)")
        combo= input()
        if combo == '458':
            print("Weel done!  With a click the latch pops open.  You lift the lid and look inside.  You found a sword, 132 gold, and 2 potions.")
            data['player']['inventory'].append("sword")
            print(data['player']['inventory'][0]['gold'])
            print(type(data['player']['inventory'][0]['gold']))
            data['player']['inventory'][0]['gold'] += int(132)
            data['player']['inventory'][0]['potions'] += int(2)
            maplist[MapLoc[0]][MapLoc[1]][2] = ""
        elif combo != "":
            print("You attempt to open the chest, but the latch remains firmly in place.")
    if event == '5':
        print("You found a green key.")
        data['player']['inventory'].append("green key")
        maplist[MapLoc[0]][MapLoc[1]][2] = ""
        _=input()
    if event == '6':
        print("You found a yellow key.")
        data['player']['inventory'].append("yellow key")
        maplist[MapLoc[0]][MapLoc[1]][2] = ""
        _=input()
    if event == '7':
        print("You found a red key.")
        data['player']['inventory'].append("red key")
        maplist[MapLoc[0]][MapLoc[1]][2] = ""
        _=input()
    if event == '8':
        print("Green Door")
        maplist[MapLoc[0]][MapLoc[1]-2][1] = "\033[1;32;40m|\33[0;0m"
        displaymap()
        if 'green key' in data['player']['inventory']:
            print("You stand before a big green door.  You notice a keyhole. \nYou pull the green key out of your inventory, insert it into the keyhole, and turn the key.  The key crumbles away as the door opens with a creak.")
            maplist[MapLoc[0]][MapLoc[1]-2][1] = " "
            data['player']['inventory'].remove("green key")
            maplist[MapLoc[0]][MapLoc[1]][2] = ""
        elif 'key' in data['player']['inventory']:
            print("You stand before a big green door.  You try to unlock the door, but none of your keys work.")
        else:
            print("You stand before a big green door.  You notice a keyhole, but you don't currently have any keys.")
        _=input()

    if event == '9':
        maplist[MapLoc[0]][MapLoc[1]+2][1] = "\033[1;33;40m|\33[0;0m"
        displaymap()
        if 'yellow key' in data['player']['inventory']:
            print("You stand before a big yellow door.  You notice a keyhole. \nYou pull the yellow key out of your inventory, insert it into the keyhole, and turn the key.  The key crumbles away as the door opens with a creak.")
            maplist[MapLoc[0]][MapLoc[1]+2][1] = " "
            maplist[MapLoc[0]][MapLoc[1]][2] = ""
            data['player']['inventory'].remove("yellow key")
        elif 'key' in data['player']['inventory']:
            print("You stand before a big yellow door.  You try to unlock the door, but none of your keys work.")
        else:
            print("You stand before a big yellow door.  You notice a keyhole, but you don't currently have any keys.")
            _=input()

    if event == '0':
        for i in [-1,0,1]:
            maplist[MapLoc[0]-1][MapLoc[1]+i][1] = "\033[1;31;40m-\33[0;0m"
        displaymap()
        if 'yellow key' in data['player']['inventory']:
            print("You stand before a big red door.  You notice a keyhole. \nYou pull the red key out of your inventory, insert it into the keyhole, and turn the key.  The door opens with a creak.")
            for i in [-1,0,1]:
                maplist[MapLoc[0]+1][MapLoc[1]+i][1] = " "
                maplist[MapLoc[0]][MapLoc[1]][2] = ""
        elif 'key' in data['player']['inventory']:
            print("You stand before a big red door.  You can hear whimpering through the keyhole.  You try to unlock the door, but none of your keys work.  You try pounding on the door, but nothing happens.")
        else:
            print("You stand before a big red door.  You notice a keyhole, but you don't currently have any keys.  You can hear whimpering through the keyhole.  You try pounding on the door, but nothing happens.")
        _=input()

    if event == 'a':
        print("You take your first steps into the cave.  As your eyes are adjust to the light you trip over something.\nLooking back you find a sturdy stick.  You think to yourself that maybe having the stick might not be a bad idea.\nStick has been added to your inventory.\nTo equip your new stick go to your menu and then the equipment screen and select the weapon slot.")
        data['player']['inventory'].append("stick")
        global combatenable
        combatenable = 1
        maplist[MapLoc[0]][MapLoc[1]][1] = " "
        maplist[MapLoc[0]][MapLoc[1]][2] = ""
        _=input()

    if event == 'b':
        combat('boss')        
        data['boss'] = '1'

    if event == 'cave1':

        if data['boss'] == '1':
            print("You and Rusty smell fresh grass as you approach the cave exit.  Stepping out you feel the warm sun on your face and reflect on the ordeals you just endured.")
        else:
            print("Rusty is still lost in the cave.  You can't just abandon him!")
        _=input()


#main menu
def mmenu():
    while True:
        splash(2)
        menus= int(input())
        if menus == 1:
            setvars()
            break
        elif menus == 2:
            loadgame()
            break
        elif menus == 3:
            continue
        elif menus == 4:
            exit()
        else:
            continue

#player menu
def pmenu():
    while True:
        clear()
        pmenu= input("Pleayer Menu:\n\n  1: Stats \n  2: Equipment \n  3: Inventory \n  4: Abilities\n  5: Save \n  6: Main Menu \n  7: Return \n")
        clear()
        if pmenu == "1":
            print(f"Player Stats: \n\n  Name: {data['player']['stats']['name']}\n  Level: {data['player']['stats']['level']}\n  Hit Points: {data['player']['stats']['hp'][0]}/{data['player']['stats']['hp'][1]}\n  Mana:  {data['player']['stats']['mana'][0]}/{data['player']['stats']['mana'][1]}\n  Attack: {data['player']['stats']['atk']}\n  Defense: {data['player']['stats']['def']}\n  XP: {data['player']['stats']['xp'][0]} / {data['player']['stats']['xp'][1]}\n")
            _= input()
        elif pmenu == "2":        
            ifequip = equipmenu()
        elif pmenu == "3":
            inv= data['player']['inventory']
            print(f"Inventory:")
            print(f" -Gold: {inv[0]['gold']}\n -Potions: {inv[0]['potions']}")
            for i in range(1,len(inv)):
                print(f" -{inv[i].title()}")
            use= input("Press e + Enter if you would like to use an item or just Enter to continue." )
            if use == "e":
                useitem()
        elif pmenu == "4":
            for a in range(1, data['player']['stats']['level']+1):
                print(f"{a}- {data['player']['abilities'][a][0]}   MP: {data['player']['abilities'][a][1]}\n  -{data['player']['abilities'][a][2]}\n  ")
            abilmen= input("\nPress ability number to use ability or Enter to continue.\n")
            if abilmen == '2':
                abil = ability(2)
                if abil[0] == 2 and abil[1] == 0:
                    result1 = "You do not have enough mana"
                elif abil[0] == 2:
                    result1 = f"You healed {abil[1]} life."
                print(abil)
                print(result1)                
                _=input()
            else:
                print("That ability can only be used during combat.")

        elif pmenu == "5":
            savegame()
            _=input("Game Saved.  Press Enter to continue.")
        elif pmenu == "6":
            mmenu()
        elif pmenu == "7":
            return
        elif pmenu == 'h':
            intros('h')
        else:
            continue

def equipmenu():
    while True:
        clear()
        displaymap()
        slots= {1:'weapon', 2:'offhand', 3:'head', 4:'chest', 5:'legs', 6:'accessory'}
        slot= ""
        while True:
            slot= input(f"Player EquipVment: \n\n  1: Weapon: {data['player']['equipment']['weapon']} \n  2: Off-hand: {data['player']['equipment']['offhand']} \n\n  3: Head: {data['player']['equipment']['head']} \n  4: Chest: {data['player']['equipment']['chest']} \n  5: Legs: {data['player']['equipment']['legs']}\n  6: Accessory: {data['player']['equipment']['accessory']} \n\n  (Press slot number to change equipment or Enter to go back)\n  ").lower()
            if slot in ['1','2','3','4','5','6']:
                slot= int(slot)
                break
            elif slot == "":
                return
            else:
                continue
        slot= slots[slot]
        while True:
            inv= []
            for i in range(1,(len(data['player']['inventory']))):
                item= data['player']['inventory'][i]
                if data['items']['gear'][item]['slot'] == slot:
                    inv.append(item.title())
            if inv == []:
                print(f"No gear available for the {slot} slot.\n")
                _=input()
                return 
            else:

                if data['player']['equipment'][slot] == "":
                    print("Which item would you like to equip?\n")
                    for i in range(len(inv)):
                        print(f"  {i+1}- {inv[i]}")
                else:
                    print(f"Which item would you like to replace {data['player']['equipment'][slot]} with?\n")
                    for i in range(len(inv)):
                        print(f"  {i+1}- {inv[i]}")
            itemnum= input()
            if itemnum > '0' and itemnum <= str(i+1):
                itemnum = int(itemnum)
                break
            elif itemnum =="":
                return 0
        item= inv[itemnum-1].lower()
        equip(item,slot)
        _= input()
        return 1

#Put on equipment
def equip(item,slot):        #stats
    clear()
    displaymap()
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
            idata['player']['inventory'].remove(item)       #removes the equipped item from inventory
        else:
            print(f"{item.title()} does not go in the {slot} slot.")
    else:
        print(f"{item} not found in inventory")
#attack results
def combat(monster):
    if monster == 'boss':
        mon = 'ogre'
    else:
        mon= randint(1, data['player']['stats']['level'])         #data["monsters"]["goblin"]["name"]
    patk= data["player"]["stats"]["atk"]
    pdef= data['player']['stats']['def']
    mname= data['monsters']['monsters'][mon-1]
    mlife= data["monsters"][mname]["hp"]
    matk= data["monsters"][mname]["atk"]
    atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability
    dmg= 0

    print(f"Youn encounter {mname}.")

    while data["player"]["stats"]["hp"][0] > 0 and mlife > 0:
        while True:
            fmenu= (input("What would you like to do?\n  1- Attack\n  2- Ability\n  3- Use item\n  4- Change Equipment\n  5- Escape\n"))
            if fmenu == 'cheatkiller':
                print("You dirty cheater.......\nWell, I guess the monster dies...\n....I hope you are at least suitably embarrassed...")
                _=input()  
                data['player']['stats']['xp'][0] += data['monsters']['goblin']['xp']
                if data['player']['stats']['xp'][0] >= data['player']['stats']['xp'][1]:
                    levelup()
                    _=input()
                return
            if fmenu == '1':
                clear()
                displaymap()
                dmg = patk + random.choice(atkvar)
                mlife -= dmg
                result1 = f"You hit {mname} for {dmg}.  {mname} is down to {mlife} life."
                break
            elif fmenu == '2':
                abil= []
                abil= ability(0)
                if abil[0] == 1 and abil[1] == 1:
                    clear()
                    displaymap()
                    dmg = round((patk + random.choice(atkvar)) * 1.5)
                    mlife -= dmg
                    result1 = f"You hit {mname} with a powerful blow for {dmg}.  {mname} is down to {mlife} life."
                    break
                elif abil[0] == 1 and abil[1] == 0:
                    result1 = "You swing wildly, but miss your target."
                elif abil[0] == 2 and abil[1] == 0:
                    result1 = "You do not have enough mana"
                elif abil[0] == 2:
                    result1 = f"You healed {abil[1]} life."

                break
            elif fmenu == '3':
                useitem()
                break
            elif fmenu == '4':
                ifequip = equipmenu()
                if ifequip == 0:
                    continue
                else:
                    break
            elif fmenu == '5':
                plvl= data['player']['stats']['level']
                mlvl= mon
                esc = randint(1,plvl+1)                
                clear()
                displaymap()
                if esc > mlvl:
                    print(f"You managed to escape the {mname}.")
                    sleep(2)
                    return
                else:
                    result1 = f"You try to escape the {mname}, but can't get away."
                    break
            else:
                displaymap()
                continue

        dmg = matk + random.choice(atkvar) - pdef
        if dmg < 1:
            result2 = f"{mname} missed you."
        else:
            data["player"]["stats"]["hp"][0] -= dmg
            result2 = f'{mname} hit you for {dmg}.  You are down to {data["player"]["stats"]["hp"][0]} life.'
        displaymap()
        print(result1)
        print(result2)

#fight results
    if data["player"]["stats"]["hp"][0] < 1 and mlife < 1:         #both player and creature died
        print(f"You managed to slay the {mname}, however, your own injuries are too grevious and you too succumb to death.")
        sleep(2)
        print("How embarassing.")
        sleep(2)
        splash2()
        mmenu
    elif data["player"]["stats"]["hp"][0]< 1:         #only the player died
        print("You have died...")
        sleep(1)
        print("Seriously...")
        sleep(1)
        print(f"You couldn't defeat a single {mname}?")
        sleep(1)
        print("You're parents are very dissapointed in you...")
        sleep(2)
        print("...but more importantly.  So am I...")
        splash2()
        mmenu
    else:               #only goblin dies
        print(f"You defeated {mname}!  Are you proud of yourself?  You really shouldn't be.")
        data['player']['stats']['xp'][0] += data['monsters']['goblin']['xp']
        if data['player']['stats']['xp'][0] >= data['player']['stats']['xp'][1]:
            levelup()


    _= input("Press enter to continue.")

def ability(abilmen):
    while True:
        if abilmen == 2:
            abil = '2'
        else:
            print("Available abilities.  Which would you like to use?")
            for a in range(1,data['player']['stats']['level']+1):
                print(f"{a}- {data['player']['abilities'][a][0]}     MP: {data['player']['abilities'][a][1]}\n")
            abil= input()
        if abil == "1":
            if randint(1,4) != 1:
                return [1,1]
            else:
                return [1,0]
            break
        if abil == '2':
            if data['player']['stats']['mana'][0] >= 5:
                data['player']['stats']['mana'][0] -= 5
                heal= int(data['player']['stats']['hp'][1] *.3)
                data['player']['stats']['hp'][0] += heal
                int(data['player']['stats']['hp'][1] *.3)
                if data['player']['stats']['hp'][0] > data['player']['stats']['hp'][1]: 
                    heal = heal - (data['player']['stats']['hp'][0] - data['player']['stats']['hp'][1])
                    data['player']['stats']['hp'][0] = data['player']['stats']['hp'][1]
                return [2,heal]
            else:
                return [2,0]



def useitem():
    global data
    inv = []
    for i in range(1,len(data['player']['inventory'])):
        item= data['player']['inventory'][i]
        useable= data['items']['gear'][item]['useable']
        if useable == 'yes':
            inv.append(item)
    print(f"What would you like to use?\n 1- Potion: {data['player']['inventory'][0]['potions']}\n")
    for i in range(len(inv)):
         print(f" {i+2}- {inv[i]}")
    use =input()
    if use == '1':
        if data['player']['inventory'][0]['potions'] > 0:
            data['player']['stats']['hp'][0] += 15
            if data['player']['stats']['hp'][0] > data['player']['stats']['hp'][1]:
                data['player']['stats']['hp'][0] = data['player']['stats']['hp'][1]
            data['player']['inventory'][0]['potions'] -= 1
        else:
            print("You are out of potions.")
#            _=input()
    elif len(inv) > 0:
        item= inv[int(use)-2]          
        if item == "scrap1":
            clear()
            print(f"  __________\n /  _____  /\n/  |  ___| \\\n\\  | |__   /\n/  |__  \\  \\\n\\   __)  | /\n \\ |____/ / \n/________\\\n(Press Enter to Continue.")
        if item == 'scrap2':
            clear()
            print(f" ___________\n|  _   _   /\n| | | | | / \n| | |_| | \\ \n| |___  | / \n|     | | \\ \n|     |_|  \\\n|__________/\n(Press Enter to Continue.")
        if item == 'scrap3':
            clear()
            print(f"  _________\n /   ___   |\n \\  / _ \\  |\n / | (_) | |\n \\  > _ <  |\n / | (_) | |\n/   \___/  |\n\\__________|\n(Press Enter to Continue.")
    _=input()

def levelup():
    clear()
    lvl= data['player']['stats']['level']
    data['player']['stats']['hp'][1] += (10 + 5 * data['player']['stats']['level'])
    data['player']['stats']['level'] += 1
    lvl= data['player']['stats']['level']
    data['player']['stats']['xp'][1] *= 3
    data['player']['stats']['atk'] += 2
    data['player']['stats']['def'] += 1
    data['player']['stats']['mana'][1] += 10
    data['player']['stats']['hp'][0] = data['player']['stats']['hp'][1]
    data['player']['stats']['mana'][0] = data['player']['stats']['mana'][1]
    print(f"Congratulations!  You have gained enough experience to advance to Level {lvl}\n  You gained {10 + 5 * (lvl-1)} Max Hit Points, 10 Max Mana, 2 Attack, and 1 Defense.\n  Your Hit Points and Mana were restored to full.\n  You have gained the {data['player']['abilities'][lvl][0].title()}.\n  {data['player']['abilities'][lvl][0].title()} {data['player']['abilities'][lvl][2]} for {data['player']['abilities'][lvl][1]} Mana.")

def cheatmenu(c):
    clear()
    global combatenable
    print("\n"* ((maxy-8)//2))
    tlen= 107
    gap= " " * ((maxx-int(tlen)-2)//2)
    print(f"{gap}HOW DARE YOU INVOKE THE SACRED CODE ON THE PITIFUL EXCUSE FOR A GAME!?!?!?\n{gap}Konami has been notified of this egregious infraction and their lawyers will be in contact with you shortly.")
    if combatenable == 1:
        combatval= "Disable"
    else:
        combatval= "Enable"
    cheat= input(f"Well, how would you like to break my game?\n 1- {combatval} combat\n 2- Full health\n")
    if cheat == '1':
        if combatenable == 1:
            combatenable= 0
        else:
            combatenable= 1
    
    if cheat == '2':
        print("Wow.  What an original cheat...  Well, ok.  You now have full health.")
        data['player']['stats']['hp'][0] = data['player']['stats']['hp'][1]



mapvars= createmap()
maplist= mapvars[0]
MapLoc= mapvars[1]
maxy= mapvars[2]
maxx= mapvars[3]

def main():
    setvars()
    global maplist,MapLoc,list_h,list_w,maxx,maxy    
    boss = '0'
    mapvars= createmap()
    maplist= mapvars[0]
    MapLoc= mapvars[1]
    list_h= mapvars[2]
    list_w= mapvars[3]
    maxy= split(os.get_terminal_size())[1]
    maxx= split(os.get_terminal_size())[0]
    if maxx < list_w+2 or maxy < list_h+5:
        print(f"ERROR: Terminal size too small.  Please ensure terminal is at least {list_w+4} wide and {list_h+5} high.  Terminal is currently {maxx} x {maxy}.  Thank you.")
        exit()
    splash(1)
    _=input()
    while True:
        splash(2)
        menus= input()
        if menus == '1':
            setvars()
            break
        elif menus == '2':
            loadgame()
            break
        elif menus == '3':
            continue
        elif menus == '4':
            exit()
        else:
            continue

#checks that the terminal is big enough for the game
    if maxx < list_w+2 or maxy < list_h+5:
        print(f"ERROR: Terminal size too small.  Please ensure terminal is at least {list_w+4} wide and {list_h+5} high.  Terminal is currently {maxx} x {maxy}.  Thank you.")
        exit()
    intros(1)
    displaymap()
    turn = 0
    print("This is your interface.  To the south of you (down) is the cave entrance.  Ahead of you (up) is the cave.  You can't see much yet, but you hear barkin echoing from somewhere deeper in the cave.\nTo move: press w, a, s, or d and then Enter.  To open your character menu: press c or m followed by Enter.  For help: press h followed by enter.\n\nPress Enter to begin...")
    _=input()
    while True:
        while True:
            clear()
            displaymap()
            turn += 1
            action = input("What would you like to do? (Press h + Enter for help)\n>")
            if action in ["w","a","s","d"]:
                MapLoc= makemove(action)
                if turn % 4 == 0:
                    if data['player']['stats']['hp'][0] < data['player']['stats']['hp'][1]:
                        data['player']['stats']['hp'][0] +=1
                if turn % 8 == 0:
                    if data['player']['stats']['mana'][0] < data['player']['stats']['mana'][1]:
                        data['player']['stats']['mana'][0] +=1
                clear()
                displaymap()
                if combatenable == 1:
                    if randint(1,4) == 1:
                        combat(0)
                if maplist[MapLoc[0]][MapLoc[1]][2] != " ":
                    events(maplist[MapLoc[0]][MapLoc[1]][2])
            elif action in ["c","m"]:
                pmenu()
            elif action in ['h','help']:
                intros('h')
            elif action in ['uuddlrlrbastart']:
                cheatmenu(0)
            elif action == "q":
                exit()
            else:
                continue

main()
