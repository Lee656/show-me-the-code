#coding: utf-8

from flask import Flask, request, g, render_template, redirect, url_for
from datetime import datetime
import sqlite3

app = Flask(__name__)
DATABASE = 'message.db'

@app.route('/')
def index():
    cursor = get_db().cursor()
    cursor.execute('select * from message order by post_time desc, author')
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', data=data)

@app.route('/comment/', methods=['POST'])
def comment():
    author = request.form.get('author', None)
    message = request.form.get('message', None)
    if author is None or message is None:
        return u'填写数据非法!'.encode('utf-8')

    post_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor = get_db().cursor()
    cursor.execute('insert into message(author, message, post_time) values (?, ?, ?)', (author.encode('utf-8'), message.encode('utf-8'), post_time))
    cursor.close()
    get_db().commit()
    return redirect(url_for('index'))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_database_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('create table message (id INTEGER PRIMARY KEY, author varchar(20) NOT NULL, message varchar(500) NOT NULL, post_time datetime DEFAULT CURRENT_TIMESTAMP )')
        cursor.close()
        conn.commit()

if __name__=='__main__':
    # init_db()
    app.run(debug=True)