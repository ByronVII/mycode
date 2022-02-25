#!/usr/bin/env python3
import csv
import random
from os import system, name

#data pulled from http://miroz.com.hr/random/monsters.csv

#disctionary to call data set headers and clean display names  ( # : [ data set header , display name ] )
attributes={1:['STR','Strength'],2:['DEX','Dexterity'],3:['CON','Constitution'],4:['INT','Intelligence'],5:['WIS','Wisdom'],6:['CHA','Charisma'],7:['HP','Hit Points'],8:['AC','Armor Class'],9:['ChallengeRating','Challenge Rating'],10:['ChallengeXP','Challenge XP'],11:['STRMod','Strength Modifier'],12:['DEXMod','Dexterity Modifier'],13:['CONMod','Constitution Modifier'],14:['INTMod','Intelligence Modifier'],15:['WISMod','Wisdom Modifier'],16:['CHAMod','Charisma Modifier'],17:['HPDice','Hit Point Dice'],18:['ACType','AC Type']}

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def namesearch(attr,attrvalue,oper):
    monlist= []
    ran= 0
    with open("/home/student/mycode/read_write/monsters.csv", "r") as monsters:
        for mon in csv.DictReader(monsters, delimiter=";"):
            #creates a list of monsters that meet the requested parameters
            ran += 1
            if oper == "ran":
                if ran == attrvalue:
                    monlist.append(mon)
                    return monlist
            if oper == "con":
                if attrvalue in mon[attr]:V
                    monlist.append(mon)
            if oper == "ex":
                if mon[attr] == attrvalue:
                    monlist.append(mon)
            if oper in ["eq", "greq", "leeq"]:
                if int(mon[attr]) == int(attrvalue):
                    monlist.append(mon)
            if oper in ["gr", "greq"]:
                if int(mon[attr]) > int(attrvalue):
                    monlist.append(mon)
            if oper in ["le", "leeq"]:
                if int(mon[attr]) < int(attrvalue):
                    monlist.append(mon)
        return monlist
    

def printnames(monlist):        #Prints just the names of monsters in the supplied list
    for mon in monlist:
        print(mon["Name"])

def printfull(monlist):         #prints full stats of monsters in the supplied list
    y=0
    for x in monlist:
        #adds a plus sign to stat mods that are not negative
        if int(monlist[y]['STRMod']) >= 0:
            monlist[y]['STRMod'] = "+" + monlist[y]['STRMod']
        if int(monlist[y]['DEXMod']) >= 0:
            monlist[y]['DEXMod'] = "+" + monlist[y]['DEXMod']
        if int(monlist[y]['CONMod']) >= 0:
            monlist[y]['CONMod'] = "+" + monlist[y]['CONMod']
        if int(monlist[y]['INTMod']) >= 0:
            monlist[y]['INTMod'] = "+" + monlist[y]['INTMod']
        if int(monlist[y]['WISMod']) >= 0:
            monlist[y]['WISMod'] = "+" + monlist[y]['WISMod']
        if int(monlist[y]['CHAMod']) >= 0:
            monlist[y]['CHAMod'] = "+" + monlist[y]['CHAMod']
        
        #adds a space to single digit numbers
        if int(monlist[y]['STR']) < 10:
            monlist[y]['STR'] = " " + monlist[y]['STR']
        if int(monlist[y]['DEX']) < 10:
            monlist[y]['DEX'] = " " + monlist[y]['DEX']
        if int(monlist[y]['CON']) < 10:
            monlist[y]['CON'] = " " + monlist[y]['CON']
        if int(monlist[y]['INT']) < 10:
            monlist[y]['INT'] = " " + monlist[y]['INT']
        if int(monlist[y]['WIS']) < 10:
            monlist[y]['WIS'] = " " + monlist[y]['WIS']
        if int(monlist[y]['CHA']) < 10:
            monlist[y]['CHA'] = " " + monlist[y]['CHA']

        #prints out each stat.  shows type of AC if there is one and shows the stat modifier after stats    
        print()
        print(f'Name: {monlist[y]["Name"]}')
        print(f"HP: : {monlist[y]['HP']}")
        if monlist[y]['ACType'] == "":
            print(f"AC: {monlist[y]['AC']}")
        else:
            print(f"AC: {monlist[y]['AC']}  Type: ({monlist[y]['ACType']})")
        print(f"STR: {monlist[y]['STR']} ({monlist[y]['STRMod']})")
        print(f"DEX: {monlist[y]['DEX']} ({monlist[y]['DEXMod']})")
        print(f"CON: {monlist[y]['CON']} ({monlist[y]['CONMod']})")
        print(f"INT: {monlist[y]['INT']} ({monlist[y]['INTMod']})")
        print(f"WIS: {monlist[y]['WIS']} ({monlist[y]['WISMod']})")
        print(f"CHA: {monlist[y]['CHA']} ({monlist[y]['CHAMod']})")
