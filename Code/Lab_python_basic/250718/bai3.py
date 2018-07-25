# Write a Python program to guess a number between 1 to 9. 
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random
#target_num, guess_num = random.randint(1, 10), 0

ran = random.randint(1, 10)
x = 0
print (ran)
while ran != x:
	x = int(input('Enter a number between 1 and 10 until get it right: '))
print('Well guessed!')
