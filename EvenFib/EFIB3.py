#Project Euler
#Problem # 2
#Task: Calculate the sum of the even-valued terms in the Fibonaci sequence up to 4 million
#Author: Daniel Lwaysi
#Note: This is my third solution, MEMOIZATION TECHNIQUE
#Date: 9/25/2017

def memoize(f):

	memo = {}
	def helper(x):
		if x not in memo:
			memo[x] = f(x)
		return memo[x]
	return helper

def fib(n):

	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

fib = memoize(fib)


print(fib(4)) 


