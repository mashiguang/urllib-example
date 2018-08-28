
import urllib.request

from bs4 import BeautifulSoup


response = urllib.request.urlopen('https://www.v2ex.com/')
html = response.read().decode('utf-8')

soup = BeautifulSoup(html)

print(soup.select('span.item_hot_topic_title'))
