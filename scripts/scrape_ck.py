import re
import requests
import logging
import arrow
from bs4 import BeautifulSoup
log = logging.getLogger()
local = arrow.utcnow().to('US/Pacific')

headers = { 
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
}

cookies = {
    "limit": "100",
    "sortBy": "name_asc"
}
session = requests.Session()
page = 1
def get_cookies_header():
    r = session.get('https://www.cardkingdom.com/purchasing/mtg_singles', headers=headers, cookies=cookies)
    if not r.ok: # ? This may need to be changed based on if the error gives back something involving bad (robot) user-agent
        log.error(f"Request had error! HTTP {r.status_code}") 
    session.headers.update(headers)
    session.cookies.update(cookies)
    return r

def request_data(set:str, page:int):
    set = set.replace(" - ", " ").replace(" ", "-").lower().rstrip('\n')
    log.info(f'Grabbing the set: {set}')
    queryString = {
        "filter[sort]":"name_asc",
        "filter[search]":"mtg_advanced",
        "filter[edition]":f"{set}",
        "filter[foils]":"1",
        "filter[singles]":"1",
        "page":f"{page}"
    }
    log.debug(f'Sending request.get to https://www.cardkingdom.com/purchasing/mtg_singles with params:\n{queryString}')
    r = session.get('https://www.cardkingdom.com/purchasing/mtg_singles', params=queryString)
    if r.status_code == 400:
        log.error('400 Request Header or Cookie Too Large! This might happen if you request too fast.')
    return r.text

def parse_cards(r:str, writer):
    # ? This should be done somewhere else, maybe.
    soup = BeautifulSoup(r, 'html.parser')
    log.info('Selecting the soup details for the current page. ')
    card_name = soup.select('div.itemContentWrapper a')
    card_set = soup.select('div.productDetailSet')
    card_usd = soup.select('div.usdSellPrice')
    card_cred = soup.select('div.creditSellPrice')
    searching = soup.select_one("span.pagination-arrow-right:not(.disabled)")


    for x in range(len(soup.select('div.itemContentWrapper'))):
        if "\nFOIL" in card_set[x].text:
            set = re.sub('\([^)]*\)', "", card_set[x].text.strip('\nFOIL\n'))
            foil = "yes"
        else:
            set = re.sub('\([^)]*\)', "", card_set[x].text.strip('\n'))
            foil = "no"

        cardBuylistData = [
            card_name[x].text.strip('\n'),              # Name
            "",                                         # Collector Number
            set.rstrip(),                               # Set
            foil,                                       # Foil Property
            float(card_usd[x].text.replace('$', '')),   # Buylist Price, in USD
            float(card_cred[x].text.replace('$', '')),  # Buylist Price, in store credit (if supported)
        ]
        writer.writerow(cardBuylistData)
    return searching


def next_page(searching):
    log.debug('Checking if page has more results on another page')
    log.debug(searching)
    if searching is not None:
        # * Continue searching
        log.info('Going to the next page...')
        return True
    else:
        # * Stop Searching
        log.info('Set completed, going to the next set...')
        return False

def collapse_requests():
    session.close()
# class store_data():
#     def __init__(self, sets:str, writer) -> None:
#         self.session = requests.Session()
#         self.session.get('https://www.cardkingdom.com/purchasing/mtg_singles', headers=headers, cookies=cookies).headers
#         self.session.headers.update(headers)
#         self.session.cookies.update(cookies)
#         print(self.session.headers)
#         self.writer = writer
#         self.read_sets(sets)

#     def read_sets(self, sets):
#         for set in sets:
#             self.page = 1
#             self.fetch_page(self.name_strip(set))
    
#     def fetch_page(self,set:str):
#         self.current_set = set
#         queryString = {
#             "filter[sort]":"name_asc",
#             "filter[search]":"mtg_advanced",
#             "filter[edition]":f"{set}",
#             "filter[foils]":"1",
#             "filter[singles]":"1",
#             "page":f"{self.page}"
#         }
#         r = self.session.get('https://www.cardkingdom.com/purchasing/mtg_singles', params=queryString)
#         with open('sample.html', 'w', encoding='utf8') as test:
#             test.write(r.text)
#         self.scrape_data(r.text)

#     def scrape_data(self, scraped_page:str):
#         soup = BeautifulSoup(scraped_page, 'html.parser')
#         card_name = soup.select('div.itemContentWrapper a')
#         card_set = soup.select('div.productDetailSet')
#         card_usd = soup.select('div.usdSellPrice')
#         card_cred = soup.select('div.creditSellPrice')
#         testing = soup.select_one("span.pagination-arrow-right:not(.disabled)")

#         for x in range(len(soup.select('div.itemContentWrapper'))):
#             if "\nFOIL" in card_set[x].text:
#                 set = re.sub('\([^)]*\)', "", card_set[x].text.strip('\nFOIL\n'))
#                 foil = "yes"
#             else:
#                 set = re.sub('\([^)]*\)', "", card_set[x].text.strip('\n'))
#                 foil = "no"            
#             cardBuylistData = [
#             card_name[x].text.strip('\n'),              # Name
#             "",                                         # Collector Number
#             set.rstrip(),                               # Set
#             foil,                                       # Foil Property
#             float(card_usd[x].text.replace('$', '')),   # Buylist Price, in USD
#             float(card_cred[x].text.replace('$', '')),  # Buylist Price, in store credit (if supported)
#             ]
#             self.writer.writerow(cardBuylistData)

#     def check_page(self,testing):
#         if testing is not None:
#             self.page += 1
#             self.fetch_page(self.current_set)

#     def name_strip(self, name:str):
#         name = name.replace(" - ", " ").replace(" ", "-").lower()
#         return name.rstrip('\n')

# def store_data(set:str, page:int):
#     with requests.Session() as session:
#         # * Acquire initial headers, cookies and set the ones we want (100 per page, sorted by a-z)
#         session.get('https://www.cardkingdom.com/purchasing/mtg_singles', headers=headers, cookies=cookies).headers
#         # Combine both of these cookies together, 
#         session.headers.update(headers)
#         session.cookies.update(cookies)
#         queryString = {
#         "filter[sort]":"name_asc",
#         "filter[search]":"mtg_advanced",
#         "filter[edition]":f"{set}",
#         "filter[foils]":"1",
#         "filter[singles]":"1",
#         "page":f"{page}"
#         }
#         r = session.get('https://www.cardkingdom.com/purchasing/mtg_singles', params=queryString)
#         soup = BeautifulSoup(r.text, 'html.parser')


