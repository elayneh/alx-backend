#!/usr/bin/env python3
""" intstantiation Babel """
from flask import Config, Flask, render_template
from flask_babel import Babel


class Config(object):
    """ set up Babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCAL = 'en'


app = Flask(__name__)
app.config.from_object(Config)
b = Babel(app)


@app.route('/')
def index():
    """ Returns the html content """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port=4000)
