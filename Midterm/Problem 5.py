#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 20:02:58 2021

@author: teng
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    
    dNew = {}  # create a new dict to avoid mutating d
    for key in d:  # assign each item of d into new dic
                   # note I refer to the values of d to be keys of dNew
        if d[key] in dNew:  # extend dNew value list, this if func prevents NameError error
            dNew[d[key]].append(key)
            dNew[d[key]].sort()
        else:  # add value to dNew key if not repeated
            dNew[d[key]] = [key]

    return dNew
    
# below for testing
d1 = {1:10, 2:20, 3:30, 4:30}   
d2 = {4:True, 2:True, 0:True}    
print (dict_invert(d1))
print (dict_invert(d2))

