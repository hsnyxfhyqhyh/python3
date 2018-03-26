import datetime

#print(dir(datetime))
#help(datetime.date)

dob = datetime.date(1975, 1, 1)

print(dob)                              # 1975-01-01        , default format in yyyy-mm-dd
print (dob.year)
print (dob.month) 
print (dob.day)


# adding days to the time
dt = datetime.timedelta (100)           # 100 days to the 
print (dob + dt)                        # 100 days added to the pre-set dob.

# Format the date format
print (dob.strftime("%A, %B, %d, %Y"))  # change the format of the date.      Wednesday, January, 01, 1975

message = "Ying was born on {:%A, %B, %d, %Y}. "
print (message.format(dob))

# introduce the date/time/datetime object. 
launch_date = datetime.date(2017, 3, 20)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3,20, 22, 27, 0)

print(launch_date)                      # 2017-03-20
print(launch_time)                      # 22:27:00
print (launch_datetime)                 # 2017-03-20 22:27:00

# get the time of NOW. 
now = datetime.datetime.today()
print (now)                             # 2018-03-25 18:08:36.951307

# convert string to datetime object. 
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")

print (moon_landing_datetime)           # 1969-07-20 00:00:00

