#!/usr/bin/python3
#
# 
#
# by: Francis Kessie 
#     
#
"""
Input text logger.

Takes input text from user and number words in the order in which they were entered. 
Duplicate words are ignored and the numbering is only assigned to the word the
first time it is entered. The program terminates when the enter key is pressed
"""

my_set = set() 
my_dict = {}   

while True:
    
    words = input("Enter text (or press Enter to quit) : ")
    
    #quit the program and print "Finished" if the enter key is pressed
    if not words: 
        print("Finished")
        break
    
    #remove puntuations if any, and create a list of words from input text
    for symbol in ":,?;.":
        words = words.replace(symbol, "")
        wordlist = words.split() 
   
    #loop through list and add each word to the set
    for x in wordlist:
          setsize1 = len(my_set)
          my_set.add(x)
          setsize2 = len(my_set)
          if setsize1 <  setsize2:   
              my_dict[x] = len(my_set)
   
     #print all words and corresponding values
    for key, value in my_dict.items():
         print(key, value)
