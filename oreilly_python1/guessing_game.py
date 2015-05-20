#!/usr/local/bin/python3
"""This program generates a random number between 1 and 99.  
When the user guesses the number, the program provides hints whether the guess is too high or too low.
"""
import random

random_number = random.randint(1,99)
guess = 0
while guess != random_number:
    guess = int(input("Guess a number: "))
    if guess < random_number:
        print("Too low")
        continue
    elif guess > random_number:
        print("Too high")
        continue
print("You guessed it!")