#
# Flask - https://flask.palletsprojects.com/en/1.1.x/

from flask import Flask, render_template
app = Flask(__name__)
#print(__name__)

@app.route('/')
def hello_world():
    return render_template('./web_server/index.html') 

@app.route('/blog')
def blog(name=None):
    return 'these are my thoughts on blog'

@app.route('/blog/2020/dogs')
def blog2(name=None):
    return 'dog page'