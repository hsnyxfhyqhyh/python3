import statistics

data= [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

avg = statistics.mean(data)
print (avg)
# 2.183333333333333

# filter works the same way as the map, but filter out the element that only qualifies the filter function f
# here we are trying to get a list of data that is larger than the mean value of the list. 
print(list (filter(lambda x: x > avg, data))  )
# output: [2.7, 4.1, 4.3]


#remove the missing data
countries =["", "Argentina", "", "Chile", "", "Columbia", "", "Ecudor", "","", "Venezuela"]
print (list (filter(None, countries))   )
#   Output: ['Argentina', 'Chile', 'Columbia', 'Ecudor', 'Venezuela']