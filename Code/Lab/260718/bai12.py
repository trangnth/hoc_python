#  Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case)

lines = []

print("Enter lines (blank line to terminate): ")
while 1:
	l = input()
	if l:
		lines.append(l.upper())
	else:
		break
for l in lines:
	print (l)
# print(lines)
