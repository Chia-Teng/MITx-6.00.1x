#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:12:49 2021

@author: teng
"""

"""
Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
"""
    
s = 'azcbobobegghakl' # example given

count = 0 # define start point

for char in s: # check each char in s

    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u": 
        count += 1
    # count + 1 each vowel counted

print("Number of vowels: " + str(count))