#coding: utf-8

from flask import request, session, redirect, url_for, render_template, jsonify
from run import app
from model import User, WunderList
import utils, config

@app.route('/')
def index():
    return "Hello World"

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.methods == 'GET':
        return render_template('login.html')
    elif request.methods == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        if username is None or password is None:
            print 'username or password is None'
        password = unicode(password)
        user = User.query.filter_by(username=unicode(username)).first()
        if user is None:
            print 'user is not exist'
        proc_password = utils.encrypt_password(password, salt=config.SALT)
        if utils.check_password(user.password, proc_password):
            session['user'] = user.nickname
            # 记录session
            print 'login ok'
        else:
            print 'password erro'

@app.route('/register/', methods=['POST'])
def register():
    username = request.form.get('username', None)
    nickname = request.form.get('nickname', None)
    password = request.form.get('password', None)
    password_again = request.form.get('password_again', None)
    print username, nickname, password, password_again

    if username is None or nickname is None or password is None or password_again is None:
        print u'输入参数不合法'
    password, password_again, username, nickname = unicode(password), unicode(password_again), unicode(username), unicode(nickname)

    # 1. 用户名是否存在
    user = User.query.filter_by(username=username).first()
    if user:
        print 'user is exist'
    # 2. 密码输入不一致
    if password != password_again:
        print 'password is not same'

    proc_password = utils.encrypt_password(password, salt=config.SALT)
    User.add(User(username, proc_password, nickname))

@app.route('/logout/', methods=['GET'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)
