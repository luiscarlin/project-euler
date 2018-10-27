infile = open('C:/Users/Luis/Dropbox/Programming/Python/Project_Euler/file.txt', 'r')

lines = []
num_lines = []
twoDlist = []

for line in infile: 
	line = line.strip('\n')

	# Separate the line into a list of strings representing the numbers 
	line_list = line.split(" ")

	for num in line_list:
		num_lines.append(int(num))

	# append the list of numbers into the 2d list 
	twoDlist.append(num_lines)
	# clear the list 
	num_lines = []

maxProduct = 0
numsMuls = ""

# vertical 
# 17 is the maximum 
for cols in range(20): 
	for rows in range (17): 
		product = twoDlist[rows+0][cols] * twoDlist[rows+1][cols]*twoDlist[rows+2][cols]*twoDlist[rows+3][cols]

		if product > maxProduct: 
			maxProduct = product
			numsMuls = str(twoDlist[rows+0][cols])+","+str(twoDlist[rows+1][cols])+","+\
			 str(twoDlist[rows+2][cols])+","+str(twoDlist[rows+3][cols])

print("vertically, the maximum product is:", maxProduct)
print("the numbers were:" +numsMuls)

maxProduct = 0
numsMuls = ""

# horizontal 
for cols in range(17): 
	for rows in range (20): 
		a = twoDlist[rows][cols+0]
		b = twoDlist[rows][cols+1]
		c = twoDlist[rows][cols+2]
		d = twoDlist[rows][cols+3]
		product = a * b *c *d

		if product > maxProduct: 
			maxProduct = product
			numsMuls = str(a)+","+str(b)+","+str(c)+","+str(d)

print("horizontally, the maximum product is:", maxProduct)
print("the numbers were:" +numsMuls)

maxProduct = 0
numsMuls = ""

# diagonally (right)
for cols in range(20): 
	for rows in range (20):
		if (cols + 3 <= 19) and (rows + 3 <= 19):  
			a = twoDlist[rows+0][cols+0]
			b = twoDlist[rows+1][cols+1]
			c = twoDlist[rows+2][cols+2]
			d = twoDlist[rows+3][cols+3]
			product = a * b *c *d

			if product > maxProduct: 
				maxProduct = product
				numsMuls = str(a)+","+str(b)+","+str(c)+","+str(d)

print("diagonnaly (to the right), the maximum product is:", maxProduct)
print("the numbers were:" +numsMuls)

maxProduct = 0
numsMuls = ""

# diagonally (left)
for cols in reversed(range(20)): 
	for rows in reversed(range (20)):
		if (cols - 3 >0) and (rows + 3 <= 19):  
			a = twoDlist[rows+0][cols-0]
			b = twoDlist[rows+1][cols-1]
			c = twoDlist[rows+2][cols-2]
			d = twoDlist[rows+3][cols-3]
			product = a * b *c *d

			if product > maxProduct: 
				maxProduct = product
				numsMuls = str(a)+","+str(b)+","+str(c)+","+str(d)

print("diagonnaly (to the right), the maximum product is:", maxProduct)
print("the numbers were:" +numsMuls)
