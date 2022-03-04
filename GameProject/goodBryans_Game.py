#!/usr/bin/env python3

import csv,random,json,os
from random import randint as randint
from time import sleep as sleep
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
def splash(spl):
    clear()
    if spl == 1:
        Line1= "Press  Enter  to  Play"
        Line2= "                      "
        Line3= "                      "
        Line4= "                      "
    if spl == 2:
        Line1= "1- New Game           "
        Line2= "2- Continue           "
        Line3= "3- Settings           "
        Line4= "4- Quit               "
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
    print(" "* blank,f'*                               *****   ***                                                          {Line1}                                                                           ')
    print(" "* blank,f' **                           ********  **                                                           {Line2}                                                                           ')
    print(" "* blank,f'                             *      ****                                                             {Line3}                                                                           ')
    print(" "* blank,f'                                                                                                     {Line4}                                                                           ')

def splash2():
    print("Game Over")

#set variables
def setvars():
    #player stats
    player= {"stats":
                    {"name":"Bryan",'level':1,"hp":[25,25], "mana":[10,10],"atk":4, "def":0,"xp":[0,10]},
                    "equipment":{"weapon":"","offhand":"","head":"","chest":"","legs":"","accessory":""},"inventory":[{"gold":0,"potion":0},'shirt','pants','hat','sword','stick'],'abilities':{1:['power attack',0,'deals 150% damage with a 75% chance to hit.'],2:['heal',5,'restores 30% of your max hp'],3:['fireball',15,'shoots a fireball at your enemies dealing damage to all enemies']}}
    #creature stats
    monsters= {"goblin":
            {"name":"goblin","hp":10, "atk":3,'xp':10,'loot':1},'hobgoblin':{"name":"hobgoblin","hp":15, "atk":3,'xp':10,'loot':1},'orc':{},'gnoll':{},'ogre':{},'monsters':['goblin','hobgoblin','orc','gnoll','ogre']}
    #items
    items= {"gear":{"stick":{'slot':'weapon','stat':'atk',"atk":1},"sword":
        {'slot':'weapon','stat':'atk',"atk":3},'hat':{"slot":'head','stat':'def',"def":1},'shirt':{'slot':'chest','stat':'def','def':1},'pants':{'slot':'legs','stat':'def','def':1},'weapon':{'slot':'','stat':'atk','atk':1},'armor':{'slot':'','stat':'def','def':1}},"items":{}}
    #loot
    loot= {}
    #spells
    spells= {}
    atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability
    global data
    data= {"player":player, "monsters":monsters, 'items':items, 'loot':loot, 'spells':spells}

def loadgame():
    global data, maplist, MapLoc
    with open('savegames.txt','r') as savegames:
       savegame = json.load(savegames) #savegames.readline()    
#    print(savegame)
    data = savegame[0]
    maplist = savegame[1]
    MapLoc = savegame[2]

def savegame():
    with open("savegames.txt","w") as savefile:
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
            for a in range(1, data['player']['stats']['level']+1):
                print(f"{a}- {data['player']['abilities'][a][0]}   MP: {data['player']['abilities'][a][1]}\n  -{data['player']['abilities'][a][2]}\n  ")
            abil= input("Press ability number to use ability or Enter to continue.")

        elif pmenu == "5":
            savegame()
            _=input("Game Saved.  Press Enter to continue.")
        elif pmenu == "6":
            mmenu()
        elif pmenu == "7":
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
#    global data
    plife= data["player"]["stats"]["hp"][0]
    patk= data["player"]["stats"]["atk"]
    pdef= data['player']['stats']['def']
    mon= randint(1, data['player']['stats']['level'])         #data["monsters"]["goblin"]["name"]
    mname= data['monsters']['monsters'][mon-1]
    mlife= data["monsters"][mname]["hp"]
    matk= data["monsters"][mname]["atk"]
    atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability
    dmg= 0

    print(f"Youn encounter {mname}.")

    while plife > 0 and mlife > 0:
        while True:
            fmenu= (input("What would you like to do?\n  1- Attack\n  2- Ability\n  3- Use item\n  4- Change Equipment\n  5- Escape\n"))
            if fmenu == '1':
                clear()
                displaymap()
                dmg = patk + random.choice(atkvar)
                mlife -= dmg
                print(f"You hit {mname} for {dmg}.  {mname} is down to {mlife} life.")
                break
            elif fmenu == '2':
                abil= []
                abil= ability()
                if abil[0] == 1 and abil[1] == 1:
                    clear()
                    displaymap()
                    dmg = round((patk + random.choice(atkvar)) * 1.5)
                    mlife -= dmg
                    print(f"You hit {mname} with a powerful blow for {dmg}.  {mname} is down to {mlife} life.")
                    break
                elif abil[0] == 1 and abil[1] == 0:
                    print("You swing wildly, but miss your target.")

                break
            elif fmenu == '3':
                useitem()
                break
            elif fmenu == '4':
                equip()
                break
            elif fmenu == '5':
                print("Escape")
                break
            else:
                continue
        dmg = matk + random.choice(atkvar) - pdef
        if dmg < 1:
            print(f"{mname} missed you.")
        else:
            plife -= dmg
            print(f"{mname} hit you for {dmg}.  You are down to {plife} life.")
    data["player"]["stats"]["hp"][0] = plife

