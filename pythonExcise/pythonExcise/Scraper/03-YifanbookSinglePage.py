# -*- coding: utf-8 -*-

import requests
import io  
import sys  
import re

from bs4 import BeautifulSoup

r = requests.get("http://www.shuku.net:8082/novels/history/yxzgdsj/mzdn01.html")

print(r.status_code)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 

#print(r.text)  # 能够写文件的全部html

# 好像这个正则表达式不工作。
pattern_s = re.compile('<pre>(.*?)</pre>')

p = re.findall(pattern_s, r.text)

for c in p:
    print(c)

