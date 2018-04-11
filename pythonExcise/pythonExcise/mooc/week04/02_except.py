try:
    num = eval(input("请输入一个整数"))
    print (num**2)
except NameError:
    print ("输入不是整数")

'''
可以是
try:
except:
else:       #只有在没有异常发生时，才会奖励性执行
finally:    #不管是否有异常都会执行。

'''