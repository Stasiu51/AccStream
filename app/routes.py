from app import app
from random import randint
from flask import render_template, jsonify
import math
from app.udpRec import getLatestDatum, getData
import datetime


reqCount = 0

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', header = 'HELLO')

@app.route('/fetchtest',methods = ['GET'])
def fetchtest():
    data = {'name':'Stasiu','age':21}
    return jsonify(data)

@app.route('/strokedata/<time>', methods = ['GET'])
def fetchdata(time):
    # data = {}
    # N = 50
    # y = 0
    # data['N'] = N
    # getData
    # for i in range(N):
    #     key = str(i)
    #     data[key] = {}
    #     data[key]['x'] = i/N
    #     data[key]['y'] = math.sin(5*i/N + int(dataindex)/10)
    return getData(datetime.datetime.now().timestamp(), 20)

@app.route('/latestdatum')
def latestdatum():
    return str(getLatestDatum())


