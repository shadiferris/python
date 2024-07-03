import requests
from bs4 import BeautifulSoup


res = requests.get('https://news.ycombinator.com/news', auth=('user', 'pass'))
#print(f"this is {r.text}")
#r.status_code
#print(r.status_code)
#print(r.headers['content-type'])

soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())
#print(soup.find_all('div'))
#print(soup.find_all('title'))
# https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
#print(soup.select("#up_40862436"))
links = soup.select(".sitebit")
votes = soup.select(".score")

print(votes[0])