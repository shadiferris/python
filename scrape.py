import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('http://news.ycombinator.com/news', auth=('user', 'pass'))
res2 = requests.get('https://news.ycombinator.com/news?p=2', auth=('user', 'pass'))
#print(f"this is {r.text}")
#r.status_code
#print(r.status_code)
#print(r.headers['content-type'])

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
#print(soup.prettify())
#print(soup.find_all('div'))
#print(soup.find_all('title'))
# https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
#print(soup.select("#up_40862436"))
#links = soup.select(".titleline")
#votes = soup.select(".score")
#subtext = soup.select(".subtext")

links = soup.select('.titleline > a') #heads up! .storylink changed to .titleline
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a') #heads up! .storylink changed to .titleline
subtext2 = soup2.select('.subtext')

multi_links = links + links2
multi_subtexts = subtext + subtext2

#print(votes[0]
'''
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        #href = links[idx].get('href', None)
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    pprint.pprint(hn)
'''

def sort_stories_by_votes(hnlist):
   pprint.pprint(sorted(hnlist, key= lambda k:k['votes'], reverse=True))


def create_custom_hn2(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  #pprint.pprint(hn)
  pprint.pprint(sort_stories_by_votes(hn))
  #return sort_stories_by_votes(hn)
  # 

create_custom_hn2(multi_links, multi_subtexts)

