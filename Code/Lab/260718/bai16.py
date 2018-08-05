# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence

numbers = []
#check = True

for i in range(100,401):
	check = True
	for j in str(i):
		if int(j) %2 !=0:
			check = False
			break
	if check == True:
		numbers.append(i)
print (numbers)
