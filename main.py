import logging

from flask import flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello from cloud academy'

@app.route('/greet/<name>')
def greet(name):
    return 'Hello' + name

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error has occurred')

    return 'An error has occurred on the servr', 500
