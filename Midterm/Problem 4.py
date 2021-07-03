#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:36:25 2021

@author: teng
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    
    L.reverse()  # reverse order of L
    for index in range(len(L)):  # reverse each items in L
        L[index].reverse()