from app import app
from random import randint

@app.route('/')
@app.route('/index')
def index():
    return f'Hello World, random number: {randint(0,10)}'
