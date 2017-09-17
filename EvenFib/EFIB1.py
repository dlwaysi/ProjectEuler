#Project Euler
#Problem # 2
#Task: Calculate the sum of the even-valued terms in the Fibonaci sequence up to 4 million
#Author: Daniel Lwaysi
#Note: This is my first solution
#Date: 9/16/2017


fib = []

fib.append(1)
fib.append(2)

efib = [2]

for n in range(2, 1000):
	fib.append(fib[n-1] + fib[n-2])
	if fib[n]%2 == 0 and fib[n] <= 4000000:
		efib.append(fib[n])
	efsum = sum(efib)


print "EVEN FIBONACCI SUM = ",efsum, "efib array = ", efib




