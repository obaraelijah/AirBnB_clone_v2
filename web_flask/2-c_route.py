#!/usr/bin/env python3
"""Starts a Flask web application."""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns hello HBNB!"""
    return 'Hello, HBNB!'

@app.route('/hbnb', strict_slashes=False)
def Hbnb_route():
    """Returns  HBNB"""
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Returns  the c page"""
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)