#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 22:42:09 2021

@author: teng
"""

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):

    return "".join(l if l in lettersGuessed
                     else "_"
                   for l in secretWord)

print(getGuessedWord(secretWord, lettersGuessed))