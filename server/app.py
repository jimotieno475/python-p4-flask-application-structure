#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

@app.route('/<string:username>')
def user(OluochJim):
    return f'<h1>Profile for {OluochJim}</h1>'

if __name__ == '__main__':
    app.run(port=5555)