for i in range(1,6):
    print (i)

print("\n")
for j in range (1,6, 2):
    print (j)

print("\n")
for c in 'python123':       #从字符串中取出每个字符， 来循环
    print(c, end=",")       #打印每个字符，在后面加逗号。

print("\n")
for c in 'PYTHON':
    if c=='T':
        continue
    print(c, end = '')

#循环可以和else一起使用如
'''
for: 

else:

'''
#else 只有在循环没有 被break的时候执行，作为正常循环完成的奖励

print("\n")
for c in 'PYTHON':
    if c=='T':
        continue
    print(c, end = '')
else:
    print("正常完成")

print("\n")
for c in 'PYTHON':
    if c=='T':
        break
    print(c, end = '')
else:
    print("正常完成")       #这一行不会被执行，因为有被break.