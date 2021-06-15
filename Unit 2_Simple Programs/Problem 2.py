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
    
    remain = balance # so remain reset to balance each run
    for i in range(0,12): # 12 times
        remain = (remain - guess) * (1 + annualInterestRate/12)
    # This section calculates balance remained after 12 mon
        
    if remain <= 0:
        break
    else:
        guess += 10
    # add $10 to guess until able to repay balance
    
print("Lowest Payment: ", str(guess))