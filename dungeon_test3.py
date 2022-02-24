#!/usr/bin/env python3
import random
from time import sleep as sleep

# import only system from os
from os import system, name

# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

loading= {0:"[                    ]", 1:"[#                   ]", 2:"[##                  ]", 3:"[###                 ]", 4:"[####                ]", 5:"[#####               ]", 6:"[######              ]", 7:"[#######             ]", 8:"[########            ]", 9:"[#########           ]", 10:"[##########          ]", 11:"[###########         ]", 12:"[############        ]", 13:"[#############       ]", 14:"[##############      ]", 15:"[###############     ]", 16:"[#################   ]", 17:"[##################  ]", 18:"[################### ]", 19:"[####################]"}

for x in loading:
    clear()
    print("Loading...")
    print(loading[x])
    y= float(random.randint(0,7))
    y /= 10
    sleep(y)

#set variables
plife = 25      #players starting life
patk = 4        #players attack value
glife = 20      #goblins starting life
gatk = 3        #goblins attack rating
dmg = 0         #damage
atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability

clear()

print("You enter a dungeon.")

#first choice
while True:
    while True:
        fight= input("Youn encounter a goblin.  Do you want to 'fight' it or 'run'?  ").lower()       #encounter prompt
        if fight in ["q", "quit"]:
            break
        elif fight not in ["r", "run", "fight", "f"]:
            print("Command not valid.  Please enter a valid command.  (fight or run): ")
        else:
            break

    if fight in ["r", "run"]:           #player chose to run
        print("Coward...")
        exit()
    elif fight in ["f", "fight"]:       #player chose to fight
        print()
        print("You muster your courage and square up against the goblin.")
       

    #attack results
    while plife > 0 and glife > 0:
        print()
        hit = random.randint(1,4)
        if hit != 1:
            dmg = patk + random.choice(atkvar)      #calculates players damage for this round
            glife -= dmg                            #applies damge to goblins life total
            print(f"You hit the goblin for {dmg} damage.  It is down to {glife} life remaining.")
        else:
            print("You missed!")            #player missed
        hit = random.randint(1,4)
        if hit != 1:
            dmg = gatk + random.choice(atkvar)      #calculates goblins damage for this round
            plife -= dmg                            #applies damge to players life total
            print(f"The goblin hit you for {dmg} damage.  You are down to {plife} life remaining.")
        else:
            print("The goblin missed!")     #goblin missed
        sleep(1)

    print()

    #fight results
    if plife < 1 and glife < 1:         #both player and goblin die
        print("You managed to slay the goblin, however, your own injuries are too grevious and you too succumb to death.")
        sleep(1)
        print("How embarassing.")
        break
    elif plife < 1:         #just the player dies
        print("You have died...")
        sleep(1)
        print("Seriously...")
        sleep(1)
        print("You couldn't defeat a single goblin?")
        sleep(1)
        print("You're parents are very dissapointed in you...")
        sleep(2)
        print("...but more importantly.  So am I...")
        sleep(3)
        break
    else:           #just the goblin dies
        print("You managed to slay a goblin!  Are you proud of yourself?  You really shouldn't be.")

    cont= input("Would you like to fight another goblin? ").lower()
    if cont in ["yes", "y", "yep"]:
        clear()
        plife= 25
        glife= 20
        continue
    else:
        break
