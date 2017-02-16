# Making a Web Crawler / Spider

import requests      # request information from a webpage
from bs4 import BeautifulSoup       # sort and evaluate webpage data

def trade_spider(max_pages):
    page = 0
    while page < max_pages:
        url = "https://mobil.bazos.sk"
        # if page is not 0:
        #       url += str(page * 20) #+ "/"

        #print(url)
        source_code = requests.get(url)
        #print(source_code)
        plain_text = source_code.text
        #print(page_source_code)

        soup = BeautifulSoup(plain_text, 'html.parser')   # unspecified parser type produces warning: use 'html.parser'

        links = soup.find_all('a')
        for link in links:
            #print(link)

            href = url + link.get('href')
            print(link.get('href'))
            # print(href)
            # title = link.string
            # print(title)
            # print(href)
            # get_single_item_data(href)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.find_all('span', {'class': 'vypis'}):
    # for item_name in soup.find_all('span'):
        print(item_name.string)

    for link in soup.find_all('a'):
        print(link)
trade_spider(3)