'''
Question 0006: https://projecteuler.net/problem=6

***Sum square difference***
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer: 25164150
'''

import time
start_time = time.time()

print ("\n************* Solution 1 starts ************\n")

r = range(1, 101)  
addF = pow(sum(r), 2)
# OR use following line to calculate the square
# addF = sum(r)** 2
diff = (addF - sum(i * i for i in r))  

print(diff)

print ("\n************* Solution 1 ends ************\n")

elapsed_time = time.time() - start_time
print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))