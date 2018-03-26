#initialize a set and add element. 
example = set()

example.add(42)
example.add(3.1415)
example.add("ying Hu")

print (example)

# ignore the element exists. 
example.add(42) 
print (example)

# print the length of the set object.
print (len(example))

# get the info of remove. 
# help (example.remove)

# can remove an existing element. 
example.remove(42) 
print (example)

# can't remove an existing element. 
# example.remove (42)

# now use the discard method to remove an element only when it exists, if it doesn't exist, system won't return error. 
example.discard (50)

# fast way to initialize a set. 
example2 = set([28, True, 2.71, "Helium"])
print(len(example2))

# remove all elements of a set. 
example2.clear()
print(len(example2))


# set union and intersection
odds = set([1,3 , 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2,3,5,7])
composites = set([4, 6, 8 , 9 , 10])

# the union function will return a new set and will not change the odds. 
print (odds.union(evens))

print (odds)

# intersection. 
print(odds.intersection(primes))

# a set with empty element. 
print(odds.intersection(evens))

# to test an element is in a set or not. 
if 2 in evens:
    print ("2 in evens")

if 9 not in evens: 
    print ("9 is not in the evens")