#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 03:58:11 2021

@author: teng
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    L_sorted = sorted(L, reverse = True)
    for i in L_sorted:
        if L_sorted.count(i) % 2 == 1:
            return i
    return None