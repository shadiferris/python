import requests
from bs4 import BeautifulSoup
import pprint


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
subtext = soup.select(".subtext")

#print(votes[0]
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
  pprint.pprint(hn)
  #return sort_stories_by_votes(hn)



create_custom_hn2(links, subtext)

