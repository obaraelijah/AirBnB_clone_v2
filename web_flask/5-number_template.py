#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask , render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''The home page.'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''The hbnb page.'''
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''The c page.'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''The python page.'''
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def number_page(n):
    '''The number page.'''
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    '''The number_template page.'''
    context = {
        'n': n
    }
    return render_template('5-number.html', **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')