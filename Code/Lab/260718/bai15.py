# Write a Python program to check the validity of password input by users. Go to the editor
# Validation :
#	At least 1 letter between [a-z] and 1 letter between [A-Z].
#	At least 1 number between [0-9].
#	At least 1 character from [$#@].
#	Minimum length 6 characters.
#	Maximum length 16 characters

#password = input("Enter your password: ")

_help = """Make sure your password has: 
#	At least 1 letter between [a-z] and 1 letter between [A-Z].
#       At least 1 number between [0-9].
#       At least 1 character from [$#@].
#       Minimum length 6 characters.
#       Maximum length 16 characters"""

import re

check = False 
while 1:
	password = input("Enter your password: ")
	lengh = len(password)
	if password == "--help":
		print(_help)
	elif lengh < 6:
		print("Password is too short")
		pass
	elif lengh > 16:
		print("Password is too long")
		pass
	elif not re.search("[0-9]", password):
		pass
	elif not re.search("[a-z]", password):
		pass	
	elif not re.search("[A-Z]", password):
		pass
	elif not re.search("[$#@]", password):
		pass
	else:
		print("Valid Password.")
		break
	print("A strong password isn't enough (You can enter --help).")


