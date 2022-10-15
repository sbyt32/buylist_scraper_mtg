import logging
import scripts
from scripts.settings import logging, SITES_TO_SCRAPE
# import scripts.settings as settings

log = logging.getLogger()
log.setLevel(logging.INFO)


def main():
    for site in SITES_TO_SCRAPE:
        log.info(f'Running scrape for {site} ...')
        if site == 'abu':
            scripts.abu()
        elif site == 'csi':
            scripts.csi()
        elif site == 'ck':
            scripts.ck()

if __name__ == '__main__':
    main()


# log.info("Parsed all of the items!") # ? mmmm filler info, replace with something good maybe