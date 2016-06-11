from flask import Flask, render_template, request, redirect, url_for
import sys
import urllib
import urllib2
import json


app = Flask(__name__)
OMDB_URL = "http://www.omdbapi.com/?"


@app.route('/')
def index():
    url = OMDB_URL+"t=Star+Wars&y=1977&plot=short&r=json"
    req = urllib2.urlopen(url)
    jsonData = json.loads(req.read())
    return render_template('index.html',movieInfo = json.dumps(jsonData,indent=4))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
