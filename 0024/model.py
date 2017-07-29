#coding: utf-8

from flask_sqlalchemy import SQLAlchemy
from run import app
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' #sqlite:///开头
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

def init_db():
    db.create_all()

@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    wunderlist = db.relationship('WunderList', backref='user', lazy='dynamic')

    def __init__(self, username, password, nickname):
        self.username = username
        self.password = password
        self.nickname = nickname

    def __repr__(self):
        return '<[User username: {0}, password: {1}, nickname: {2}'.format(self.username.encode('utf-8'), self.password.encode('utf-8'), self.nickname.encode('utf-8'))

    @staticmethod
    def add(user):
        db.session.add(user)
        db.session.commit()

class WunderList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    is_done = db.Column(db.Boolean)
    date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, content, user_id, date=None, is_done=False):
        self.content = content
        self.is_done = is_done
        self.user_id = user_id
        if date is None: self.date = datetime.utcnow()

    def __repr__(self):
        return '<[WunderList content:{0}, date: {1}, user_id: {2}, is_done: {3}>'.format(self.content.encode('utf-8'), self.date, self.user_id, self.is_done)

    @staticmethod
    def add(wunderlist):
        db.session.add(wunderlist)
        db.session.commit()

    @staticmethod
    def delete(wunderlist):
        db.session.delete(wunderlist)
        db.session.commit()

if __name__ == '__main__':
    init_db()


