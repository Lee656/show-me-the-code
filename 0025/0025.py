#coding: utf-8
# refer to http://www.jb51.net/article/48597.htm
# so bad, low precision


import speech
while True:
    phrase =speech.input()
    speech.say("You said %s"%phrase)
    if phrase == u"百度":
        print u'打开百度'
        break
