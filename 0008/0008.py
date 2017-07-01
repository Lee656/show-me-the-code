# coding:utf-8

from bs4 import BeautifulSoup
import requests, re

def fetch_content(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]
    content = re.sub(r'<[^>]*>', '', soup.prettify())
    while True:
        n_content = re.sub(r'\n\s+?\n', '\n', content)
        if n_content == content:
            break
        content = n_content
    return content

if __name__ == '__main__':
    print fetch_content('http://www.tuicool.com/articles/RNFVrm')