#!/usr/bin/env python3
""" Babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """ Configure Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ return locale """
    locale = request.args.get('locale', None)

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Return html """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(port="4000")
