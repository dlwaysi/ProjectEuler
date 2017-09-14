#Project Euler
#Problem # 1
#Task: Calculate the sum of all of the multiples of 3 and 5 below 1000
#Author: Daniel Lwaysi
#Note: This is a simple test script to test the different solutions found in the module "M35.py"
#Date: 9/11/2017

import sys
import M35


def main(argv):
	print "FIRST SOLUTION:"
	M35.one(1000)
	print "SECOND SOLUTION:"
	M35.two(1000)
	print "THIRD SOLUTION:"
	M35.three(1000)
	print "FOURTH SOLUTION:"
	M35.four(1000)
	pass


#STATEMENT TO DIRECT SCRIPT TO main() FUNCTION
if __name__ == "__main__":
	main(sys.argv)







