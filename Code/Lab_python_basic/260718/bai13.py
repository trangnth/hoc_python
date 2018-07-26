# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010

# num = [x for x in input().split(',')]
n = input("Enter data (Sample Data : 0100,0011,1010,1001,1100,1001): ").split(',')

print ("Numbers that are divisible by 5: ")
for p in n:
	if int(p,2) % 5 == 0:
		print(p, " ", end="")
print("")



