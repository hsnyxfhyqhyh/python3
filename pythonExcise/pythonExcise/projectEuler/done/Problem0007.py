'''
Question 0006: https://projecteuler.net/problem=7

***10001 st prime number***
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Answer: 104743
'''
from functools import reduce

import time
start_time = time.time()

print ("\n************* Solution 1 starts ************\n")
def factors(n):    
    # please see description here: "htt ps://docs.python.org/3/library/functools.html "
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))

i = 2
primes = []

while 1: 
    if len(factors(i)) == 2:
        primes.append(i)
        i += 1
        if (len(primes) == 10001):
            break
    else: 
        #print(i)
        i +=1
        

print (max(primes))

print ("\n************* Solution 1 ends ************\n")

elapsed_time = time.time() - start_time
print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))