
import urllib.request

from bs4 import BeautifulSoup


response = urllib.request.urlopen('https://www.v2ex.com/')
html = response.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

# print(soup.find_all('span', 'item_hot_topic_title'))

for span in soup.find_all('span', 'item_hot_topic_title'):
    print(span.find('a').string)
