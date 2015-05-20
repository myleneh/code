#!/usr/local/bin/python3
"""This program asks a user to guess a number up to 5 attempts."""

numguesses = 0
secret = 12
guess = 0

while numguesses < 5 and guess != secret:
    guess = (int(input("Guess a number:")))
    if guess < secret:
        print("Guess higher")
    elif guess > secret:
        print("Guess lower")
    numguesses += 1
    
if numguesses <= 5 and guess == secret:
    print("Correct!  Well done, the number was", secret)
else:
    print("Sorry, the number was", secret)