#        print(f"Strength: {monlist[y]['STR']} ({monlist[y]['STRMod']})")
#        print(f"Dexterity: {monlist[y]['DEX']} ({monlist[y]['DEXMod']})")
#        print(f"Constitution: {monlist[y]['CON']} ({monlist[y]['CONMod']})")
#        print(f"Intelligence: {monlist[y]['INT']} ({monlist[y]['INTMod']})")
#        print(f"Wisdom: {monlist[y]['WIS']} ({monlist[y]['WISMod']})")
#        print(f"Charisma: {monlist[y]['CHA']} ({monlist[y]['CHAMod']})")
        print(f"Challenge Rating: {monlist[y]['ChallengeRating']}")
        print(f"Challenge XP: {monlist[y]['ChallengeXP']}")
        y += 1

def main():
    clear()
    print('\033[95m' + '\033[1m' + "Welcome to the Monster Database!" + '\033[0m')
    while True:
        menu1 = input("How would you like to search the DB by (n)ame, (a)ttribute, or (r)andom?  ").lower()        #search by name or attribute
        if menu1 in ["name","n","attribute","a","r","random"]:
            break
        elif menu1 in ["q","quit"]:
            exit()
        else:
            print()
            print("Please enter either (n)ame or (a)ttribute to continue.  Or q to quit.")
            continue

    if menu1 in ["name", "n"]:      #subcommands for searching by name
        clear()
        name= input("Which monster would you like information about? \n").capitalize()
        attr= "Name"
        print("\n 1- Exact Name \n 2- Contains \n")
        oper= input()
        if oper == "1":
            oper = "ex"
        else:
            oper = "con"
        monlist= namesearch(attr,name,oper)
        if monlist == []:
            print("No creatures match that search.")
        else:
            clear()
            print(f"Creatures whose name contain {name} are:")
        nameorfull = input("Would you like to see just the names of the monsters or their full info? \n 1- names \n 2- full \n")
        clear()
        if nameorfull == "1":            
            print("Creatures whose name contain {name} are:")
            printnames(monlist)
        else:
            print("Creatures whose name contain {name} are:")
            printfull(monlist)

    elif menu1 in ["attribute","a"]:        #subcommands for searching by attribute
        clear()
        print("Which attribute do you want to search for?  (enter number)")
        for x in attributes:
            print(f" {x}- {attributes[int(x)][1]}")
            x += 1
        attribute= int(input("\n"))
        print()
        attrvalue= input("What value are you searching for? \n")
        print(f"Do you want to see monsters whose {attributes[attribute][1]} is ___________  {attrvalue}? \n 1- equal to \n 2- greater than \n 3- less than \n 4- greater than or equal to \n 5- less than or equal to \n")
        oper= input()
        #sets up which types of operations will be performed creates the response to be printed before the results are displayed
        if oper == "1":
            oper = "eq"
            resp = f"Creatures with {attributes[int(attribute)][1]} of {attrvalue} are:"
        elif oper == "2":
            oper = "gr"
            resp = f"Creatures with {attributes[int(attribute)][1]} greater than {attrvalue} are:"
        elif oper == "3":
            oper = "le"
            resp = f"Creatures with {attributes[int(attribute)][1]} less than {attrvalue} are:"
        elif oper == "4":
            oper = "greq"
            resp = f"Creatures with {attributes[int(attribute)][1]} greater than or equal {attrvalue} are:"
        elif oper == "5":
            oper = "leeq"
            resp = f"Creatures with {attributes[int(attribute)][1]} less than or equal to {attrvalue} are:"
        else:
            print("Invalid input.  Please start over.")
            main()

        attr= attributes[int(attribute)][0]         #sets attribute to its format in the data set (i.e. 1- Strength is STR in the data set
        monlist= namesearch(attr,attrvalue,oper)
        if monlist == []:
            print("No creatures match that search.")
        else:
            nameorfull = input("Would you like to see just the names of the monsters or their full info? \n 1- names \n 2- full \n")
            if nameorfull == "1":
                clear()
                print(resp)
                printnames(monlist)
            else:
                clear()
                print(resp)
                printfull(monlist)

    elif menu1 in ["r", "random"]:
        ran= random.randint(1,159)
        oper= "ran"
        monlist= namesearch(0,ran,oper)
        printfull(monlist)
        

    print()
    cont= input("Would you like look up any other monster information?  ").lower()
    if cont in ["yes","y", "yep","yeah"]:
        main()
    else:
        exit()
    
main()

