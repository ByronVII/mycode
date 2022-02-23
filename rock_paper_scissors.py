#!/usr/bin/env python3
import random
throw= ["rock", "paper", "scissors"]
me= random.choice(throw)
you= input("Rock, paper, scissors, shoot!: ")
if (me == "rock" and you == "scissors") or (me == "scissors" and you == "paper") or (me == "paper" and you == "rock"):
    print(f"You threw {you} and I threw {me}.  I win!")
elif (me == "rock" and you == "paper") or (me == "scissors" and you == "rock") or (me == "paper" and you == "scissors"):
    print(f"You threw {you} and I threw {me}.  You win...   :(")
else:
    print(f"You threw {you} and I threw {me}.  We tied.  :/")
