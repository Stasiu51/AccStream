from app import app
from random import randint
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', header = 'HELLO')
