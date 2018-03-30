import random
import datetime
import time

print(time.strftime("%H:%M"))

print(datetime.date.isoformat(datetime.date.today()))

# sleep for 2 second.
time.sleep(2)
print("done")


for i in range(1,10): 
    print(random.randint(1, 10))

# to find all the element of a particular module that you import. 
print(dir(time))

help (time.sleep)