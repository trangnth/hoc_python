# Write a Python program that accepts a string and calculate the number of digits and letters

str = input("Enter data: ")
digit = letter = 0

for i in str:
	if i.isdigit():
		digit +=1
	elif i.isalpha():
		letter +=1
print ("Letters:",letter, "\nDigits:",digit)
