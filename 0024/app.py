#coding: utf-8

from flask import request, session, redirect, url_for, render_template, jsonify, flash
from run import app
from model import User, WunderList
import functools
import utils, config


def login_required(func):
    '''
    登录检查
    '''
    @functools.wraps(func)
    def wrapper(*args, **kw):
        if session.get('user', None) is None:
            return redirect(url_for('login'))
        return func(*args, **kw)
    return wrapper


@app.route('/')
@login_required
def index():
    return "Hello World"

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if session.get('user', None) is not None:
            return redirect(url_for('index'))
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        if username is None or password is None:
            flash(u'请检查输入是否为空', 'danger')
            return redirect(url_for('login'))

        user = User.query.filter_by(username=username).first()
        if user is None:
            flash(u'该用户不存在', 'danger')
            return redirect(url_for('login'))

        if not utils.check_password(user.password, password):
            flash(u'密码错误', 'danger')
            return redirect(url_for('login'))

        session['user'] = user.nickname
        return redirect(url_for('index'))

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form.get('username', None)
        nickname = request.form.get('nickname', None)
        password = request.form.get('password', None)
        password_again = request.form.get('password_again', None)

        if username is None or nickname is None or password is None or password_again is None:
            flash(u'请检查输入是否为空', 'danger')
            return redirect(url_for('register'))
        password, password_again, username, nickname = unicode(password), unicode(password_again), unicode(username), unicode(nickname)

        # 1. 用户名是否存在
        user = User.query.filter_by(username=username).first()
        if user:
            flash(u'该用户名已被注册', 'danger')
            return redirect(url_for('register'))
        # 2. 密码输入不一致
        if password != password_again:
            flash(u'两次密码输入不一致', 'danger')
            return redirect(url_for('register'))

        proc_password = utils.encrypt_password(password, salt=config.SALT)
        User.add(User(username, proc_password, nickname))
        flash(u'注册成功', 'success')
        return redirect(url_for('login'))

@app.route('/logout/', methods=['GET'])
@login_required
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)
