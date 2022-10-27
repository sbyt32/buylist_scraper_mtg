import csv
import requests
import logging
import scripts
import scripts.site_scraping
import scripts.misc.settings as settings
from time import sleep
log = logging.getLogger()

def scrape_ck():
    # * Locate the sets, first.
    sets = scripts.misc_create_define_sets('ck')

    with open('./data/ck/script.csv', 'w', newline='') as imported_data:
        writer = csv.writer(imported_data, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(settings.CARD_BUYLIST_INFO)
        log.info('Opening the file ./data/ck/script.csv ...')
    
    # * Set Cookies, Headers, etc.
        session = requests.Session()
        scripts.site_scraping.ck_get_cookies_header(session)

    # * Begin loop
    # * For every set in the set_file..

        for set in sets:
            set = set.replace(" - ", " ").replace(" ", "-").lower().rstrip('\n')
            page = 1
            # * Request Data
            r = scripts.site_scraping.ck_request_data(set, page, session)

            if r.status_code == 400:
                log.error('400 Request Header or Cookie Too Large! Check if the cookies are too large?')
                break

            s = scripts.site_scraping.ck_parse_cards(r.text, writer)
            # * Sleep here, because I have to do this slowly or the site might get angry at me :(
            sleep(.8)
            # * If there is more pages, go run this again.
            while scripts.site_scraping.ck_next_page(s) is True:
                page += 1
                r = scripts.site_scraping.ck_request_data(set, page, session)
                s = scripts.site_scraping.ck_parse_cards(r.text, writer)
                sleep(.8)

        session.close()
    imported_data.close()
    