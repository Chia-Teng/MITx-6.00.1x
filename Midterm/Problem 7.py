#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 00:17:05 2021

@author: teng
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """

    filteredList = []
    for integer in L:
        if g(f(integer)):
            filteredList.append(integer)
    
    L[:] = filteredList
    
    if filteredList == []:
        return -1
    else:
        return max(filteredList)

def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, 1,2,3,4,5,6,7,8,9]
print(applyF_filterG(L, f, g))
print(L)