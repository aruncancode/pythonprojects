#twitch subcount tracker / 23/1/2019

from urllib.request import urlopen, Request 
from bs4 import BeautifulSoup as soup 

url = "https://twitchanalysis.top/topsubs_0"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}


client = Request(url=url, headers=headers)
page_html = urlopen(client).read()
page_soup = soup(page_html, "html.parser")

for row in page_soup.find_all('tr'):
    for cell in row.find_all('td'):
        print(cell.text)