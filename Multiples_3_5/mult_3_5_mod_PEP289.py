




#Project Euler
#Problem # 1
#Task: Calculate the sum of all of the multiples of 3 and 5 below 1000
#Author: Daniel Lwaysi
#Note: This is my third solution which reduces the second solution, "Mult_3_5_mod_short.py", to one line
# using PEP 289, GENERATOR EXPRESSIONS
#Date: 9/6/2017

#The range for the Generator Expression goes to (n - 1), or 999 in this case
print(sum(n for n in range(1000) if n%3 == 0 or n%5 == 0))

