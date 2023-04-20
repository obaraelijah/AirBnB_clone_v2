#!/usr/bin/env python3
"""Starts a Flask web application."""

from flask import Flask

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def Hbnb_route():
    """Returns  HBNB"""
    return 'HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)