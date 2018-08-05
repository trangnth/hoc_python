# Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

n = 50

for i in range(n+1):
	if i%3 == 0 and i%5 == 0:
		print("fizzbuzz")
	elif i%3 == 0:
		print("fizz")
	elif i%5 == 0:
		print("buzz")
	else:
		print (i)
		
