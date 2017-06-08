#! /usr/bin/python3

import bs4
import json


read_history = open('read_history.html', encoding="GBK")
html = bs4.BeautifulSoup(read_history,"html.parser")
history = []

with open('history.json', 'w') as fp:
    for tr in html.find_all('table')[1].find_all('tr'):
        tds = tr.find_all('td')
        td = {'number': tds[0].string.strip(),
              'name':   tds[1].string.strip(),
              'code': tds[2].string.strip(),
              'operation': tds[3].string.strip()}

        history.append(td)

    json.dump(history, fp, indent=2, ensure_ascii=False)


