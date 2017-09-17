#Project Euler
#Problem # 2
#Task: Calculate
#Author: Daniel Lwaysi
#Note: This is my second solution
#Date: 9/16/2017

odd, even = 1,2
sum = 2

while True:
	odd1 = odd + even
	odd2 = odd1 + even
	even = odd1 + odd2
	odd = odd2
	if even <= 4000000:
		sum += even

	else:
		break

	print sum	
