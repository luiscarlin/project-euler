#!/usr/bin/env python3

# Project Euler
# Problem #1
# 9/29/13
############################################################################
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
############################################################################

import math 

def sumOfMultiples(last, factor, starting=1):
	print("Parameters: \n- Multiples of \t= %d\n- Below (inc) \t= %d\n- starting at \t= %d\n" % (factor, last, starting))
	
	lastInSeries = math.floor(last/factor)

	sum = (int)(factor*lastInSeries*(lastInSeries+1)/2)
	print ("The sum is: %d\n" %(sum))
	return sum

print (sumOfMultiples(999,3)+sumOfMultiples(999,5)-sumOfMultiples(999,15))


