#coding: utf-8

from flask import Flask, request, session, redirect, url_for, render_template, jsonify
app = Flask(__name__)

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
        # check password

@app.route('/register/', methods=['POST'])
def register():
    username = request.form.get('username', None)
    nickname = request.form.get('nickname', None)
    password = request.form.get('password', None)
    password_again = request.form.get('password_again', None)
    # 1. 用户名是否存在
    # 2. 密码输入不一致

@app.route('/logout/', methods=['GET'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)
