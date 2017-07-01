# coding:utf-8

from bs4 import BeautifulSoup
import requests

def fetch_link(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    ret = []
    for item in soup.find_all('a', href=True):
        ret.append(item['href'])
    return ret

if __name__ == '__main__':
    print fetch_link('http://www.tuicool.com/articles/RNFVrm')