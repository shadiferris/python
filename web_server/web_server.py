#
# Flask - https://flask.palletsprojects.com/en/1.1.x/
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)
#print(__name__)

@app.route('/')
def hello_world():
    return render_template('./templates/index.html')

@app.route('/hello/')
@app.route('/hello/')
def hello(name=None):
    return render_template('./index.html', name=name)

@app.route('/blog')
def blog(name=None):
    return 'these are my thoughts on blog'

@app.route('/blog/2020/dogs')
def blog2(name=None):
    return 'dog page'
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about.html')
def hello(name=None):
    return render_template('about.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)