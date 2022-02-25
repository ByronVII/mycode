#!/usr/env python3
z= 5
for x in range(1,10):
#    print(x)
    if x < 6:
        for y in range(0,x):
            print("* ", end="")       
    print("\n")
    if x >=6:
        z -= 1
        for y in range(z,0,-1):
            print("* ", end="")
    print("\n")


