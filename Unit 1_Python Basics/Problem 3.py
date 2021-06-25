#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 02:18:29 2021

@author: teng
"""

"""
Write a program that prints the longest substring of s
in which the letters occur in alphabetical order.
"""

s = "abcdefghijcbobobegghaklaz" # given example

answer = s[0]  # start guess with first letter
elong_index = 0  # this variable is used to exclude repeated check on tested str

for startpoint in range(len(s)-1):  # check each potential start point from 1st through -2nd char
    
    trantient_answer = s[startpoint]  # set a trantient answer to be elongated
    
    if startpoint >= elong_index:  # this step excludes repeated check on tested str, so shorten running time
        
        for elong_index in range(startpoint+1, len(s)):  # elongate trantient_answer with continuously ascending alphabets
            if s[elong_index] >= s[elong_index-1]:
                trantient_answer += s[elong_index]
            else:
                break
        
    if len(trantient_answer) > len(answer):  # replace answer with longer trantient_answer
        answer = trantient_answer


print("Longest substring in alphabetical order is: " + str(answer))