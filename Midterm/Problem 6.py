#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:39:54 2021

@author: teng
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''

    flattenList = []  # this is a blank list to add non-list items in
    
    def extendFlattenList(bList):
        '''
        bList : a list (may with list items)
        return flattenList extended with unlisted items
        '''
        
        for subList in bList:  # check each item in bList
            if type(subList) != list:  # only add non-list items
                flattenList.append(subList)
            else:  # for list items, repeat recursion, until decomposed into non-list types
                extendFlattenList(subList)
    
        return flattenList

    return extendFlattenList(aList)

test = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(test))