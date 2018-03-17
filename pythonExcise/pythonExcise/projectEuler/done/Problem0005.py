'''
Question 0005: https://projecteuler.net/problem=5

***Smallest multiple***
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Answer: 232792560
'''

print ("\n************* Solution 1 starts ************\n")

# i acts as the place holder for the final result, 
# the outside loop of k is to find the current highest number that is not divisible by i, 
    # if found a k, then we need to find the smallest number j, starts from range bottom,  
    #   that we can find to satisfy condition that i * j is divisible by k, reset i*j to i, and break     

rangeBottom, rangeTop = 1, 20

i= rangeTop + 1 

for k in range(rangeBottom, rangeTop):
    if i % k > 0:       
        for j in range(rangeBottom, rangeTop):
            if (i*j) % k == 0:
                i *= j
                break
print (i)

print ("\n************* Solution 1 ends ************\n")

