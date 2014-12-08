# coding:utf-8
# 生成的激活码保存到Redis非关系数据库中
'''
1. windows 下redis安装， python redis相关模块安装
2. redis使用
参考
http://www.cnblogs.com/lxx/archive/2013/06/04/3116985.html
http://www.cnblogs.com/dwnblogs/archive/2013/02/25/2931647.html
'''
import redis

# 读取数据
def read_data(data_file):
    f = open(data_file)
    data = []
    for line in open(data_file):
        line = line.strip('\n')
        data.append(line)
    return data

# 向Redis中插入激活码
def insert_code(data):

    r = redis.Redis(host='localhost', port=6379, db=0) # 如果设置了密码，就加上password=密码
    # 删除当前redis中所有数据
    r.flushall()
    for index, active_code in enumerate(data):
        # 写入激活码
        r.set('active_code_'+str(index), active_code)
        print '写入激活码: %s , %s' % ('active_code_'+str(index), active_code)
    # 保存激活码
    r.save()
    # 打印redis中存储数据数目
    print '当前redis共记录数据:', r.dbsize()

if __name__ == '__main__':
    activation_file = "activation_code.txt"
    # 读取激活码
    print 'Read activation code'
    data = read_data(activation_file)
    # 插入激活码
    print 'Insert activation code'
    insert_code(data)
    print 'Finished'