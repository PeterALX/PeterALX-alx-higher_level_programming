#!/usr/bin/python3
"""
0-add_integer
has one function, add_integer

add_integer takes two arguments: a and b and returns their sum
usage:
>>> add_integer(50,60)
110
"""
def add_integer(a, b = 98):
    """ returns the addition of two ints """
    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer") 
    if (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer") 
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    return a + b
