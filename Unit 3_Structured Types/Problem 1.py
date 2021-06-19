#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 22:07:29 2021

@author: teng
"""

secretWord = 'rsssssi'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...    
    return set(secretWord) - set(lettersGuessed) == set()
        
print(isWordGuessed(secretWord, lettersGuessed))