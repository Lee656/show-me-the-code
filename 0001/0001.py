# coding:utf-8
# 生成激活码(或优惠券)
# 思路：uuid 生成唯一的激活码
'''
 UUID是128位的全局唯一标识符，通常由32字节的字符串表示。
它可以保证时间和空间的唯一性，也称为GUID，全称为：
        UUID —— Universally Unique IDentifier      Python 中叫 UUID
        GUID —— Globally Unique IDentifier          C#  中叫 GUID

它通过MAC地址、时间戳、命名空间、随机数、伪随机数来保证生成ID的唯一性。
UUID主要有五个算法，也就是五种方法来实现：

   1、uuid1()——基于时间戳
       由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，
       但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。

   2、uuid2()——基于分布式计算环境DCE（Python中没有这个函数）
        算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。
        实际中很少用到该方法。

  3、uuid3()——基于名字的MD5散列值
        通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，
        和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。

   4、uuid4()——基于随机数
        由伪随机数得到，有一定的重复概率，该概率可以计算出来。

   5、uuid5()——基于名字的SHA-1散列值
        算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法

使用方面：
    首先，Python中没有基于DCE的，所以uuid2可以忽略；
    其次，uuid4存在概率性重复，由无映射性，最好不用；
    再次，若在Global的分布式计算环境下，最好用uuid1；
    最后，若有名字的唯一性要求，最好用uuid3或uuid5。
'''
import uuid

if __name__ == '__main__':
    activation_code_num = 200
    print '开始生成激活码,数量为%d' % activation_code_num
    f_out = open('activation_code.txt', 'w')
    for i in range(activation_code_num):
        code = ''.join(str(uuid.uuid1()).split('-'))
        print "第 %d 个激活码: %s" % (i+1, code)
        f_out.write(str(code)+'\n')
    f_out.close()
    print '激活码生成完毕,存储在 activation_code.txt'