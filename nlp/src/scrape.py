import re
import unicodedata

from bs4 import BeautifulSoup

def cleanse(text):
    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'\s+', ' ', text)

    return text

def scrape(html):

    pass