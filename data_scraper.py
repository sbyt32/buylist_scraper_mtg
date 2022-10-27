import scripts
import logging
scripts.log_setup()
log = logging.getLogger()
log.setLevel(logging.INFO)

def main():
    # TODO: Set up debug / testing scripts
    scripts.scrape_all_sets()
    scripts.sf()

if __name__ == '__main__':
    main()

# log.info("Parsed all of the items!") # ? mmmm filler info, replace with something good maybe