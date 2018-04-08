'''
eval will remove the outside most quotes and trying to process the rest information
'''
a = eval("1")
print (a)       # 1

a = eval("1+2")
print (a)       # 3

a = eval('"1+2"')
print (a)       # 1+2

eval ('print("hello")') # hello