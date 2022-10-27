import scripts
import logging
from scripts.misc.settings import SITES_TO_SCRAPE
log = logging.getLogger()

def scrape_all_sets():
    for site in SITES_TO_SCRAPE:
        log.info(f'Scraping {site}...')
        if site == 'abu':
            scripts.abu()
        elif site == 'csi':
            scripts.csi()
        elif site == 'ck':
            scripts.ck()
