from app import app
from random import random

@app.route('/')
@app.route('/index')
def index():
    return f'Hello World, random number: {random()}'
