#!/usr/bin/env python3

import math
# Project Euler 
# Problem #3
# 10/27/13
############################################################################
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
############################################################################

# find factors of a number 
# need to go up until sqrt of that number


def findFactors(num):
	factors = []
	factors.append(1)
	factors.append(num)

	for i in range(2, int(math.ceil(math.sqrt(num)))):
		if(num%i == 0): 
			# it is a factor 
			# save the number
			factors.append(i)
			# save the other factor
			factors.append(num/i)

	factors.sort()
	return factors
# number we want to find max prime factor of
num=600851475143
factors =findFactors(num)

max = 1
for i in factors:
	factors2 = []

	factors2 = findFactors(i)
	if len(factors2) == 2:
		# prime was found
		if max < factors2[1] : 
			max = factors2[1]

print("The maximum prime factor of",num, "is", max)
