import logging
import os
import scripts.site_scraping

log = logging.getLogger()

def scrape_sf():
    if not os.path.exists('data/scryfall/scryfall_bulk.json'):
        scripts.site_scraping.sf_bulk_scrape()
    if not os.path.exists('data/scryfall/sets_to_fetch.txt'):
        scripts.site_scraping.sf_set_name_scraper()