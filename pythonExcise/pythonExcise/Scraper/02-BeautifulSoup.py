from bs4 import BeautifulSoup

markup = '<p class="title"><b>The little prince</b></p>'

soup = BeautifulSoup(markup, 'lxml')
print(soup.b)       # <b>The little prince</b>

print(type(soup.b))     # <class 'bs4.element.Tag'>

tag = soup.p

print(tag.name)         # p