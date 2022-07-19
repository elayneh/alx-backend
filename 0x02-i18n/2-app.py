#!/usr/bin/env python3
""" Get local """
from flask import *
from flask import Babel


class Config(object):
    """ class to set up """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ return local """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Return html content"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(port=4000)
