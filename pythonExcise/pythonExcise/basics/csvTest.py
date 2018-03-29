import csv
from datetime import datetime 

path = "C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\basics\\stock.csv"

'''
# ????????
file = open(path)
for line in file: 
    print (line)
'''

'''
# ??????????
lines = [line for line in open(path)]
print(lines[0])     #Date,Open,High,Low,Close,Volume,Adj Close
print(lines[1])     #8/19/2014,585.002622,587.342658,584.002627,586.862643,978600,586.862643

#??????????lines[0].strip() ????????????
print(lines[1].strip())

# ??????split(',')?tokenize ???? 
print(lines[1].strip().split(','))  # ['8/19/2014', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643']

# ??????nested list ????????? 
dataSet = [line.strip().split(',')  for line in open(path)]
print(dataSet[0])
print(dataSet)

# ????????????nested list. ??????????? ???????????????????????? ??????????????string

'''

'''
?csv module
'''
file = open (path, newline = '')
reader = csv.reader(file)

header = next(reader)           # the first line is the header. 
# data = [row for row in reader]  # read the remaining data   
# print (header)
# print (data[0])

data = []
for row in reader:
    # Date,Open,High,Low,Close,Volume,Adj Close
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1]) #open is a bultin function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

print(data[0])

#compute and store daily stock returns and use csv.writer to write the calculated value into another file. 
return_path = "C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\basics\\stockoutput.csv"
file = open(return_path, 'w')
writer = csv.writer(file)

# write the header of the output file. 
writer.writerow(["Date", "Return"])

for i in range (len(data) -1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1] 
    
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    # calculate return
    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    #writer.writerow([todays_date, daily_return])
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])