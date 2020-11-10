import requests
from bs4 import BeautifulSoup
import json

searchItem = 'airpods'
finalList = []

for page_number in range(1, 11):
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw=' + searchItem + '&_pgn=' + str(page_number))

    soup = BeautifulSoup(r.text, 'html.parser')

    items = soup.select('li.s-item')
    for item in items:
        result = {}
        titles = item.select('.s-item__title')
        for title in titles:
            result['title'] = title.text

        prices = item.select('.s-item__price')
        for price in prices:
            result['price'] = price.text

        statuses = item.select('.SECONDARY_INFO')
        for status in statuses:
            result['status'] = status.text

        if len(result.items())!=0:
            finalList.append(result)


with open('items.json', 'w') as outfile:
    json.dump(finalList, outfile)
