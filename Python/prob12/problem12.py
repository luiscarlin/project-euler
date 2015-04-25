# problem 12 
from math import sqrt

def find_triangle(num):
	return (num*(num+1)/2)

def factors(n):
	# 1 and n are automatically factors of
	# starting at 2 as we have already dealt with 1
	check=2
	
	num_div=2; 
	# calculate the square root of n and use this as the
	# limit when checking if a number is divisible as
	# factors above sqrt(n) will already be calculated as
	# the inverse of a lower factor IE. finding factors of
	# 100 only need go up to 10 (sqrt(100)=10) as factors
	# such as 25 can be found when 5 is found to be a
	# factor 100/5=25	
	rootn=sqrt(n)
	while check<=rootn:
		if n%check==0:
			num_div+=1
			if check != rootn:
				num_div+=1
		check+=1 
	return num_div

num = 0; 

while 1: 
	if  factors(find_triangle(num)) == 500:
		print(num," generated 500 divisors")
		print("It's triangle sum was", find_triangle(num))
		break
	else: 
		num+=1
		if num > 100000: 
			print("watchdog")
			print(num, " had ", factors(find_triangle(num)), " factors.")
			break