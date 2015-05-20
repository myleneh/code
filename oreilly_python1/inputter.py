#!/usr/local/bin/python3
"""This program takes input from a user, saves it to a file, then prints the contents of the file."""

# Create file inputted_text.txt if it does not exist yet.
inputted_text = open('inputted_text.txt', 'a')
inputted_text.close()

# Print contents of the file if any exists.
inputted_text = open('inputted_text.txt', 'r').readlines()
if inputted_text:
    for line in inputted_text:
        print(line)

# Ask user for input, add to inputted_text.txt file, then print the contents of the file.
while True:
    user_string = input('Enter text: ')
    if user_string != '':
        inputted_text = open('inputted_text.txt', 'a')
        inputted_text.write(user_string)
        inputted_text.close()
        inputted_text = open('inputted_text.txt', 'r')
        for line in inputted_text:
            print(line)
    else:
        break