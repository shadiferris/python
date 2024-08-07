#
# Flask - https://flask.palletsprojects.com/en/1.1.x/

from flask import Flask
app = Flask(__name__)
#print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! this is a TEST' 
