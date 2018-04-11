
height, weight = eval(input("请输入身高（米）和体重（公斤）[逗号隔开]:"))
BMI = weight/(height ** 2)
print("BMI  数值为{:.2f}".format(BMI))
