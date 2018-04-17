from bs4 import BeautifulSoup

markup = '<p class="title"><b>The little prince</b></p>'

soup = BeautifulSoup(markup, 'lxml')
print(soup.b)       # <b>The little prince</b>

print(type(soup.b))     # <class 'bs4.element.Tag'>

tag = soup.p

print(tag.name)         # p

print(tag.attrs)        # get all attributes --> {'class': ['title']}

print (tag['class'])    # get a particular attribute value of the tag --> ['title']

print (tag.string)      # get the string value  --> The little prince

print(soup.b.string)    # get the string value  --> The little prince

print (soup.find_all('b'))