#!/usr/local/bin/python3
"""
Balanced Parentheses: Write a function which checks if parentheses in a given 
expression are balanced. 

Example: (5+6)*(7+8)/(4+3) - balanced parentheses 
(4+5)*(2+(4-7) - not balanced parentheses 
(7+8)*{3-[5+6]*4} - balanced parentheses
"""

import sys
from stack import Stack

opens = "([{"
closes = ")]}"

def isBalanced(expression):
    balanced = True
    index = 0
    s = Stack()

    while index < len(expression) and balanced == True:
        item = expression[index]
        if item in opens:
            s.push(item)
        elif item in closes:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, item):
                    balanced = False
        index = index + 1
    return (balanced and s.isEmpty())

def matches(open, close):
    return opens.index(open) == closes.index(close)

if __name__ == "__main__":
    expression = sys.argv[1]
    print(isBalanced(expression))
