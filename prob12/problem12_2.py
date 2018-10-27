# problem 12_2

def triangle(index):
	triangle = (index * (index + 1)) / 2
	return triangle

def factors(n):
	count=0
	divisors = 0; 
	
	if n%2 == 0:
		n=n/2

	while n%2 == 0:
		count+=1
		n = n/2
	divisors = count +1

	div=3

	# at this point, n is no even 	
	while n!=1:
		count = 0
		while n%div == 0:
			count+=1
			n = n/div
		# a this point, n is not divisible by div 
		divisors = divisors*(count+1)

		# at this point, increase the number of divisor by 2 (STILL ODD)
		div+=2

	# At thi point, divisors should contain the number of divisors that the number n had 
	return divisors

def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = factors(n), factors(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, factors(n+1)
    return n


n = find_triangular_index(500)
print ("The %sth triangle with value T(n)=%s has 500 divisors"% (n,triangle(n)))