html_doc = """
<html><head><title>The Dormouse's story</title></head>
<script type = "j

<body>
<p class="title"><b class = 'BoldClass class2' id= 'id1' anytag='hello'>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

<h2><!--Hey, buddy. Want to buy a used parser?--></h2>

"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser') #soup now contains the html code of the content

#We will get the prettified html code.
#print(soup.prettify())
#To print the title of the html code...
#print soup.title
#To print the title extracted...
#print soup.title.string
#print all the links in the html code
'''
for link in soup.find_all('a'):
	print link 	 #type link.getText() to extract text of the links
'''
'''To print the entire text from the from the html code..
''' 
#print soup.get_text() # or print soup.getText()
'''
To print the tag whose ID is suppose link3 
'''
#print soup.find(id='link3')
'''
To parse any html file located at some directory...
'''
#soup1 = BeautifulSoup(open('index.html'), 'html.parser')
#print soup.title
'''
getting tags out of the html content
'''
tag = soup.b
#print tag #This will print the tag that <b> has.
#print type(tag)#This will return that which type of tag is it.
'''
To print the name of the tag, we use .name and to print the class Name to which it belongs, we use ["class"]
'''
#print tag.name

#print tag['class'] # in case, it has multiple class, it would show an array of class.

'''
Same with id... 
'''
#print tag['id']
'''
Infact you can do this with any tag.
'''
#print tag['anytag']
'''
print tag name
'''
#print tag.name
'''
If there's some comment in the html content, it can 
parse it very easily...
Let's read a comment from the html content...
'''

#comment  = soup.h2.string # this will fetch the string in h2 tag..
#print comment

'''
Parsing head content from <head> tag. This will return an array
including all the tags collectively in <head> tag.
'''

#headTag = soup.head
#print headTag

'''
To print string in set of strings in the html content

'''
#for string in soup.strings:
#	print (repr(string))

'''
Search for the tree
'''