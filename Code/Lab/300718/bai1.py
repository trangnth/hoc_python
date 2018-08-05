# Function
# Write a Python program to calculate the length of a string.

def string_length(str):
	count = 0
	for c in str:
		count += 1
	return count

print("Do dai chuoi:", string_length("My name is Trang"))