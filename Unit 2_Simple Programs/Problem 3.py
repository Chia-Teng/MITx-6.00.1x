#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:28:59 2021

@author: teng
"""

#Test Case 2:
balance = 999999999999
annualInterestRate = 0.0000001

lower = balance / 12
upper = balance * (1 + annualInterestRate/12)**12 / 12
pay = (lower + upper) / 2 # start guessing point

while upper - lower > 0.001: # run until upper and lower are close enough to 2nd decimal

    remain = balance
    for i in range(0,12):
        remain = (remain - pay) * (1 + annualInterestRate/12)
    # This section calculates balance remained after 12 mon

    if remain <= 0: # replace upper if pay is sufficient
        upper = pay
    else: # replace lower if pay is insufficient
        lower = pay
        
    pay = (lower + upper) / 2 # re-calculate pay and run again

   
print("Lowest Payment: ", str(round(pay,2)))