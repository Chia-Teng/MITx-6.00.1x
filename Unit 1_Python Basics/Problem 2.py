#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:19:50 2021

@author: teng
"""

"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl',
then your program should print
Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl' # example given
target = "bob"

count = 0  # count of targets, start with 0

for s_index in range(len(s)-len(target)+1):  # check along the s, using index
                                             # range shortened so last checked str within the range
    if s[s_index:s_index+len(target)] == target:
        count += 1

print("Number of times bob occurs is: " + str(count))