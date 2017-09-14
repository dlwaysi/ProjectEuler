#Project Euler
#Problem # 1
#Task: Calculate the sum of all of the multiples of 3 and 5 below 1000
#Author: Daniel Lwaysi
#Note: This is my fourth solution which uses the Arithmetic Progression Technique
#Date: 9/7/2017

n         = 1000
multiples = (3,5,15)

nterms    = [(n-1)//c for c in multiples]
m35sums   = [d*c*(1+d)/2 for d,c in zip(nterms, multiples)]

tsum      = m35sums[0] + m35sums[1] - m35sums[2]

print(tsum)
	
