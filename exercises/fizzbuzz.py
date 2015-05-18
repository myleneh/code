#!/usr/local/bin/python3
"""
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number and 
for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

http://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/
"""

def fizzbuzz():
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output = output + "Fizz"
        if i % 5 == 0:
            output = output + "Buzz"
        if not output:
            output = "{0}".format(i)
        print(output)

if __name__ == "__main__":
    fizzbuzz()
