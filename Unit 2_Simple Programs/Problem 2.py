#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:28:59 2021

@author: teng
"""

# Test Case 1:
balance = 4773
annualInterestRate = 0.2

guess = int(balance/120) * 10 # start with balance/12mon, with a multiple of $10

while guess < balance: 
    
    temp_balance = balance # set a temperary balance to be reset each run
    
    # calculate balance remained after 12 mon
    for i in range(0,12):
        temp_balance = (temp_balance - guess) * (1 + annualInterestRate/12)

    # add $10 to guess until it can clear the balance
    if temp_balance <= 0:
        break
    else:
        guess += 10
    
print("Lowest Payment: ", str(guess))