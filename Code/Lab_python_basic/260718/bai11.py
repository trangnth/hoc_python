# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

m = int(input("Enter number of row: "))
n = int(input("Enter number of column: "))

arr = [[0 for col in range(n)] for row in range(m)]

for i in range(m):
	for j in range(n):
		arr[i][j] = i*j
print (arr)
