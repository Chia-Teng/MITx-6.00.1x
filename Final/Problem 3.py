#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 03:36:35 2021

@author: teng
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    digit_count = 0
    for i in s:
        if i.isdigit():
            digit_count += 1
    if digit_count == 0:
        raise ValueError
    s_sum = 0
    for i in s:
        try:
            s_sum += int(i)
        except:
            pass
    return s_sum