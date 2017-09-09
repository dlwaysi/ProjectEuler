#Project Euler
#FUNCTION # 1
#Task: Calculate the sum of all of the multiples of 3 and 5 below 1000
#Author: Daniel Lwaysi
#Note: This is the first function definition based on my first solution
#Date: 9/7/2017

def M35001(n):

	threes     = []
	fives      = []
	commons    = []
	threesome  = 0
	fivesome   = 0
	commonsome = 0

	if( n <= 100000000):

		for i in range(1,n):
		
			y = i%3
			w = i%5
			if y == 0 and w != 0:
				#THIS LINE HAS BEEN COMMENTED TO PREVENT SHELL SATURATION: print(i, "\tThrees")
				threes.append(i)
				threesome += i
			elif w == 0 and y != 0:
				#THIS LINE HAS BEEN COMMENTED TO PREVENT SHELL SATURATION: print(i, "\tFives")
				fives.append(i)
				fivesome += i
			elif w == 0 and y == 0:
				#THIS LINE HAS BEEN COMMENTED TO PREVENT SHELL SATURATION: print(i, "\tCommon Multiples")
				commons.append(i)
				commonsome += i
	
		print "THE SUM OF ALL MULTIPLES OF 3, UP TO",n,", = ",threesome,"\n"
		print "THE SUM OF ALL MULTIPLES OF 5, UP TO",n,", = ",fivesome,"\n"
		print "THE SUM OF ALL MULTIPLES OF 15, UP TO",n,", = ",commonsome,"\n"
		print "THE SUM OF ALL THE MULTIPLES OF 3 AND 5, UP TO",n,", = ",threesome + fivesome + commonsome,"\n"
			

	if ( n > 100000000):
		
		print "THE SUM OF ALL MULTIPLES OF 3, UP TO",n,", = ","OVERFLOW","\n"
		print "THE SUM OF ALL MULTIPLES OF 5, UP TO",n,", = ","OVERFLOW","\n"
		print "THE SUM OF ALL MULTIPLES OF 15, UP TO",n,", = ","OVERFLOW","\n"
		print "THE SUM OF ALL THE MULTIPLES OF 3 AND 5, UP TO",n,", = ","OVERFLOW","\n"

	threes     = []
	threesome  = 0
	fives      = []
	fivesome   = 0
	commons    = []
	commonsome = 0

	return;


	
	
