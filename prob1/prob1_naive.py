#!/usr/bin/env python3

# Project Euler
# Problem #1
# 9/29/13
############################################################################
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
############################################################################

# this variable will accumulate the sum of the multiples of 3 or 5 or both
sum = 0

# loop through values from 1 to 999
for num in range(1, 1000):
    # check if the number is multiple of 3 or 5 
    if ((num % 3 == 0) or (num % 5 == 0)):
        # same as sum = sum + num => It accumulates values
        sum +=num; 
        # print the number
        print(num)
# print the sum 
print(sum)
