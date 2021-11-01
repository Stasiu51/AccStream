from app import app
from random import randint
from flask import render_template, jsonify


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', header = 'HELLO')

@app.route('/fetchtest',methods = ['GET'])
def fetchtest():
    data = {'name':'Stasiu','age':21}
    return jsonify(data)