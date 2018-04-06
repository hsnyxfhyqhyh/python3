import pprint
import datetime

input_filename= "C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\options\\OptionList.txt"

class Stock: 
    '''
    def __init__(self, stockName, stockPrice,  optionDistance, halfDollarFlag, optionWeekDay):
        Stock=SPY#
            CurrentPrice=223#
            PriceDifference=6#
            HalfDollarFlag=true#
            WeekDay=5
        

        self.symbol =stockName 
        self.price = stockPrice
        self.range = optionDistance
        self.halfDollar = halfDollarFlag
        self.weekDay = optionWeekDay
    '''

    def __init__(self):
        self.symbol = "" 
        self.price = 0
        self.range = 0
        self.halfDollar = False
        self.weekDay = 5

    def getCallOptions(self): 
        #   .GLD180406C125
        prefix ="."
        direction = 'C'
        dateString = '180406'
        price = 125
        
        optionLine = '.'+ self.symbol + dateString + direction + str(price)
        print(optionLine)




#main functions
# if there is an input, a date of a specific week, only generate the options for that week. 
# otherwise , use friday or wednesday of next week. 
# only worry about the current week's Friday or Wednesday. 

def handleStockLine(line):
    stockElements = line.strip().split("#")
    
    st = Stock()

    # print(stockElements)
    for s in stockElements:
        tokens = s.split("=")
        if (tokens[0] == 'Stock'):
            st.symbol = tokens[1]
        
        if (tokens[0] == 'CurrentPrice'):
            st.price = tokens[1]
        
        if (tokens[0] == 'PriceDifference'):
            st.range = tokens[1]

        if (tokens[0] == 'HalfDollarFlag'):
            st.halfDollar = tokens[1]

        if (tokens[0] == 'WeekDay'):
            st.WeekDay = tokens[1]

    st.getCallOptions()

print('Please enter day as MM/dd/YYYY so the option of Friday/Wednesday of that week can be used:')
print ('____________________________')

wednesdayOptionString = ''
fridayOptionString = ''

# convert string to datetime object. 
baseDayString = input()
baseDay = datetime.datetime.strptime(baseDayString, "%m/%d/%Y")

#  Monday starts weekday as 0, Sunday as 6. 
baseDayWeekday = baseDay.weekday()

while (baseDayWeekday !=0):
    print('Please enter day as MM/dd/YYYY so the option of Friday/Wednesday of that week can be used:')
    baseDayString = input()
    baseDay = datetime.datetime.strptime(baseDayString, "%m/%d/%Y")
    baseDayWeekday = baseDay.weekday()


print(baseDayWeekday)


dt = datetime.timedelta (4)             # prepare to advance the day to Friday
friday= baseDay + dt                                        # advance the day to Friday.

dt = datetime.timedelta (2)             # prepare to advance the day to Friday
wednesday = baseDay  + dt

 
fridayOptionString = str(friday.year)[2:4]


print(fridayOptionString)
print(friday.month)
print (wednesday)

lines =[]

with open(input_filename) as fp:
    lines = fp.readlines()

for line in lines:
    if line.startswith("Stock"): 
        pass
        #handleStockLine(line)
        #print("______________________");



    