#Dice Rolling Simulator for Python
#Github: IamRiyadh
#November 2020

#Concepts to keep in mind: Random, Integer, Print and while loops


from random import randint
repeat = True
while repeat:
    print("You rolled",randint(1,6))
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()