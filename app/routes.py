from app import app
from random import randint
from flask import render_template, jsonify
import math

reqCount = 0

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', header = 'HELLO')

@app.route('/fetchtest',methods = ['GET'])
def fetchtest():
    data = {'name':'Stasiu','age':21}
    return jsonify(data)

@app.route('/strokedata/<dataindex>', methods = ['GET'])
def fetchdata(dataindex):
    data = {}
    N = 50
    y = 0
    data['N'] = N
    for i in range(N):
        key = str(i)
        data[key] = {}
        # data[key]['x'] = i/N
        # data[key]['y'] = y
        # y += randint(-1,1)
        data[key]['x'] = i/N
        data[key]['y'] = math.sin(3*i/N + int(dataindex)/10)
    return jsonify(data)
