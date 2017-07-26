#!/usr/bin/env python
#coding=utf-8

import urllib.request
import re
import os
if __name__ ==  '__main__':
    #url = 'https://www.qiushibaike.com/text/page/3/?s=5003526'
    url = 'https://www.qiushibaike.com/text/'
    #url = 'http://www.maiziedu.com/'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.0.4.3000 Chrome/47.0.2526.73 Safari/537.36'}
    req = urllib.request.Request(url = url, headers=header )
    response = urllib.request.urlopen(req)
    the_page = response.read().decode('utf-8')
    #'<div class="content">.*?<span>(.*?)</span>'
    pattern = re.compile('<a href="/users/(\d+)/" target="_blank" title="(.*?)">.*?<div class="content">.*?<span>(.*?)</span>', re.S)
    items = re.findall(pattern, the_page)
    for item in items:
        #print(item[0],item[1],item[2])
        item_new = item[2].replace('\n','').replace('<br/>','\n')
        path = 'qiubai'
        if not os.path.exists(path):
            os.makedirs(path)
        filepath =  path + '/' + item[1] + '.txt'
        f = open(filepath, 'w')
        f.write(item_new)
        f.close()