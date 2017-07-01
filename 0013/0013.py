#coding: utf-8
import requests, re

def scrapy_mm():
    url = r'http://tieba.baidu.com/p/2166231880'
    content = requests.get(url).text
    img_links = re.findall(r'<img pic_type="0" class="BDE_Image" src="(.*?)"', content)
    index = 1
    for link in img_links:
        r = requests.get(link, stream=True)
        if r.status_code == 200:
            with open('download/'+str(index) + '.jpg', 'wb') as f:
                for chunk in r.iter_content(chunk_size=512):
                    if chunk: f.write(chunk)
            index += 1


if __name__ == '__main__':
    scrapy_mm()