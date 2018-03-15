'''
Question 0001: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Below provides 2 solutions. 
1. getResult give the simplest solution. 
2. solution 2 is to practice the new skills just learned on Python3. 
'''


def getResult():
    sum = 0
    for var in range(1000):
        if var % 3 == 0 or var % 5 == 0:        #either one is correct but not both
            sum = sum + var
    
    return sum
    

print ("************* Solution 1 starts ************")
print (getResult())
print ("************* Solution 1 ends ************")

print ('\n')


def getMultiples(base, limit):
    l = []
    r = limit // base    # for the integer division and ignore remainder.

    #print ("r = " + str(r))

    for num in range(r + 1):    
        currentMultiple = num * base
        if currentMultiple < 1000:        
            l.append(currentMultiple)

    return l

def sum_list(numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum



print ("************* Solution 1 starts ************")
result = 0 

multiplesOf3 = getMultiples(3, 1000)
#print (multiplesOf3)
#print(sum_list(multiplesOf3))

multiplesOf5 = getMultiples(5, 1000)
#print (multiplesOf5)
#print(sum_list(multiplesOf5))

multiplesOf15 = getMultiples(15, 1000)
#print (multiplesOf15)
#print(sum_list(multiplesOf15))

result = sum_list(multiplesOf3) + sum_list(multiplesOf5) - sum_list(multiplesOf15)

print (result)

print ("************* Solution 2 ends ************")

