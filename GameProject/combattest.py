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
    monsters= {"goblin":{"name":"goblin","life":20, "attack":3}}
    atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability
    stats= {"player":player, "monsters":monsters}
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
    mname= stats["monsters"]["goblin"]["name"]
    mlife= stats["monsters"]["goblin"]["life"]
    matk= stats["monsters"]["goblin"]["attack"]
    atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability
    dmg= 0

    while plife > 0 and mlife > 0:
        print()
        dmg = patk + random.choice(atkvar)      #calculates players damage for this round
        mlife -= dmg                            #applies damge to goblins life total
        print(f"You hit the {mname} for {dmg} damage.  It is down to {mlife} life remaining.")
        dmg = matk + random.choice(atkvar)      #calculates goblins damage for this round
        plife -= dmg                            #applies damge to players life total
        print(f"The {mname} hit you for {dmg} damage.  You are down to {plife} life remaining.")
        sleep(1)
    return [plife,mlife,mname]
        

#fight results
def results(result):
    if result[0] < 1 and result[1] < 1:         #both player and creature died
        print(f"You managed to slay the {result[2]}, however, your own injuries are too grevious and you too succumb to death.")
        sleep(1)
        print("How embarassing.")
    elif result[0] < 1:         #only the player died
        print("You have died...")
        sleep(1)
        print("Seriously...")
        sleep(1)
        print(f"You couldn't defeat a single {result[2]}?")
        sleep(1)
        print("You're parents are very dissapointed in you...")
        sleep(2)
        print("...but more importantly.  So am I...")
    else:               #only goblin dies
        print(f"You managed to slay a {result[2]}!  Are you proud of yourself?  You really shouldn't be.")
    

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

