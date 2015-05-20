#!/usr/local/bin/python3

"""This program asks for an input from the user and divides 10 by that number."""

def divide(a):
    try:
        return 10/int(a)
    except ValueError:
        print("Your input must be an integer")
        raise
    except ZeroDivisionError:
        print("Your input must not be zero (0)")
        raise

if __name__ == "__main__":
    print("Dividing 10 by an integer")
    while True:
        inp = input("Provide an integer: ")
        if not inp:
            print("Goodbye!")
            break
        else:
            try:
                print(divide(inp))
            except:
                continue