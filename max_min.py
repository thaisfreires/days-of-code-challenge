#!/bin/bash /Users/thaisfreire/anaconda3/bin/pythonw

# -*- coding: utf-8 -*-


# Write a program to find the maximum and minimum values in a list.

def max_min(lst):
    max_num = max(lst)
    min_num = min(lst)
    return max_num, min_num

lst1 = input('Enter a list of numbers: ')
lst = lst1.split(',')
max_num, min_num = max_min(lst)

print('Maximum number- ', max_num)
print('Minimum number- ', min_num)
