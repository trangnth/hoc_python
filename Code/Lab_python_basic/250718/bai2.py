# Write a Python program to convert temperatures to and from celsius, fahrenheit.

while(1):
	temp = input("Enter temperature (e.g: 45F, 60C): ")
	degree = int(temp[:-1])
	#print(degree)
	i = temp[-1]

	if i.upper() == "C":
		result = int(round(degree /5 *9 +32))
		o = "Celsius"
	elif i.upper() == "F":
		result = int(round(degree -32)/9 *5)
		o = "Fahrenherit"
	else:
		print ("Error!")
		continue
	print ("The temperature in ", o, " is: ", result)
	break

