num_count = {}
max = {}
max_length = 0
for start in range(1,1000000):
	#print("testing number: ", start)
	items = []

	num = start
	rest = 0
	items.append(num)

	while (num != 1):

		if (num%2 == 0): 
			#even
			num = (num/2)
			if(num in num_count):
				rest = num_count[num]
				#print("found: ",num)
				break; 
			else:
				items.append(int(num))
		else:
			num = ((3*num)+1)
			if(num in num_count):
				rest = num_count[num]
				#print("found: ",num)
				break; 
			else:
				items.append(int(num))

	#print("items to save:", items)
	for i in range(len(items)):
		if (max_length < len(items)-i+rest):
			max={items[i]:len(items)-i+rest}
			max_length= len(items)-i+rest
		num_count.update({items[i]:len(items)-i+rest})
	#print("number:", start, " has number of elements: ",num_count[start])
	#print("num_count as of now:",num_count)

#print(num_count)
print("maximum number and its count:",max)