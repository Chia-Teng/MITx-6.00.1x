#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:28:59 2021

@author: teng
"""

#Test Case 2:
balance = 999991
annualInterestRate = 0.0000001

lower = balance / 12  # lower bound: pay without considering interest
upper = balance * (1 + annualInterestRate/12)**12 / 12  # upper bound: pay all interest accumulating in 12 mon
pay = (lower + upper) / 2  # start guessing point

while round(upper,2) - round(lower,2) >= 0.01:  # run until upper and lower are close enough to 2nd decimal

    temp_balance = balance
    
    # This block calculates balance remained after 12 mon
    for i in range(0,12):
        temp_balance = (temp_balance - pay) * (1 + annualInterestRate/12)

    # This block replaces upper/lower if pay is sufficient/insufficient
    if temp_balance <= 0:
        upper = pay
    else:
        lower = pay
        
    pay = (lower + upper) / 2 # re-calculate pay and run again

   
print("Lowest Payment: ", str(round(pay,2)))