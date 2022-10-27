import re
import logging
import arrow
from bs4 import BeautifulSoup
log = logging.getLogger()
local = arrow.utcnow().to('US/Pacific')


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
            float(re.sub('[$,]', '',card_usd[x].text)), # Buylist Price, in USD
            float(re.sub('[$,]', '',card_cred[x].text)),# Buylist Price, in store credit (if supported)
        ]
        writer.writerow(cardBuylistData)
    return searching




