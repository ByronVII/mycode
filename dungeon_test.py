#!/usr/bin/env python3
import random
from time import sleep as sleep

# import only system from os
from os import system, name

#set variables
def setvars():
    #player stats
    player= {"name":"Bryan", "life":25, "attack": 4}
    #creature stats
    creatures= {"goblin":{"name":"goblin","life":20, "attack":3}}
    atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability
    stats= {"player":player, "creatures":creatures}
    return stats

#defining functions
# define our clear function 
def clear(): 
   
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
   
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#attack results
def combat(stats):
    print("Good")
    plife= stats["player"]["life"]
    patk= stats["player"]["attack"]
    cname= stats["creatures"]["goblin"]["name"]
    clife= stats["creatures"]["goblin"]["life"]
    catk= stats["creatures"]["goblin"]["attack"]
    atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability
    dmg= 0

    while plife > 0 and clife > 0:
        print()
        dmg = patk + random.choice(atkvar)      #calculates players damage for this round
        clife -= dmg                            #applies damge to goblins life total
        print(f"You hit the goblin for {dmg} damage.  It is down to {clife} life remaining.")
        dmg = catk + random.choice(atkvar)      #calculates goblins damage for this round
        plife -= dmg                            #applies damge to players life total
        print(f"The goblin hit you for {dmg} damage.  You are down to {plife} life remaining.")
        sleep(1)

#fight results
def results():
    if plife < 1 and glife < 1:         #both player and goblin died
        print("You managed to slay the goblin, however, your own injuries are too grevious and you too succumb to death.")
        sleep(1)
        print("How embarassing.")
    elif plife < 1:         #only the player died
        print("You have died...")
        sleep(1)
        print("Seriously...")
        sleep(1)
        print("You couldn't defeat a single goblin?")
        sleep(1)
        print("You're parents are very dissapointed in you...")
        sleep(2)
        print("...but more importantly.  So am I...")
    else:               #only goblin dies
        print("You managed to slay a goblin!  Are you proud of yourself?  You really shouldn't be.")
    

#first choice 
def main():
    stats= setvars()
    clear()
    print("You enter a dungeon.")
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
        print("You muster your courage and square up against the goblin.")
        result= combat(stats)
        results(result)

main()

