from flask import Flask

app = Flask(__name__)

from app import routes
from app import udpRec
print('hello init')

udpRec.startRec(100)