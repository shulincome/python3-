from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda suck at this.",
            "Nice job,you died ...jackass",
            "Such a luser.",
            "I have a small puppy that's better at this."]
    print(quips[randint(0,len(quips)-1)])
    exit(1)


def central_corridor():
    print("The Gothon of Plant Percal #25 have invaded you ship and destroyed")
    
    print("your entire crew. You are the last surviving member and your last")
    print("mission is to get the neutron destruct bomb from the Weapons Armory,")
    print("put it in the bridge, and blow the ship up after getting into an ")
    print("escape pod.")
    print("\n")
    
