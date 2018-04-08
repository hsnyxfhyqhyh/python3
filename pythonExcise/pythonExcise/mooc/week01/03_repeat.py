Temp = input("please enter the temperature with symbol: ")

if Temp[-1:] in ('F', 'f'):
    C = ( eval(Temp[0:-1]) -32) / 1.8
    print ("Celsius temperature is {:.2f}".format(C))
elif Temp[-1:] in ('C', 'c'):
    F = 1.8 * ( eval(Temp[0:-1])) +32  
    print ("F temperature is {:.2f}".format(F))
else: 
    print("invalid format")