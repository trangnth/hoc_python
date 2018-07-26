f1, f2 = 0, 1

print("Day Fibonacci giua 0 va 50: ")
while (1):
	print (f1, " ", end="")
	f3 = f1 + f2
	f1 = f2
	f2 = f3
	if f1 > 50:
		break
print("")
