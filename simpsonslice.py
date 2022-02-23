#!/usr/bin/env python3
# """Morning Slicing Challenge!"""

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def main():
  #  """write your code in this function to solve the challenge"""

    # write one print function for each list above
    # get the strings "eyes," "goggles," and "nothing from each
    # final output for each print should look like this:
   # """My eyes! The goggles do nothing!"""

        print(f"My {challenge[2][1]}!  The {challenge[2][0]} do {challenge[3]}!")
        print(f"My {trial[2]['goggles']}!  The {trial[2]['eyes']} do {trial[3]}!")
        print(f"My {nightmare[0]['user']['name']['first']}!  The {nightmare[0]['kumquat']} do {nightmare[0]['d']}!")

if __name__ == "__main__": # <-- what is this??? we will review later :)
    main()
