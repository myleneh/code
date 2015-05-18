#!/usr/local/bin/python3
"""
Pig Latin: Write a method that takes in a string and returns the pig latin 
equivalent. Pig Latin takes the first consonant, moves it to the end of the 
word and places "ay" at the end. If the string starts with a vowel do nothing. 
Examples: "pig" = "igpay" 
"banana" = "ananabay".
"""

from sys import argv

def pig_latin(word):
    out_word = word
    if not word[0] in ['a', 'e', 'i', 'o', 'u']:
        out_word = "{0}{1}{2}".format(word[1:], word[0], 'ay')
    return(out_word)

if __name__ == "__main__":
    try:
        word = argv[1]
    except IndexError:
        print("No input word was given.")
    else:
        print(pig_latin(word))
