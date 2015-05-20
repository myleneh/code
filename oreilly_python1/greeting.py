#
# greeting.py
#
"""This program prompts user for first and last names
and prints a greeting."""

first = input("Please enter your first name: ")
last = input("Please enter your last name: ")

# This capitalizes the first letters.
firstcap = first.capitalize()
lastcap = last.capitalize()

print("I am pleased to meet you,",firstcap,lastcap)