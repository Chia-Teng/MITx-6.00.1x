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

s = "azcbobobegghakl" # given example

alphabet = "abcdefghijklmnopqrstuvwxyz" # alphabetic order list
answer = s[0] # start guess with first char

for start in range(len(s)-1): # check each potential start point from 1st through -2nd char

    t_answer = s[start] # trantient answer starts with 1st char

    for rest in range(start+1,len(s)): # check each char following start point

        for abc in alphabet: # match each alphebet to current then previous char

            if abc == s[rest-1]:
                t_answer += s[rest] # if the previous char matches first, extend t_answer
                break # then stop matching rest of alphabets
            
            elif abc == s[rest]:
                break # if current char matches first,  stop matching rest of alphabets
            
        if abc != s[rest-1]:
            break # if t_answer doesn't extend, stop checking rest of s

    if len(t_answer) > len(answer):
        answer = t_answer # only keep the first longest result

print("Longest substring in alphabetical order is: " + str(answer))