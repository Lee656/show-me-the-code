# coding:utf-8
# 生成的激活码存储到MySQL中
'''
1. 读取activation_code激活码信息
2. MySQLdb 模块完成数据库操作，注意编码问题
'''

import MySQLdb, sys

# 读取数据
def read_data(data_file):
    f = open(data_file)
    data = f.read().split('\n')
    return data

# 向数据库中插入激活码
def insert_code(data):
    try:
        # 连接数据库 创建游标
        conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', port=3306, charset='utf8')
        cur = conn.cursor()
        # 创建数据库 show-me-the-code
        cur.execute('create database if not exists show_me_the_code')
        conn.select_db('show_me_the_code')
        # 创建表 activation_code 和 字段activate_code varchar(35)
        cur.execute('create table activation_code(activate_code varchar(35))')
        # 插入激活码
        cur.executemany('insert into activation_code values(%s)', data)
        # 提交 关闭游标
        conn.commit()
        cur.close()
    except MySQLdb.Error, e:
        print 'Mysql Error %d: %s' % (e.args[0], e.args[1])

if __name__ == '__main__':
    activation_file = "activation_code.txt"
    # 读取激活码
    print 'Read activation code'
    data = read_data(activation_file)
    print data
    # 插入激活码
    print 'Insert activation code'
    insert_code(data)
    print 'Finished'