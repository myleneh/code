#!/usr/local/bin/python3
"""This program reads a line of input from the user and encodes it in the following cipher:
Take each character of the string individually, 
and make the corresponding character in the output string be that whose ordinal value is 1 more than the ordinal value of the input character. 
Once the output string has been constructed in this way, the output of the program should be the reverse of the constructed output string."""

user_string = input('Message: ')
output_string = ''

for i in user_string:
    output_string = output_string + chr(ord(i)+1)

print(output_string[::-1])