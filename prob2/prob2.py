#!/usr/bin/env python3

# Project Euler 
# Problem #2
# 9/29/13
############################################################################
# By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the even-valued terms.
############################################################################

# first and second numbers of the fibonacci sequence 
num1=1
num2=2
newNum=0

# start with 2 because of we are already counting num2 (it's even) 
sum=2

# loop until you reach 4 million
while(newNum <= 4000000):
    newNum = num1 + num2

    # if even, then accumulate the sum
    if newNum%2 == 0:
        sum=sum+newNum
    # move to the next numbers 
    num1=num2
    num2=newNum

print("The sum of even numbers is %d" %(sum))
