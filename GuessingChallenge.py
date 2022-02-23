#!/usr/bin/env python3
"""Number guessing game!"""

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

clear()  #clear the screen

import random


def main():
    num= random.randint(1,100)
    count = 5
    
    print(f"You have {count} chances to guess the correct number.  Press q to quit.")
    print()

    while True and count > 0:
        guess= input("Guess a number between 1 and 100: ")

        count= count - 1
    
        if guess.lower() == "q":
            break

        try:
            int(guess)
        except:
            print("That is not a number between 1 and 100.")
            print(f"You have {count} chances remaining.  Please try again.")
            print()
            continue
        else:
            guess= int(guess)

        if guess < 1 or guess > 100:
            print("That is not a number between 1 and 100.")
            print(f"You have {count} chances remaining.  Please try again.")
            print()
            continue

        
        if guess > num:
            print("Too high!")
            if count > 0:
                print(f"You have {count} chances remaining.")
                print()
            else:
                print("Ha!  You are a failure!")

        elif guess < num:
            print("Too low!")
            if count > 0:
                print(f"You have {count} chances remaining.")
                print()
            else:
                print("Ha!  You are a failure!")

        else:
            print("Correct!")
            break

main()
