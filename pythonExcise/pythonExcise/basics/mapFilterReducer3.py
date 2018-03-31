# from python 3, Reducer is not a built-in function.
# it has been moved to the functools module
# according to the python creator, Guido van Rossum, "Use functools.reduce() if you really need it; however 99% of the time the explicit for loop is more readable. 

# Reduce function
# Data: [a1, a2, ...., an]
# Function : f(x, y)
# reduce(f, data)
#   step1: val1=f(a1, a2)
#   step2: val2=f(val1, a3)
#   step3: val3=f(val2, a4)
#   step...
#   step n-1: val<n-1> = f(val<n-2>, an)
#   return: val<n-1>

#   Alternatively, it returns f(f(f(a1,a2), a3), a4),.......an)

# Example: multiply all numbers in a list. 
from functools import reduce

data=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# use of reduce function. 
multiplier = lambda x, y: x * y
print (reduce(multiplier, data))

#direct use of for loop
product = 1
for x in data: 
    product = product * x

print(product)

# obviously the for loop is much easier to read. 
