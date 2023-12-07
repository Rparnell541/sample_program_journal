# URL scraping tool, fetches html using BeautifulSoup library, parses and extracts data from HTML.
import urllib.request as ur
from bs4 import BeautifulSoup

url = input('Enter- ')

html = ur.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count_of_spans = 0
sum = 0

spans = soup('span')
for span in spans:
    sum += int(span.contents[0])
    count_of_spans += 1

print('Count ', count_of_spans)
print('Sum ', sum)
