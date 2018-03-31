import math

def area (r):
    '''return area of a circle with radius 'r' '''
    return math.pi* (r**2)

radii = [2, 5, 7.1, 0.3, 10]

#Method 1: direct method
areas = []

for r in radii:
    a = area (r)
    areas.append(a)

print (areas)

#Method 2: use map: 
# this one tells the system to operate through the iterable object radii 
# and and for each item in the iterable , apply the area function and add it to the final map
# then we create a list based on the map  and print
print( list(map(area, radii))   )

# In general, you have
#   data:   a1, a2, a3, 
#   Function: f
#   map(f, data) - returns iterator over f(a1), f(a2), ....f(an)


#Example 2
#tuples of location, temparature in celcius
temps = [("Berlin", 29), ("Cario", 36), ("Buenos Aires", 19), ("Los Angels", 26), 
    ("Tokyo", 27), ("New York", 28), ("London", 22), ("Beijing", 32)]

#use lambda function to do the convert, input of lambda is the element of tuples.
c_to_f = lambda data: (data[0], (9/5) * data[1] + 32)
print( list(map(c_to_f, temps)) )

# output
# [('Berlin', 84.2), ('Cario', 96.8), ('Buenos Aires', 66.2), ('Los Angels', 78.80000000000001), 
#    ('Tokyo', 80.6), ('New York', 82.4), ('London', 71.6), ('Beijing', 89.6)]