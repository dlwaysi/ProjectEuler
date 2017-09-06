


#Project Euler
#Problem # 1
#Task: Calculate the sum of all of the multiples of 3 and 5 below 1000
#Author: Daniel Lwaysi
#Note: This is my second solution which is a shorthand version of the first solution "Mult_3_5_mod_long.py"
#Date: 9/6/2017

#Initialize Result Variable

sum = 0

for i in range(1000):
	if( i%3 == 0 or i%5 == 0):
		sum += i
print sum
