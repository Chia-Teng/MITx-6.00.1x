#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 23:18:37 2021

@author: teng
"""

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    return "".join(l for l in "abcdefghijklmnopqrstuvwxyz"
                   if l not in lettersGuessed)

print(getAvailableLetters(lettersGuessed))