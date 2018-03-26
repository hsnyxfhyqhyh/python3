import logging

# Create and configure logger. create the following file in the location, if doesn't exist then creates it. 
# logging.basicConfig(filename = "C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\myLog.log")  # default level to 20
# logging.basicConfig(filename = "C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\myLog.log", level = logging.DEBUG) # has no time in the log

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
# logging.basicConfig(filename = "C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\myLog.log", level = logging.DEBUG, format = LOG_FORMAT)  # the log message will have time stamp

# the following line adds one more parameter, to default the mode to overwrite mode instead of append mode. 
logging.basicConfig(filename = "C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\myLog.log", level = logging.DEBUG, format = LOG_FORMAT, filemode = "w")  


logger = logging.getLogger()

# Test the logger. 
logger.info("our first message")        # the line create the file but didn't log the message. because the logger's level s default to Warning. 

# Level : 0 - NOTSET ; 10- DEBUG; 20 -INFO;  30 - WARNING; 40 - ERROR; CRITICAL - 50
print (logger.level)






