#coding: utf-8

from flask_sqlalchemy import SQLAlchemy
from app import app
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' #sqlite:///开头
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    nickname = db.Column(db.String(255))

    def __init__(self, username, password, nickname):
        self.username = username
        self.password = password
        self.nickname = nickname

    def __repr__(self):
        return '<[User username: `{}`, password: `{}`, nickname: `{}`'.format(self.username, self.password, self.nickname)

class WunderList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('wunderlist', lazy='dynamic'))

    def __init__(self, content, date=None):
        self.content = content
        if date is None: date = datetime.utcnow()

    def __repr__(self):
        return '<[WunderList content: `{}`, date: `{}`>'.formate(self.content, self.date)


