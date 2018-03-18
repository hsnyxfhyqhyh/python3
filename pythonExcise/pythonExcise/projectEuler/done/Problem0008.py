'''
Question 0008: https://projecteuler.net/problem=8

***Largest product in a series***
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

Answer: 23514624000

SETUP: 
create a temp file 'temp.txt' and save it to the same location of the .py file so it can be picked up. 
'''

import time
start_time = time.time()

print ("\n************* Solution 1 starts ************\n")
def loadFile(filename):
    fd = open(filename, 'rU')
    chars = []
    for line in fd:
       for c in line:
           if (c!= '\n') :                  # remove the new line symbol
                chars.append(c)
    
    digits = [int(d) for d in chars]        #convert every character in the list to integer. 
    return digits

#assuming the element of the list is integer. 
def product(list):
    p = 1
    for i in list:
        p *= int(i)
    return p

maxValue  = 0
maxList = []

digits = loadFile('temp.txt')

for i in range(0, len(digits) -13 +1):
    if product(digits[i: i+13]) > maxValue:
        maxValue = product(digits[i: i+13])
        maxList = digits[i: i+13]

print (maxValue)
print (maxList)

print ("\n************* Solution 1 ends ************\n")

print ("\n************* Solution 2 starts ************\n")
digits = loadFile('temp.txt')

l = [digits[x:x+13] for x in range(1000-13+1) if 0 not in digits[x:x+13]]
#print (l)

print ( max( [product(x) for x in l] ) )

# whole thing can be converted in one line. 
# print ( max( [product(x) for x in ([digits[x:x+13] for x in range(1000-13+1) if 0 not in digits[x:x+13]])] ) )

print ("\n************* Solution 2 ends ************\n")

elapsed_time = time.time() - start_time
print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))