
import urllib.request

response = urllib.request.urlopen('https://www.v2ex.com/')
result = response.read().decode('utf-8')

print(result)
