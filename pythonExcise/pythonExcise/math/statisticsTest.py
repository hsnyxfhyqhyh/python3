import math
import statistics

round2 = 1      # round the mean and standard deviation to the 10th position. 
data = [7,1,9,14]    

def calcStandardDeviation(d, mean):
    squareSum = 0
    for i in d:
        squareSum += (i - mean)**2

    length = len(d)
    variance = squareSum / length
    varianceSample = squareSum / (length -1)
    
    print("populate variance - ", round(variance, 1))
    print("Sample variance - ", round(varianceSample, 1))

    print("populate standard Deviation - ", round(math.sqrt( variance), 1))
    print("Sample standard deviation - " , round(math.sqrt( varianceSample), 1))

meanValue = round(statistics.mean(data), round2)
print ("Mean - " , meanValue)

calcStandardDeviation(data, meanValue)