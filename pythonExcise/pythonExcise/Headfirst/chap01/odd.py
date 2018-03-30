import os
from datetime import datetime
from os import getcwd

odds = [1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
       21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
       41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(5):
    right_this_minute = datetime.today().minute
    print (right_this_minute)

    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")

print("hello world")

# this is the fuction in the standard module of os.
# since we import it into the current module , we can use it as a native function inside this module. 
print (getcwd())
print (os.getenv("PATH"))