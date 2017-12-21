from flask import render_template, redirect

from . import app, get_locale


@app.route('/')
def lang_redirect():
    return redirect('/' + app.config['BABEL_DEFAULT_LOCALE'] + '/', code=301)


@app.route('/<lang_code>/')
def index():
    return render_template("index.html")
