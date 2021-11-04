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
    y = 0
    data['N'] = N
    for i in range(N):
        data[N] = {}
        data[N]['x'] = i/N
        data[N]['y'] = y
        y += randint(-1,1)

    print(data)
    return jsonify(data)
