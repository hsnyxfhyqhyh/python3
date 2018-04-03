from flask import Flask

# This content is in the chapter 5 of the head first python 2nd edition book. 

# before running this file, need to install by "pip install flask"

# enter this folder from command prompt, and "python helloflask.py" to run, 
# this will start the web server of flask, and wait
# open a browser and type in http://127.0.0.1:5000  you will see the hello world line print out as output. 
app= Flask(__name__)

@app.route("/")

def hello() ->str:
    return 'hello world from flask'

app.run()