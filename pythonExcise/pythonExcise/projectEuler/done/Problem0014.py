'''
Question 0014: https://projecteuler.net/problem=14

***Longest Collatz sequence***
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Answer: 837799


'''

import time
start_time = time.time()

print ("\n************* Solution 1 starts ************\n")
dic = {}            # look up dictionary for the pass numbers' length
num, l =0, 0        # these are the number and length temp holder for the current max 

def getNextNumber(n):
    if (n%2==0) :
        return int (n/2)
    else: 
        return 3*n+1

def getSequenceLength(n):
    orig = n

    count = 1       #initialize the count, for the number itself in the chain

    if (n==1):
        return count 
    
    while n/2!=1 :  # loop make n stop at 2, 
        n= getNextNumber(n)
        count = count + 1
        if (n< orig): 
            count = count + dic[n]  - 1
            return count

    if n/2==1 :
        count = count + 1

    return count

for i in range (1, 1000001) : 
    n = getSequenceLength(i) 
    if n> l:
        num =i
        l = n
    
    dic[i] = getSequenceLength(i) 

print (str(num) + ' - length ' + str(l))
        
print ("\n************* Solution 1 ends ************\n")

elapsed_time = time.time() - start_time
print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

'''
def getSequence(n):
    result = [n]
    if (n==1):
        return 1
    else:
        while n/2!=1 :
            n= getNextNumber(n)
            result.append(n)

        if (int(n/2)==1) :
            result.append(1)
    r = len(result)

    return r

'''