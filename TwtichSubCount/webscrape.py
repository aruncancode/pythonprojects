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

for cell in page_soup.find_all('td')[3]:
    cell = page_soup.find_all('td')
    db[cell[2].text] = [cell[0].text, cell[3].text]
print(db)


# for row in page_soup.find_all('tr')[3]:
#     for cell in page_soup.find_all('td'):
#         db[cell[2].text] = [cell[0].text, cell[3].text]
# print(db)

# with open ('twitch_stats.txt', 'w') as db:
#     for row in page_soup.find_all('tr'):
#         for cell in row.find_all('td'): 
#             print(cell.text('channel'))
#             db.write(cell.text.ljust(20))
#         db.write('\n')


