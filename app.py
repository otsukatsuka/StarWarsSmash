from flask import Flask, render_template, request, redirect, url_for
import sys
import urllib
import urllib2
import json

app = Flask(__name__)
episode = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7}

@app.route('/')
def index():
    f = open('rate.json','r')
    jsonData = json.load(f)
    return render_template('index.html',movieInfo = json.dumps(jsonData,indent=4))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
