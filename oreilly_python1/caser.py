#!/usr/local/bin/python3
"""This program takes input from the user on the case method to be applied to another input of text.
The options are:
capitalize
title
upper
lower
exit
"""

import sys

def capitalize_text(text_input):
    """Prints the user's input in capitalized format."""
    print(text_input.capitalize())
    
def title_text(text_input):
    """Prints the user's input in title format."""
    print(text_input.title())
    
def upper_text(text_input):
    """Prints the user's input in upper format."""
    print(text_input.upper())
    
def lower_text(text_input):
    """Prints the user's input in lower format."""
    print(text_input.lower())
    
def exit_program(text_input):
    """Terminates the program"""
    print('Goodbye for now!')
    sys.exit()

if __name__ == "__main__":
    switch = {
              'capitalize': capitalize_text,
              'title': title_text,
              'lower': lower_text,
              'upper': upper_text,
              'exit': exit_program
              }
        
    options = switch.keys()
    prompt = 'Enter a function name: ({0}): '.format(', '.join(options))
    
    while True:
        input_option = input(prompt)
        input_text = input('Enter a string: ')
        option = switch.get(input_option, None)
        if option:
            option(input_text)
        else:
            print('Select a valid function.')
        