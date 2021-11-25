#!/usr/bin/env python
# coding: utf-8

# In[140]:


#Web Scripting with Python


# In[ ]:





# In[141]:


import requests


# In[ ]:





# In[142]:


#Grabbing a title (html source)


# In[143]:


result = requests.get("http://example.com/")


# In[144]:


type(result)


# In[145]:


#returns the source code from the URL
result.text


# In[146]:


import bs4


# In[147]:


#improves the view of source
soup = bs4.BeautifulSoup(result.text,'lxml')


# In[148]:


type(soup)


# In[149]:


soup


# In[150]:


#grabbing the titles of the source
soup.select('title')


# In[151]:


#grabbing the paragraphs of of the source

soup.select('p')


# In[152]:


#grabbing the head of of the source

soup.select('h1')


# In[153]:


#grabbing the titles only of the source
soup.select('title')[0].getText()


# In[154]:


#grabbing the paragraphs of of the source

soup.select('p')[0].getText()


# In[ ]:





# In[155]:


#Grabbing a Class


# In[156]:


#Syntax to pass to the .select() method         Match Results
#.....................................................................................................................................................................
#soup.select('div')                             All elements with the <div> tag

#soup.select('#some_id')                        The HTML element containing the id attribute of some_id

#soup.select('.notice')                         All the HTML elements with the CSS class named notice

#soup.select('div span')                        Any elements named <span> that are within an element named <div>

#soup.select('div > span')                      Any elements named <span> that are directly within an element named <div>, with no other element in between


# In[157]:


res = requests.get("https://en.wikipedia.org/wiki/Asnoun")
#result.text
soup = bs4.BeautifulSoup(res.text,'lxml')


# In[158]:


#class on webpages need a '.' at the beginning
soup.select('.toctext')


# In[159]:


#first_item = soup.select('.toctext')[0]
first_item = soup.select('.toctext')[0].getText()


# In[160]:


first_item


# In[161]:


for item in soup.select('.toctext'):
    print(item.text)


# In[ ]:





# In[162]:


#Grabbing an Image


# In[163]:


import bs4
import requests

req2 = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
#result.text
soup = bs4.BeautifulSoup(req2.text,'lxml')


# In[164]:


soup


# In[165]:


#class calls need the '.' at the beginning
soup.select('img')[0]


# In[166]:


computer = soup.select('.thumbimage')[0]


# In[167]:


deep_blue = soup.select('img')[0]


# In[168]:


computer['src']


# In[169]:


deep_blue['src']


# In[170]:


#to retrieve/request the image

image_link_computer = requests.get('http://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')


# In[171]:


#image_link_computer.content


# In[172]:


#saves the image to the local computer
f = open('my_computer_image.jpg','wb')


# In[173]:


#written that image to the 'f' image we just created. 

f.write(image_link_computer.content)


# In[174]:


#closing the image on the computer
f.close()


# In[175]:


ls -la


# In[176]:


#convert the cell into a markdown cell and it will display the image
#<img src="http://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png">


# In[ ]:





# In[177]:


# Working with Multiple pages and Items


# In[178]:


#CHALLENGE - get the title of every book with a 2 star rating


# In[179]:


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'


# In[180]:


page_num = 12
base_url.format(page_num)


# In[181]:


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'


# In[182]:


import bs4
import requests

req2 = requests.get(base_url.format(1))
#result.text
soup = bs4.BeautifulSoup(req2.text,'lxml')


# In[183]:


#class=star-rating Four
#class=product_pod
 


# In[184]:


soup


# In[185]:


#displays the .product_pods class which is the parent class for all the pructs on the http://books.toscrape.com/catalogue/page-1.html page (after inspecting it)
#soup.select('.product_pod')[0]
soup.select('.product_pod')


# In[186]:


#refers to the number of products on the page
len(soup.select('.product_pod'))


# In[187]:


products = soup.select('.product_pod')


# In[188]:


#can also be written as:
#example = soup.select('.product_pod')[0]
example = products[0]


# In[189]:


str(example)


# In[190]:


#searching is string is in the source output. Will return True or False
'star-rating Three' in str(example)


# In[191]:


'star-rating Two' in str(example)


# In[192]:


example.select('.star-rating.Three')


# In[193]:


#empty string returns the star rating on the page.
[] == example.select('.star-rating.Two')


# In[194]:


#retrieve the title of the book
example


# In[195]:


example.select('a')


# In[196]:


example.select('a')[1]


# In[197]:


example.select('a')[1]['title']


# In[198]:


#we can check if soemthing is 2 stars (string call in, example.select(rating))
#example.select('a')[1]['title'] to grab the book titles


# In[199]:


two_star_titles = []

#running for pages 1 to 50
for n in range(1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])


# In[200]:


two_star_titles


# In[201]:


three_star_titles = []

#running for pages 1 to 50
for n in range(1,60):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Three')) != 0:
            three_star_titles.append(book.select('a')[1]['title'])


# In[202]:


three_star_titles


# In[ ]:





# In[203]:


#Exercises


# In[204]:


#TASK: Import any libraries you think you'll need to scrape a website.
import bs4
import requests


# In[ ]:





# In[205]:


#TASK: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.

req2 = requests.get("http://quotes.toscrape.com/")
#result.text
soup = bs4.BeautifulSoup(req2.text,'lxml')


# In[206]:


soup


# In[207]:


#TASK: Get the names of all the authors on the first page (no duplicates).
#authors = soup.select('.author')
#note, i only want the name once. so I will use the set() function

authors = set()

for name in soup.select('.author'):
    authors.add(name.text)


# In[208]:


authors


# In[209]:


#TASK: Create a list of all the quotes on the first page.


# In[210]:


soup.select('.text')[0].getText()


# In[211]:


quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)


# In[212]:


quotes


# In[213]:


#TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top 
#right from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath 
#each quote, try to find a class only present in the top right tags, perhaps check the span.


# In[214]:


soup.select('.tag-item')[0].getText()


# In[215]:


for item in soup.select('.tag-item'):
    print(item.text)


# In[216]:


#TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
#Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors 
#on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how
#to check that your loop is on the last page with quotes. For debugging purposes, I will let you know that there are only 
#10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it
#wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!

import bs4
import requests


base_url = 'http://quotes.toscrape.com/page/{}/'
three_star_titles = []

#running for pages 1 to 50
for n in range(1,11):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Three')) != 0:
            three_star_titles.append(book.select('a')[1]['title'])
            
            
            
#authors = set()

#for name in soup.select('.author'):
#    authors.add(name.text)


# In[217]:


base_url = 'http://quotes.toscrape.com/page/'


# In[218]:


#base_url+str(10)

authors = set()

for page in range(1,10):
    page_url = base_url+str(page)
    
    res = requests.get(page_url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")

    for name in soup.select('.author'):
        authors.add(name.text)


# In[219]:


authors


# In[220]:


#base_url+str(10)

authors = set()

for page in range(1,10):
    page_url = base_url+str(page)
    
    res = requests.get(page_url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")

    for name in soup.select('.author'):
        authors.add(name.text)


# In[221]:


url = 'http://quotes.toscrape.com/page/'

# Choose some huge page number we know doesn't exist
page_url = url+str(9999999)

# Obtain Request
res = requests.get(page_url)

# Turn into Soup
soup = bs4.BeautifulSoup(res.text,'lxml')


# In[222]:


'No quotes found!' in res.text


# In[223]:


page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url+str(page)
    
    # Obtain Request
    res = requests.get(page_url)
    
    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break
    
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)
        
    # Go to Next Page
    page += 1


# In[224]:


authors


# In[ ]:




