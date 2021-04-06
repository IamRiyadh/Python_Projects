#Guess the Number for Python
#Github: IamRiyadh
#December 2020

#Concepts to keep in mind: Random function, Variables, Integer, Input/Output, Print, while loops and if/else statements

import random

n = random.randint(1, 99)

guess = int(input("Enter an integer from 1 to 99: "))

while n != "guess":
  print
  if guess < n:
    print ("Guess is too low")
    guess = int(input("Enter an integer from 1 to 99: "))
  elif guess > n:
    print ("Guess is too high")
    guess = int(input("Enter an integer from 1 to 99: "))
  else:
    print ("Congrats! You guessed it!")
    break
  print