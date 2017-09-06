#Project Euler
#Problem # 1
#Task: Calculate the sum of all of the multiples of 3 and 5 below 1000
#Author: Daniel Lwaysi
#Note: This is my first solution
#Date: 7/6/2017

#Program Header
print 'This program will sum all multiples of 3 and 5,up to but not including, a number you specify'
#USER PROMPT INPUT
x          =int(raw_input('Give me a number: '))

ans        = True
threes     = []
fives      = []
commons    = []
threesome  = 0
fivesome   = 0
commonsome = 0

while ans:

	for i in range(1,x):
	
		y = i%3
		w = i%5
		if y == 0 and w != 0:
			#THIS LINE HAS BEEN COMMENTED FOR SHELL SATURATION: print(i, "\tThrees")
			threes.append(i)
			threesome += i
		elif w == 0 and y != 0:
			#THIS LINE HAS BEEN COMMENTED FOR SHELL SATURATION: print(i, "\tFives")
			fives.append(i)
			fivesome += i
		elif w == 0 and y == 0:
			#THIS LINE HAS BEEN COMMENTED FOR SHELL SATURATION: print(i, "\tCommon Multiples")
			commons.append(i)
			commonsome += i
	
	z = raw_input('Continue?(Y or N): ')


	if z == 'Y' or z == 'y':
		ans = True
		#print("Threes\t", threes)
		#print("Fives\t", fives)
		#print("Common Multiples\t", commons)
		print("Threesome = ", threesome)
		print("Fivesome = ", fivesome)
		print("Commonsome = ", commonsome)
		print("Eightsome = ", threesome + fivesome + commonsome)
		threes     = []
		threesome  = 0
		fives      = []
		fivesome   = 0
		commons    = []
		commonsome = 0
		x = int(raw_input('Give me a number: '))
	else:
		ans = False

	
	
