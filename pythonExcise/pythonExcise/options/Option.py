import datetime

input_filename= "C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\options\\OptionList.txt"
output_folder = "C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\options\\output\\"

class Stock: 
    def __init__(self):
        self.symbol = "" 
        self.price = 0
        self.range = 0
        self.halfDollar = False
        self.weekDay = 5

    def writeOptionsInFile(self, wednesdayOptionString : str, fridayOptionString: str, optionDirection: str): 
        prefix ="."
        option = ''
        
        lowrange = self.price - self.range 
        highrange = self.price + self.range

        optionDateString = fridayOptionString
        if self.weekDay == 2: 
            optionDateString = wednesdayOptionString

        increase = 1
        
        # if halfDollar value is "True", modify the increase value to 0.5
        if (self.halfDollar == "True"): 
            increase = 0.5
        else: 
            increase = 1

        while lowrange <= highrange: 
            if str(lowrange)[-2:] == '.0': 
                lowrange = int(lowrange)

            optionLine = '.' + self.symbol + optionDateString + optionDirection + str(lowrange) 
                
            option = option + optionLine + '\n'
            lowrange += increase
        
        # decide the file name 
        filename = output_folder + '.' + self.symbol + optionDateString + optionDirection + '.txt'

        with open(filename, 'w') as out:
            out.write(option )

# main functions
# if there is an input, a date of a specific week, only generate the options for that week. 
# otherwise , use friday or wednesday of next week. 
# only worry about the current week's Friday or Wednesday. 
wednesdayOptionString = ''
fridayOptionString = ''

def handleStockLine(line):
    stockElements = line.strip().split("#")
    
    st = Stock()

    for s in stockElements:
        tokens = s.split("=")
        if (tokens[0] == 'Stock'):
            st.symbol = tokens[1]
        
        if (tokens[0] == 'CurrentPrice'):
            st.price = int(tokens[1])
        
        if (tokens[0] == 'PriceDifference'):
            st.range = int(tokens[1])

        if (tokens[0] == 'HalfDollarFlag'):
            st.halfDollar = tokens[1]

        if (tokens[0] == 'WeekDay'):
            st.weekDay = int(tokens[1])

    st.writeOptionsInFile(wednesdayOptionString, fridayOptionString, 'C')
    st.writeOptionsInFile(wednesdayOptionString, fridayOptionString, 'P')

def padZero(num : int) -> str:
    '''pad leading zeros to month and day'''

    if len(str(num))==1:
        return "0" + str(num)
    else: 
        return str(num)

print('Please enter day as MM/dd/YYYY so the option of Friday/Wednesday of that week can be used:')
print ('____________________________')

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


dt = datetime.timedelta (4)             # prepare to advance the day to Friday
friday= baseDay + dt                    # advance the day to Friday.

dt = datetime.timedelta (2)             # prepare to advance the day to Wednesday
wednesday = baseDay  + dt               # advance the day to Wednesday.

# save the strings into global variables.
fridayOptionString = str(friday.year)[2:4] + padZero(friday.month) + padZero(friday.day)
wednesdayOptionString = str(wednesday.year)[2:4] + padZero(wednesday.month) + padZero(wednesday.day)

lines =[]

with open(input_filename) as fp:
    lines = fp.readlines()

for line in lines:
    if line.startswith("Stock"): 
        
        handleStockLine(line)
