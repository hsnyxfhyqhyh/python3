﻿# -*- coding: utf-8 -*-
'''
need to 
pip install requests
pip install bs4

need to download the exe file for lxml: https://files.pythonhosted.org/packages/dd/6e/f0ffb41406def64554a21997ea03861c5089006a070b9de3e12321b7ab38/lxml-3.4.4.win32-py3.4.exe
double click to install and add lxml to the python installation lib folder. . 
'''

import requests
from bs4 import BeautifulSoup

import re

sum =0 

# send a request to some url and get a response. 
r = requests.get("https://book.douban.com/subject/25862578/comments/")

# print the response的 status. 
print(r.status_code)

#create a BeautifulSoup object. 
soup = BeautifulSoup(r.text, 'lxml')               # https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# print (soup.title)

#find all p tag with comment-content class attribute. 
pattern = soup.find_all('p', 'comment-content')

# print all the string values of the above found tags. 
for item in pattern:
    print(item.string)


pattern_s = re.compile('<span class="user-stars allstar(.*?)rating"')

p = re.findall(pattern_s, r.text)

for star in p:
    sum += int(star)

print(sum)