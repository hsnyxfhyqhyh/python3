'''
如果有可选参数在定义中，那么可选参数应该放在不可选参数的定义后方。 如例中的m值在调用时是不需要传入的。 

'''
def fact(n, m=1):
    s=1
    for i in range (1, n+1):
        s *=i
    return s/m

print (int(fact (10)))
print (int(fact (10, 2)))
# 也可以用参数名字的方式来调用函数， 这样可以不用用函数定义的参数位置顺序来缺省调用
print (int(fact (m=2, n=10)))

'''
下面是一个函数的定义， 参数的数量是不限制的。 

'''
def fact2(n, *b):
    s = 1
    for i in range (1, n+1):
        s *=i
    for item in b:
        s*= item 

    return s
''' b 只有一个值'''
print (int(fact2(10, 3)))
''' b 有三个值'''
print (int(fact2(10, 3, 5 , 8)))

'''
一个函数可以返回几个值

'''
def fact3(n, m=1): 
    s=1
    for i in range (1, n+1):
        s *=i
    return s/m, n, m        # return tuples

print (fact3(10, 2))

#或者定义三个变量分别接受返回的三个值。 
a, b, c = fact3(10, 2)

print(a)
print(b)
print(c)