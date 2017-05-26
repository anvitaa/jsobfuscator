import re
import sys
import random


global seed 

seed = random.randint(0,500)
global jsarray 
jsarray= ""

variables = {}
def replace_variables (code):
	
	# variables contains the names of all the 
	# variables that have been assigned values in the code
	
	for var in re.finditer(r"([\$\w]+)\s*(=|\()", code):
		global variables 
		variables[var.group(1)] = random_name_generator()
	print variables
	newCode = code
	for var in variables:
		newCode = re.sub( r'(\s+)'+r'('+re.escape(var)+r')'+r'(\s*|\.|\()', r'\1'+variables[var]+r'\3', newCode)
	return newCode	
	

def random_name_generator ():
	global seed
	seed = seed + 1
	return '_'+hex(seed)