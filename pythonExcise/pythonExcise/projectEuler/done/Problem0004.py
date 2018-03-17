'''
Question 0004: https://projecteuler.net/problem=4

***Largest palindrome product***
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers 
is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
'''

print ("\n************* Solution 1 starts ************\n")

def isPalindrome(num): 
     return num == num[::-1]        # num[::-1] to reverse a string

largest = 0

for i in range(100, 1000):
    for j in range (100, 1000): 
        product = i * j
        if isPalindrome(str(product)): 
            if product > largest:
                largest = product
                
print (largest)

print ("\n************* Solution 1 ends ************\n")

print ("\n************* Solution 2 starts ************\n")

def getResult():
    # put everything in one line
    return max(  [i*j for i in range(100,1000) for j in range(100,1000) if str(i * j) == str(i * j)[ : : -1]]   )

print(getResult())
print ("\n************* Solution 2 ends ************\n")

