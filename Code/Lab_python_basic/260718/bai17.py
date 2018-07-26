#  Write a Python program to print alphabet pattern 'A'. Go to the editor
#Expected Output:

#  ***                                                                   
# *   *                                                                  
# *   *                                                                  
# *****                                                                  
# *   *                                                                  
# *   *                                                                  
# *   *

for row in range(0,7):
	for col in range(0,6):
		if (((col == 1 or col == 5) and row != 0) or ((row == 0 or row == 3) and (col > 1 and col < 5))):
			print("*", end="")
		else:
			print (" ", end="")
	print("")
