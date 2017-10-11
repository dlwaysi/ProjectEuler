#Project Euler
#Problem # 2
#Task: Calculate the sum of all even terms contained in the Fibonacci sequence up to the number 4000000
#Author: Daniel Lwaysi
#Note: This is a simple test script to test the different solutions found in the module "EF.py"
#Date: 9/16/2017

import sys
import EF


def main(argv):
	print "FIRST SOLUTION:NAIVE RECURSSIVE"
	EF.one()
	print "SECOND SOLUTION:"
	EF.two()
	pass


#STATEMENT TO DIRECT SCRIPT TO main() FUNCTION
if __name__ == "__main__":
	main(sys.argv)

