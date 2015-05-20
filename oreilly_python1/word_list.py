#!/usr/local/bin/python3
"""This program reads a string from the user then prints out the words (separated by a new line) with at least one upper-case letter,
then prints out the words (separated by a new line) with no upper-case letters.
Punctuation is ignored.
"""

words_upper = [] # List that stores all words with at least one upper-case character
words_lower = [] # List that stores all words with all lower-case characters

string = input("Input your text:")

# Split the string into words
words = string.strip().split()

# For each word, test if is all lower case.  If so, append words_lower with the word.  If not, append words_upper with the word.
for word in words:
    if word.isalpha():
        if word.islower():
            words_lower.append(word)
        else:
            words_upper.append(word)
    else: #if the word has non-alpha characters 
        current_word = ""
        for i in word:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                current_word = current_word + i
        if len(current_word) > 1:
            if current_word.islower():
                words_lower.append(current_word)
            else:
                words_upper.append(current_word)

# Merge two lists so that printing can happen in 1 loop
upper_then_lower = words_upper + words_lower

# Print words_upper followed by words_lower, separated by a new line
for word in upper_then_lower:
    print(word)