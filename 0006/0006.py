# coding:utf-8
# 你有一个目录，放了一你一个月的日记，都是txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词

import os, sys

STOP_WORDS = [] # 存储停词表

# 载入停词表
def load_stop_words():
    global STOP_WORDS
    f = open('stopwords.txt')
    STOP_WORDS = f.read().split('\n')

# 寻找最重要，除去停词以外出现次数最多单词
def find_important_word(file_name):
    f = open(file_name)
    content = f.read()
    word = ""
    word_cnt = {}
    for ch in content:
        if ch.isalpha() or ch == r"'" or ch == '-':
            word += ch
        else:
            if word:
                word = word.lower()
                if word not in STOP_WORDS:
                    if word in word_cnt:
                        word_cnt[word] += 1
                    else:
                        word_cnt[word] = 1
            word = ""
    if word:
        word = word.lower()
        if word not in STOP_WORDS:
            if word in word_cnt:
                word_cnt[word] += 1
            else:
                word_cnt[word] = 1
    word_cnt = sorted(word_cnt.items(), key=lambda d:d[1], reverse=True)
    ret_word = []
    for i in range((5 if len(word_cnt) > 5 else len(word_cnt))):
        ret_word.append(word_cnt[i])
    return ret_word

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'command error!\nUsage: python 0006.py dairy_directory'
        sys.exit(1)

    # 遍历当前目录
    try:
        # 载入停词表
        load_stop_words()

        for (dirpath, dirnames, filenames) in os.walk(sys.argv[1]):
            # 遍历当前文件夹下文件
            for name in filenames:
                file_name = os.path.join(dirpath, name)
                print 'search in %s' % name
                ret_word = find_important_word(file_name)
                # 打印前最多前5个重要词
                print 'the top %d important words:' % len(ret_word)
                for word, times in ret_word:
                    print word, times
                print

    except Exception, e:
        print e
    finally:
        os.system('pause')

