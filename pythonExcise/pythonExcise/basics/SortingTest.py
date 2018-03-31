#Example 1: 
# Sorting the element name by alphbetic order 
earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
earth_metals.sort() # by default , python assumes you want to sort it by alphbetic order 

print (earth_metals)

# sort by reversed alphbetic order 
earth_metals.sort(reverse=True)
print (earth_metals)

# remember sorting changes of things, so the list can be sorted, however if you put the
# above data into a tuples, then you can not sort it directly because tuples are immutable. 

# the following will fail. 
# earth_metals = ("Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")
# earth_metals.sort()

# however you can use the sorted function instead to sort the tuples. 
earth_metals = ("Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")
sorted_earth_metals = sorted(earth_metals)
print (sorted_earth_metals)
print (earth_metals)

data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
print (sorted(data))


# Exmple 2: 
# we want to sort by the 2nd value of the tuple in the planet list. 
planets = [("Mercury", 2440, 5.43), 
            ("Venus", 6052, 5.24), 
            ("Mars", 3397, 1.530), 
            ("Jupiters", 71452, 1.33, 5.21)]

# use lambda to get the size of the planet. 
size = lambda planet: planet[1]

# use the lambda function in the sort "key" value, 
planets.sort(key=size, reverse=True)
print (planets)