#fight results
    if  plife < 1 and mlife < 1:         #both player and creature died
        print(f"You managed to slay the {mname}, however, your own injuries are too grevious and you too succumb to death.")
        sleep(1)
        print("How embarassing.")
        splash2()
        mmenu
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
        splash2()
        mmenu
    else:               #only goblin dies
        print(f"You defeated {mname}!  Are you proud of yourself?  You really shouldn't be.")
        data['player']['stats']['xp'][0] += data['monsters']['goblin']['xp']
        if data['player']['stats']['xp'][0] >= data['player']['stats']['xp'][1]:
            levelup()


    _= input("Press enter to continue.")

def ability():
    while True:
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


def useitem():
    print("Use Item")

def levelup():
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
    print(f"Congratulations!  You have gained enough experience to advance to Level {lvl}\n  You gained {10 + 5 * (lvl-1)} Max Hit Points, 10 Max Mana, 2 Attack, and 1 Defense.\n  You have gained the {data['player']['abilities'][lvl][0].title()}.\n  {data['player']['abilities'][lvl][0].title()} {data['player']['abilities'][lvl][2]} for {data['player']['abilities'][lvl][1]} Mana.")



mapvars= createmap()
maplist= mapvars[0]
MapLoc= mapvars[1]
maxy= mapvars[2]
maxx= mapvars[3]

def main():
    setvars()
    global maplist,MapLoc,list_h,list_w,maxx,maxy    
    mapvars= createmap()
    maplist= mapvars[0]
    MapLoc= mapvars[1]
    list_h= mapvars[2]
    list_w= mapvars[3]
    maxy= split(os.get_terminal_size())[1]
    maxx= split(os.get_terminal_size())[0]
    splash(1)
    _=input()
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

#    with open("savegames.txt","w") as savefile:
#        json.dump(data, savefile)

#    save= 2
#    savegame= 0
#    with open('savegames.txt','r') as savegames:
#        savegame = json.load(savegames) #savegames.readline()

    #checks that the terminal is big enough for the game
#    if maxx < list_w+4:
#        print(f"ERROR: Terminal size too small.  Please ensure terminal is at least {list_w+4} wide and {list_h+5} high.  Terminal is currently {maxx} x {maxy}.  Thank you.")
#        exit()
#    elif maxy < list_h+5: 
#        print(f"ERROR: Terminal size too small.  Please ensure terminal is at least {list_w+4} wide and {list_h+5} high.  Terminal is currently {maxx} x {maxy}.  Thank you.")
#        exit()
        

    while True:
        clear()

        while True:
            clear()
            displaymap()
            temp= round(((maxx-len(MapLoc))/2))
            action = input("What would you like to do? \n>")
            if action in ["w","a","s","d"]:
                MapLoc= makemove(action)
                if data['player']['stats']['hp'][0] < data['player']['stats']['hp'][1]:
                    data['player']['stats']['hp'][0] +=1
                clear()
                displaymap()
                if randint(1,1) == 1:
                    combat()
            elif action in ["c","m"]:
                pmenu()
            elif action == "q":
                exit()
            else:
                continue

main()
