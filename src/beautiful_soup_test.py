
import urllib.request

from bs4 import BeautifulSoup


response = urllib.request.urlopen('https://www.v2ex.com/')
html = response.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

# print(soup.find_all('span', 'item_hot_topic_title'))

for span in soup.find_all('span', 'item_title'):
    print(span.find('a').string)

for img in soup.find_all('img', 'avatar'):
    print(img.parent['href'])

for tr in soup.select('div.item table tr'):
    member = tr.find('img', 'avatar').parent['href']
    title = tr.select('span.item_title a')[0].string
    print('%-32s %s' % (member, title))


