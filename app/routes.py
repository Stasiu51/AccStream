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

@app.route('/strokedata', methods = ['GET'])
def fetchdata():
    data = {}
    N = 100
    x = 0
    for i in range(N):
        data[i/N] = x
        x += randint(-1,0,1)
    return jsonify(data)
