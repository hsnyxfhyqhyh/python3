import random
random.seed(10) #当确定种子时，下行产生的随机数是固定的，这对于我们在编程中需要复现同一个随机数有帮助。如果不给种子，系统会以系统时间的值缺省为种子。

print(random.random())

print(random.randint(3, 100))  #产生3-100之间的一个随机整数

print(random.randrange(10,100, 10)  ) #产生10到100之间的以10为步长的随机整数