#!/usr/bin/env python3     
#missing /bin

def main():
    
    words= {1: "great",
            2: "fabulous",
            3: "super"}

    while True:         #True needed to be capitalized and missing colon
        
        name= input("What is your name?\n>")        #missing quotes
        num= int(input("Pick a number between 1 and 3: "))      #changed input to integer.  numbers in list also could have been made into strings
        
        if name and num in words.keys():
            # Hi <name>! Welcome to Day 2 of Python Training!
            print(f"Hi {name.capitalize()}! Have a {words[num]} day!")      #changed to fstring
            break
        else:
            print("Come on, follow directions. Try again.")         #fixed indent
            continue                                                #fixed indent
            # the continue keyword skips over any remaining code and goes back to
            # the beginning of the while loop!


if __name__ == '__main__' : main()           
