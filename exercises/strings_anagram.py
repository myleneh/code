#!/usr/local/bin/python3
"""
Anagrams: Write a method to decide if two strings are anagrams or not. An 
anagram is a word formed by rearranging the letters of another word, e.g., 
"iceman" is an anagram of "cinema".
"""

from sys import argv

def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    word1 = ''.join(sorted(word1))
    word2 = ''.join(sorted(word2))
    if word1 == word2:
        return(True)
    else:
        return(False)

if __name__ == "__main__":
    try:
        word1 = argv[1]
        word2 = argv[2]
    except IndexError:
        print("Please pass 2 strings as arguments.")
    else:
        if is_anagram(word1, word2):
            print("{0} and {1} are anagrams.".format(word1, word2))
        else:
            print("{0} and {1} are not anagrams.".format(word1, word2))
