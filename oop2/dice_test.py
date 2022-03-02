#!/usr/bin/python3

# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Cheat_Mulligans

def main():
    draw=0
    win1=0
    win2=0

    # create two cheater objects
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Mulligans() # increase all rolls by +1 provided they are < 6 
    x=1000000
    for i in range(x):
        # both players take turns
        cheater1.roll() 
        cheater2.roll()

        # both players use their cheat methods
        cheater1.cheat()
        cheater2.cheat()

    #    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    #    print(f"Cheater 2 rolled {cheater2.get_dice()}")

        if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
            draw += 1
    #        print("Draw!")
            
        elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
            win1 += 1
    #        print("Cheater 1 wins!")

        else:
            win2 += 1
    #        print("Cheater 2 wins!")i
    print(f"Player1 won {win1} ({win1/x*100}%) times.\nPlayer2 won {win2} ({win2/x*100}%) times.\nThey tied {draw} ({draw/x*100}%) times.")

if __name__ == "__main__":
    main()
 
