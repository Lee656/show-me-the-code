#coding: utf-8
from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '\xdb\xb2\x18\xf1\xd6\xf2\x10+\xd0\xe3\x1c\x85\xe1o\r\x192j\xed4\x85\xe9B\x87'
from app import *

if __name__ == '__main__':
    app.run(debug=True)
