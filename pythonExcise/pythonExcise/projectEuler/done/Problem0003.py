'''
Question 0003: https://projecteuler.net/problem=3

***Largest prime factor***
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

from functools import reduce

print ("\n************* Solution 1 starts ************\n")

ORIG_NUMBER = 600851475143

def factors(n):    
    # please see description here: "htt ps://docs.python.org/3/library/functools.html "
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))

facs = sorted(factors(ORIG_NUMBER))

#print(facs)
facs.reverse()
#print(facs)

for num in facs:
    if (num != ORIG_NUMBER and num !=1):    # facs contains 1 and ORIG_NUMBER, so need to ignore them. 
        fs = factors(num)                   # get the factors list of num
        if len(fs)==2:                      # if the factor num has only 2 factors, 1 and itself, then num is the biggest factor. 
            print(num)
            break

print ("\n************* Solution 1 ends ************\n")



