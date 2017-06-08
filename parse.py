#! /usr/bin/python3

import bs4
import json


read_history = open('read_history.html', encoding="GBK")


html = bs4.BeautifulSoup(read_history,"html.parser")

history = []

# print(html.find_all('table')[1].find_all('tr'))
for tr in html.find_all('table')[1].find_all('tr'):

    # print(tr.find_all('td'))
    tds = tr.find_all('td')
    # print( tds[0].string + ', '  + tds[1].string + ', ' + tds[2].string + ', ' + tds[3].string)
    # print("%s, %s, %s, %s" %(tds[0].string.strip() ,tds[1].string.strip(), tds[2].string.strip(), tds[3].string.strip()))

    td = {'number': tds[0].string.strip(),
          'name':   tds[1].string.strip(),
          'code': tds[2].string.strip(),
          'operation': tds[3].string.strip()}

    history.append(td)

    # tds_json = json.dumps(tds_dict, indent=2, ensure_ascii=False)

    # print("%s, " %(tds_json))
    # print(json.dumps(tds_dict, indent=2, ensure_ascii=False))

print(json.dumps(history, indent=2, ensure_ascii=False))
    
    
    # for td in tr.find_all('td'):
        # content = td.string.strip()
        # print(content, end=", ")
        # print(td.string.strip(), end=', ')
    # print()

# print(html.find_all('table')[1].find_all('tr'))

#print(html)
