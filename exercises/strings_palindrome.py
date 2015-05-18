#!/usr/local/bin/python3
"""
Palindrome: Determine if a given string is a palindrome. A palindrome is a 
string that is the same forwards as backwards. For example, "abccba" and 
"racecar" are palindromes, "abcd" is not.
"""

from sys import argv

def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return(True)
    else:
        return(False)

if __name__ == "__main__":
    try:
        word = argv[1]
    except IndexError:
        print("No input word was given.")
    else:
        if is_palindrome(word):
            print("{0} is a palindrome.".format(word))
        else:
            print("{0} is not a palindrome.".format(word))
