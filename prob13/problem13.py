from __future__ import print_function
import sys

# this will store the list of digits representing 1 number
num_1_list = []
num_2_list = []
suma = 0
carry = 0

# read the first line 

# open the file with all the numbers in it
with open('nums') as f:
	# read  one line and strip the endl
	for num in f.readline().rstrip('\n'):
		num_1_list.append(int(num))
	
	# this list contains the first 50 digit number 
	# now, rotate it 
	num_1_list = num_1_list[::-1]
	# update the number of lines read from the file
	num_lines = 1; 
	
	# Read all the following lines  ( 50 digit numbers) in the file 
	for line in f:
		num_2_list = []
		
		# read the next line and strip the endl
		for num in line.rstrip('\n'):
			num_2_list.append(int(num))
			
		# reverse the list of numbers 
		num_2_list = num_2_list[::-1]
	
		# at this point: you have 2 lists with a number each. 
		# both of them are in reverse order, so they need to be accessed from the index 0 on 
		
		# make both numbera of equal length by appending 0s to the left of the number (actually stored as right)
		for a in range(len(num_1_list)-len(num_2_list)):
			num_2_list.append(0)
			
		# sanity check 
		if (len( num_1_list) != len(num_2_list)):
			print("Error: Adding 2 numbers of different length")
			sys.exit(1)
		
		# reset the sum and the carry to 0 two start adding the two 50 digit numbers 
		carry = 0 
		suma = 0
		
		# start adding numbers starting from the least significant digit (index 0) 
		for i in range(len(num_1_list)):
			# add the numbers
			suma = num_1_list[i] + num_2_list[i] + carry
			
			# if the length of the sum is 2, then there was a carry 
			if len(str(suma)) == 2:
				# split the 2 digit number into sum to store and carry 
				carry = int(str(suma)[0])
				suma = int(str(suma)[1])
			else :
				# the sum was only 1 digit long, so reset the carry to 0
				carry = 0
			
			# sanity check
			if ((len(str(suma)) > 1) or ((len(str(carry))) > 1)):
				print("Error: The sum or the carry length is greater than 1")
				sys.exit(2);
				
			# store the sum the first 50 digit number 
			num_1_list[i] = suma
			
			# Check if you are adding the Most Significant Digits
			# if you are, then you should also store the carry in the result 
			# This is not very efficient. If could have been done outside of this loop
			
			if ((i == len(num_1_list)-1)  and (carry != 0)):
			# append the carry to the end of the result if you are adding the last digits and the carry is not 0
				num_1_list.append(carry)
				
		# done adding the numbers
		num_lines += 1 
		# move on to the next number 
	# done adding al lthe numbers (list 1 should contain the final result)

# flip the number 
num_1_list = num_1_list[::-1]

if ( num_lines != 100):
	print("Error: Not all the numbers were read"); 
	print(num_lines)
	sys.exit(3)
	
print("\nPrining the first 10 digits of the answer:")
for i in range(10): 
	print(num_1_list[i], end='')

print("\nDONE!")

# Close the file 
f.close()