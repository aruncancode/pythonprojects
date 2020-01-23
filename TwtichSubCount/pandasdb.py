from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
import pandas as pd


url = "https://twitchanalysis.top/topsubs_0"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}


client = Request(url=url, headers=headers)
page_html = urlopen(client).read()
page_soup = soup(page_html, "html.parser")

db = pd.read_html(page_html, index_col=4, attrs={"class": 'generalTable'})

file = './test.csv'

