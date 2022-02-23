#!/usr/bin/env python3
import random
from time import sleep as sleep

# import only system from os
from os import system, name

#set variables
plife = 25      #players starting life
patk = 4        #players attack value
glife = 20      #goblins starting life
gatk = 3        #goblins attack rating
dmg = 0         #damage
atkvar = [-2,-1,-1,0,0,0,0,1,1,2]       #damage variability

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
def fight():
    while plife > 0 and glife > 0:
        print()
        dmg = patk + random.choice(atkvar)      #calculates players damage for this round
        glife -= dmg                            #applies damge to goblins life total
        print(f"You hit the goblin for {dmg} damage.  It is down to {glife} life remaining.")
        dmg = gatk + random.choice(atkvar)      #calculates goblins damage for this round
        plife -= dmg                            #applies damge to players life total
        print(f"The goblin hit you for {dmg} damage.  You are down to {plife} life remaining.")
        sleep(1)
    return plife

#fight results
def results():
    if plife < 1 and glife < 1:
        print("You managed to slay the goblin, however, your own injuries are too grevious and you too succumb to death.")
        sleep(1)
        print("How embarassing.")
    elif plife < 1:
        print("You have died...")
        sleep(1)
        print("Seriously...")
        sleep(1)
        print("You couldn't defeat a single goblin?")
        sleep(1)
        print("You're parents are very dissapointed in you...")
        sleep(2)
        print("...but more importantly.  So am I...")
    else:
        print("You managed to slay a goblin!  Are you proud of yourself?  You really shouldn't be.")
    return plife

#first choice 
def main():
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
        fight()
        results()

if __name__ == "__main__": main()

