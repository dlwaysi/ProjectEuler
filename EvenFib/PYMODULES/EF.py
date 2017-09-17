#Project Euler
#Problem # 2
#Task: Calculate the sum of all of the even terms in the Fibonacci sequence up to the number 4000000
#Author: Daniel Lwaysi
#Note: This is my PYMODULE for the Even Fibonacci tast
#Date: 9/16/2017

def one():
        fib = []
        fib.append(1)
        fib.append(2)

        efib = [2]
        for n in range(2,1000):
                fib.append(fib[n-1] + fib[n-2])
                if fib[n]%2 == 0 and fib[n] <= 4000000:
                        efib.append(fib[n])
                efsum = sum(efib)

        print "EVEN FIBONACCI SUM = ",efsum, "efib array = ",efib


def two():
        odd,even = 1,2
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

        print "EVEN FIBONACCI SUM = ",sum

