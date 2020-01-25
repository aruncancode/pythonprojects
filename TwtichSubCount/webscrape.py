#twitch subcount tracker / 23/1/2019
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import csv


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}


link = 0
db = {}

while link <=40:
    url = "https://twitchanalysis.top/topsubs_" + str(link)
    client = Request(url=url, headers=headers)
    page_html = urlopen(client).read()
    page_soup = soup(page_html, "html.parser")
    table = page_soup.find("table", id="topsubs_table")

    for row in table.find_all('tr')[1:]:
        cell = row.find_all('td')
        if 'This is a spot for an advertisement' in cell[0].text:
            continue
        else:
            db[cell[2].text] = [cell[0].text, cell[3].text]

    print(link)
    link += 1


print(len(db))

# with open('database.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['name', 'rank', 'subs', 'monthly income', 'salary'])
#     for key, value in db.items():
#         est_income = int(value[1]) * 3.5 * 1.47
#         yearly = est_income*12
#         writer.writerow([key, value[0], value[1], est_income, yearly])


userinput = input('command ')
while userinput != 'stop':
    if userinput in db:
        print(db[userinput])
        userinput = input('command ')
    elif userinput == 'all':
        print(db)
        userinput = input('command ')
    else:
        print('invalid')
        userinput = input('command ')
