#!/usr/local/bin/python3
"""This program takes a user's input on Name and Breed of a dog, then prints a list of the dogs."""

class Dog:
    
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        
    def __str__(self):    
        return "{0}:{1}".format(self.name, self.breed)
        
if __name__ == "__main__":
    dogs = []
    while True:
        name = input('Name: ')
        if not name:
            print("Goodbye!")
            break
        breed = input('Breed: ')
        dogs.append(Dog(name, breed))
        print("DOGS")
        for i in range(len(dogs)):
            print("{0}. {1}".format(i,dogs[i]))
        print("*" * 20)