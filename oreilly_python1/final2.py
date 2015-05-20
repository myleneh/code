#!/usr/local/bin/python3

"""
This program takes a filename as input and displays the count for each word length, ignoring punctuation and non-alphanumeric characters.  
Then it displays a histogram.
"""

import re, sys, math

def histogram(table):
    # Calculate ((max - min)/# of keys).  This program limits the scale to 5, 10 or 20.
    min_value = min(table.values())
    max_value = max(table.values())
    scale = ((max_value-min_value)/len(table))
    if scale < 10:
        scale = 5
    elif (scale > 10) and (scale < 15):
        scale = 10  
    else:
        scale = 20

    # Calculate the top label for the value.
    y = scale * math.ceil(max_value/scale)
    
    # Create a dict -- convert to values based on the scale.
    scaled_table = {}
    for key in table:
        scaled_table[key] = scale *(math.ceil(table[key]/scale))
    
    # Get length of the maximum value so that the y-axis can be properly formatted with leading spaces for values 
    # with less digits than the max.
    digits = len(str(y))
    
    # Start with top value, then go down by subtracting the scale each time.  As long as the value is >= y scale, then print ***.
    while y >= scale:
        print("{0}{1} -|".format(" "*((digits-len(str(y)))+1),y), end="")
        for key in scaled_table:
            if scaled_table[key] >= y:
                print("***", end="")
            else:
                print("   ", end="")
        print(""),
        y = y - scale

    # Print the y-axis.  
    print("{0}0  -+".format(" "*(digits-1)), end="")
    for key in table:
        print("-+-", end="")
    print(""),
    print("{0}   | ".format(" "*(digits)), end="")
    for key in table:
        print(" {0}".format(key), end="")
        
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
            
histogram(word_table)            
            
   
            
