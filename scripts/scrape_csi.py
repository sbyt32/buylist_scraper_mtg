from bs4 import BeautifulSoup
import logging
log = logging.getLogger()

def store_data(data, writer, set:str):
    # * Parse Response
    """
    * CoolStuffInc uses a .php website link that you must send a POST request to, which then gives you back all the information for the set.
    TODO: Promo, variants, etc has a unique aspect that can be grabbed with

    div.main-container:not([data-rarity='B']) div.search-info-cell div:nth-child(4)

    ? Consider implementing this whenever possible!
    """
    soup = BeautifulSoup(data['html'], 'html.parser').select("div.main-container:not([data-rarity='B'])")
    if soup == []:
        # In case the set does not work don't bother selecting and just gg go next
        log.error(f'The set "{set}" does not work or has no data!')
    else:
        for cardInfo in soup:
            writer.writerow([cardInfo['data-name'], "", set, cardInfo['data-foil'], cardInfo['data-price'], 0])
