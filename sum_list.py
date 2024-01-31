#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:56:43 2024

@author: thaisfreire
"""

# Write a program to find the sum of all elements in a list.

lst = input('Enter a list of numbers separated by spaces: ').split()
numbers = []

for num in lst:
    numbers.append(int(num))

total_sum = sum(numbers)
print(f'Sum: {total_sum}')
