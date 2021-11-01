from app import app
from random import randint

@app.route('/')
@app.route('/index')
def index():
    return f'Hello World 2, random number: {randint(0,10)}'
