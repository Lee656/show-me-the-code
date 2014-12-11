# coding:utf-8
# 任一个英文的纯文本文件，统计其中的单词出现的个数
'''
1. 使用trie树的结构实现
2. 使用键值对实现(python字典简单)
'''
import sys,os

# 读入数据
def read_data(data_file):
    f = open(data_file)
    return f.read()

# 统计单词数量
def calc_words(data):
    word = ""
    word_cnt = {}
    for s in data:
        if s.isalpha() or s == r"'" or s == '-':
            word += s
        else:
            if word:
                word = word.lower()
                if word in word_cnt:
                    word_cnt[word] += 1
                else:
                    word_cnt[word] = 1
            word = ""
    if word:
        word = word.lower()
        if word in word_cnt:
            word_cnt[word] += 1
        else:
            word_cnt[word] = 1
    return word_cnt

if __name__ == '__main__':
    print '统计单词'
    if len(sys.argv) != 2:
        print '输入参数有误, 格式: python 0004 文件名'
        sys.exit(1)
    try:
        data = read_data(sys.argv[1])
        # 统计单词数目
        word_cnt = calc_words(data)
        for word, cnt in word_cnt.items():
            print 'Word: %s, count: %d' % (word, cnt)
        print '统计完毕'
    except:
        print '出现错误，请确认文件是否存在'




