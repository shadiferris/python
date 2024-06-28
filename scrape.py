import requests
from bs4 import BeautifulSoup


r = requests.get('https://news.ycombinator.com/news', auth=('user', 'pass'))
print(f"this is {r.text}")
#r.status_code
#print(r.status_code)
#print(r.headers['content-type'])