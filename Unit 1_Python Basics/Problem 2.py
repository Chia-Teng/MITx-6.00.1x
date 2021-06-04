#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:19:50 2021

@author: teng
"""

# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl',
# then your program should print
# Number of times bob occurs is: 2

s = 'azcbobobegghakl' # example given

count = 0 # define start point

for char in range(len(s)-2): # len(s)-2, so test ends at -3rd char

    if s[char] == "b" and s[char+1] == "o" and s[char+2] == "b": # test if start with "b" followed by "o" then "b"
        count += 1 # count + 1 if true

print("Number of times bob occurs is: " + str(count))