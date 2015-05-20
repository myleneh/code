#!/usr/local/bin/python3
"""This program loops over a tuple and pritns out the results of multiplying two numbers together.
This assumes no input greater than 99 or lesser than -99."""

multipliers = ((1,1), (2,2), (12, 13), (4, 4), (13, 14), (99, 98), (99, -99), (-99, 99), (-99, -99))

for num1, num2 in multipliers:
    product = num1 * num2
    print ("{0:>5d} = {1:>3d} x {2:>3d}".format(product, num1, num2))