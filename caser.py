#!/usr/bin/python3
#
# caser.py
#
# by: Francis Kessie
#     
#
"""
A text processor.

The program ask user to select an option from what they 
would like to do with the text input.  Afterwards the user is prompted 
to enter a text string. The selected action is performed on the user's
input string and printed to screen
"""

import sys

def capitalize(inp1):
    """
    accepts a string parameter and applies 
    the capitalize() method
    """
    print(inp1.capitalize())
           
def title(inp2):
    """
    accepts a string parameter and applies 
    the title() method.
    """  
    print(inp2.title())
            
def upper(inp3):
    """"
    accepts a string parameter and applies 
    the upper() method. 
    """
    print(inp3.upper())
    
def lower(inp4):
    """
    accepts a string parameter and applies 
    the lower() method.
    """
    print(inp4.lower())
    
def exit(inp5):
    """
    ends the program
    """
    print("Good bye for now!")
    sys.exit()
    
if __name__ == "__main__":

    switch = {
         "capitalize" : capitalize,
         "title" : title,
         "upper" : upper,
         "lower" : lower,
         "exit" : exit 
       }
       
    options = switch.keys()
    option = ", ".join(options) 
    prompt = 'Enter a function name ({0}): '.format(option)
    
    while True:         
        inp1 = input(prompt)
        if not inp1:
            continue
        if inp1 in options:
            inp2 = input("Enter a String: ")                             
            switch[inp1](inp2) 
            break
        else:
            print("invalid input")
            print()
            continue  
    
