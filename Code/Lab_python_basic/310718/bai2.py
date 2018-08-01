# Write a Python program to read a random line from a file.

import random

def random_line(f):
	lines = open(f).read().splitlines()
	print (random.choice(lines))

random_line("bai1.py")
