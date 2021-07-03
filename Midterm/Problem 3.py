#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:36:42 2021

@author: teng
"""

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    '''

    guess = 1
    while isMyNumber(guess) != 0:
        if isMyNumber(guess) == -1:  # increase guss if too small
            guess += 1
        else:  # decrease guss if too large
            guess -= 1
    return guess