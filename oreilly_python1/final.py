#!/usr/local/bin/python3

"""
This program takes a filename as input and displays the count for each word length, ignoring punctuation and non-alphanumeric characters.
"""

import re, sys

word_table = {}

with open(sys.argv[1]) as f:
    for line in f:
        for word in line.split():
            stripped = re.sub("[^a-zA-Z ]", "", word)
            length = len(stripped)
            if length in word_table.keys():
                word_table[length] += 1
            else:
                if length > 0:
                    word_table[length] = 1
                
print("Length  Count")
for key in word_table:
    print("{0}   {1}".format(key, word_table[key]))
            
            
            
