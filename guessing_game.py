#!/usr/bin/python3
#
#   
#
#  by:  Francis Kessie
#       
""" 
A guessing game.

This game generates and stores a random secrete integer between 1 
and 99 inclusive. The user is given the opportunity to guess this secrete 
number in 7 attempts. A correct guess will terminate the program and declare 
the user a winner. The game will terminate and display the secrete number 
after the seventh attempt"""

import random 

secrete = random.randrange(1,100)
guess = 0
count = 7

while True:
    
    guess = input("Guess a number: ")
    if not guess:
        continue
    if not guess.isdigit():
        print("Invaild input. Input is not a number")
        continue
    
    guess = int(guess)
    if guess == secrete:
        print ("You got it", "You are a genuis...", sep = "\n")
        break
    else:
        count -=1
    
    if count == 0:
        print("You missed it. The number was", secrete)
        break
        
    elif guess < secrete:
        print ("It's lower...")
        if count == 1:
            print("This is your last chance")
        else: 
            print("You have", count, "more times to try")
               
    elif guess > secrete:
        print ("It's higher...")
        if count == 1:
            print("This is your last chance")
        else: 
            print("You have", count, "more times to try")
            
         
