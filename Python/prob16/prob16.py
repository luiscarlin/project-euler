#!/usr/bin/env python


#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 21000?


import math 

debug = False

num = long(math.pow(2, 1000))

sum = 0

while(num):
	if debug : print("debug: num=" + str(num) + "\ndebug: sum=" + str(sum)) 
	sum = sum + (num % 10)
	num = num/10

print("Sum of the digits of 2^10000 = " + str(sum))