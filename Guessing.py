#!/usr/bin/env python3
"""Number guessing game!"""

import random


def main():
    num= random.randint(1,100)
    count = 5
    
    print(f"You have {count} chances to guess the correct number.  Press q to quit.")

    while True and count > 0:
        guess= input("Guess a number between 1 and 100: ")

        count= count - 1
#        print(count)
    
        if guess.lower() == "q":
            break

        guess= int(guess)
        
        if guess > num:
            print("Too high!")
            if count > 0:
                print(f"You have {count} chances remaining.")
            else:
                print("Ha!  You are a failure!")

        elif guess < num:
            print("Too low!")
            if count > 0:
                print(f"You have {count} chances remaining.")
            else:
                print("Ha!  You are a failure!")

        else:
            print("Correct!")
            break

main()
