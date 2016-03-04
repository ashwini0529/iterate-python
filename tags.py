from bs4 import BeautifulSoup

'''
Suppose we have a HTML tag in the code. To play with tags, and get values, we have certain commands.
'''
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
#To print tag
tag= soup.b
print tag
print soup.b['class']
