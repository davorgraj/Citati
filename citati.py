import urllib
import random
from BeautifulSoup import BeautifulSoup


url = 'http://quotes.yourdictionary.com/theme/marriage/'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

quotes = []
quotes = soup.findAll('p', attrs={'class': 'quoteContent'})
five_quotes = random.sample(quotes,  5)

for quote in five_quotes:
    print quote.text