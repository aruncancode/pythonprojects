#twitch subcount tracker / 23/1/2019
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup

url = "https://twitchanalysis.top/topsubs"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
client = Request(url=url, headers=headers)

page_html = urlopen(client).read()
page_soup = soup(page_html, "html.parser")
db = {}
table = page_soup.find("table", id="topsubs_table")

for row in table.find_all('tr')[1:]:
    cell = row.find_all('td')
    if 'This is a spot for an advertisement' in cell[0].text:
         continue
    else:
        db[cell[2].text] = [cell[0].text, cell[3].text]


userinput = input('username ')
while userinput != 'stop'
    if userinput in db:
        print(db[user])
    elif: userinput == 'all':
        print(db)
    else:
        print('invalid')