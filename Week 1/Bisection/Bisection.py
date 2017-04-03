# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

a = input('Start range :')
b = input('End range :')
tol = input('Tolerance : ')



def func(x) :
    return(x*x - 4)

c = ( a + b ) / 2


def method(a, b, tol) :
    c = (a + b) / 2.0	
    while ( b - a ) / 2.0 > tol :
        if func(c) == 0:
            return c
        elif func(a) * func(c) < 0:
            b = c
        else :
            a = c
        c = ( a + b ) / 2.0
    return c

ans = method(a, b, tol)
print ans
	
    