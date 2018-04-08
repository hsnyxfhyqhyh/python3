TempStr = input("please enter the temperature with Symbol: ")

if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32 ) / 1.8
    print ("Celsius Temp is: {:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8* eval(TempStr[0:-1] ) + 32
    print("Farenheit Temp is: {:.2f}F".format(F))
else: 
    print("Invalid Format")