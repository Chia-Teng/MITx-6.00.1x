#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:07:56 2021

@author: teng
"""
# Test Case 1
# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

# Test Case 2
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(0,12): # 12 times
    balance = balance * (1 - monthlyPaymentRate) * (1 + annualInterestRate/12)    

print("Remaining balance: ", str(round(balance,2)))