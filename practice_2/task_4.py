# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""

def checkNumber(number):
    if number.isdigit():
        b = int(number)
        digits = set(number)
        return (1000 < b < 9999) and len(digits) == 4
    else:
        return False
x = int(input())
y = int(input())
z = int(input())
v = int(input())
b = x+y+z+v
print(x, '+', y, '+', z, '+', v, '=', b)