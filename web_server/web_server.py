#
# Flask - https://flask.palletsprojects.com/en/1.1.x/
# how to run and execute flask
# https://flask.palletsprojects.com/en/2.0.x/quickstart/
# Rendering templates
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
# static files
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files


import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route('/about.html')
def hello(name=None):
    return render_template('about.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)