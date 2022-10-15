import csv
import requests
import logging
import scripts.ck_scripts as ck_scripts
import scripts.settings as settings
from time import sleep
from scripts.define_sets import create_and_define_sets
log = logging.getLogger()

def scrape_ck():
    # * Locate the sets, first.
    sets = create_and_define_sets('ck')

    with open('./data/ck/script.csv', 'w', newline='') as imported_data:
        writer = csv.writer(imported_data, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(settings.CARD_BUYLIST_INFO)
        log.info('Opening the file ./data/ck/script.csv ...')
    
    # * Set Cookies, Headers, etc.
        session = requests.Session()
        ck_scripts.get_cookies_header(session)

    # * Begin loop
    # * For every set in the set_file..

        for set in sets:
            page = 1
            r = ck_scripts.request_data(set, page, session)
            if r.status_code == 400:
                log.error('400 Request Header or Cookie Too Large! This might happen if you request too fast.')
                break
            s = ck_scripts.parse_cards(r.text, writer)
            # * Sleep here, because I have to do this slowly or the site might get angry at me :(
            sleep(.8)
            # * If there is more pages, go run this again.
            while ck_scripts.next_page(s) is True:
                page += 1
                r = ck_scripts.request_data(set, page, session)
                s = ck_scripts.parse_cards(r.text, writer)
                sleep(.8)

        session.close()
    imported_data.close()
    