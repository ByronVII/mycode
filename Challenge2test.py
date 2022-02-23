#!/usr/bin/env python3
marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"She-Hulk":
  {"real name": "jennifer walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
             }
names= ["Starlord", "Mystique", "She-Hulk", "1", "2", "3"]
stat= ["real name", "powers", "archenemy", "1", "2", "3"]

while True:
    char_name = input("What character do you want to know about? (1-Starlord, 2-Mystique, 3-She-Hulk)?  ")
    if not char_name in names:
        print("Name not listed.  Please try again.")
        continue
    else:
        if char_name.isdigit():
            char_name= int(char_name) - 1
            char_name= names[char_name]
        break


while True:
    char_stat= input("What statistic do you want to know about? (1-real name, 2-powers, 3-archenemy)  ")
    if not char_stat in stat:
        print("Stat not in list.  Please try again.")
        continue
    else:
        if char_stat.isdigit():
            char_stat= int(char_stat) - 1
            char_stat= stat[char_stat]
        break

if char_stat == "real name":
    print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat].title()}.")
else:
    print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}.")


