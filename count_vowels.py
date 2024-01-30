#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:39:35 2024

@author: thaisfreire
"""

# Write a function to count the number of vowels in a given string

def count_vowels():
  vowels = 'aeiouAEIOU'
  count = 0
  
  for i in str:
    if i in vowels:
      count += 1
  
  print(f'{str} has {count} vowels')

str = input('Enter a string- ')
count_vowels()