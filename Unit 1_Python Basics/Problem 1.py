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
    
s = 'azcbobobegghakl'  # example given

count = 0  # count of vowels, start with 0

for s_index in range(len(s)):  # check every index in s
    if s[s_index] in "aeiou":  # check if the charater is a vowel
        count += 1

print("Number of vowels: " + str(count))