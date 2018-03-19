'''
Question 0009: https://projecteuler.net/problem=9

***Special Pythagorean triplet***
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


Answer: 31875000 ([200] [375] [425])


'''

import time
start_time = time.time()

print ("\n************* Solution 1 starts ************\n")
for a in range(1, 334):
    for b in range(a + 1, a + 1 + 334): 
        c = 1000-a-b
        if pow(a, 2) + pow (b, 2) == pow (c, 2):
            print ([a], [b], [c])
            print (a * b* c)
            break 
            

print ("\n************* Solution 1 ends ************\n")

elapsed_time = time.time() - start_time
print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))