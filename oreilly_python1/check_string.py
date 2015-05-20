#!/usr/local/bin/python3
"""This program verifies that text input is in all CAPS and ends with a period."""

s = ""

#while s.isupper() != True or s.endswith(".") != True:
#    s = input("Please enter an upper-case string ending with a period: ")
#    if s.isupper() != True:
#        print("Input is not all upper case.")
#        if s.endswith (".") != True:
#            print("Input does not end with a period.")
#    elif s.endswith(".") != True:
#        print("Input does not end with a period.")
#    else:
#        print("Input meets both requirements.")
        
while s.isupper() != True or s.endswith(".") != True:
    s = input("Please enter an upper-case string ending with a period: ")
    if s.isupper() != True:
        print("Input is not all upper case.")
    if s.endswith (".") != True:
            print("Input does not end with a period.")

print("Input meets both requirements.")