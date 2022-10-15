import csv
from time import sleep
import requests
import logging
import json
import os
import scripts
from urllib.parse import quote
from log_example import log

log = logging.getLogger()
log.setLevel(logging.INFO)

sites_to_scrape = [
    'abu',  # ABUGames.com
    'ck',   # CardKingdom.com
    'csi'   # CoolStuffInc.com
    # ...
]

cardBuylistInfo = [
    "name",     # Name
    "card_num"  # Collector Number (if supported, ABU Specific)
    "set",      # Set
    "foil",     # Foil Property
    "usd",      # Buylist Price, in USD
    "credit"    # Buylist Price, in store credit (if supported)
]

def _send_request(method:str, url:str, **kwargs) -> dict:
    """
    Catch all wrapper for sending web request and interpreting as json
    """

    log.debug(f"Sending request to {url} with args {kwargs}")
    r = requests.request(method, url, **kwargs)

    # basic error checking
    if not r.ok:
        log.error(f"Request had error! HTTP {r.status_code}")

    # Try to decode response
    data = {}
    try:
        data = json.loads(r.text)
    except json.JSONDecodeError as e:
        log.exception(f"Failed to decode response as json, was there an error in request?: {e}")
    return data


def create_and_define_sets(site):
    # * Create directory to hold data if not exist
    if not os.path.exists(f'./data/{site}'):
        log.info(f'Creating directory for {site}...')
        os.makedirs(f'./data/{site}')

    # * Check if the set_name_{site}.txt exists, which contains the way the site organizes their cards.
    try:
        log.debug(f'Checking ./data/{site}/set_name.txt exists')
        setList = open(f'./data/{site}/set_name.txt')
    except FileNotFoundError:
        # TODO: Create script that makes the directories? Adapt from older script.
        log.error(f'Directory "./data/{site}/set_name.txt" does not exist! Create the file first by running this other script.')
        # ? Maybe check that, if above does not work, break something?
    else:
        log.info(f'Opening set folder for {site}...')
        # * Get the list of sets and close the file, then return it.
        sets = setList.readlines()
        setList.close()
        return sets[:2]

# AlphaBetaUnlimitedGames, aka ABUGames
def scrape_abu():
    # *Locate the sets, first. 
    sets = create_and_define_sets('abu')

    with open('./data/abu/script.csv', 'w', newline='') as imported_data:
        writer = csv.writer(imported_data, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(cardBuylistInfo)
        log.info('Opening the file ./data/abu/script.csv ...')

    # * Begin loop
    # * For every set in the set_file...

        for set in sets:
            set = set.strip('\n')
            # * Prepare request
            params = {
                    "facet.field":["magic_edition","rarity","buy_price","trade_price","language","card_style"],
                    "facet.mincount":"1",
                    "facet.limit":"-1",
                    "facet":"on",
                    "indent":"on",
                    "q":"*:*",
                    "fq":   [
                        "-buy_price:0 -buy_list_quantity:0 -magic_features:(\"Actual Picture Card\") +display_title:*",
                        "category:\"Magic the Gathering Singles\"",
                        "language:(\"English\")",
                        "-condition:(\"PLD\",\"HP\",\"SP\",\"MINT\")"
                        f"magic_edition:(\"{set}\")",
                        ],
                    "sort":"magic_edition_sort asc,display_title asc",
                    "fl":"id,artist,card_style,language,layout,magic_edition,magic_edition_sort,category,multiverseid,title,product_id,display_title,simple_title,price,quantity,buy_list_quantity,buy_price,trade_price,condition,production_status,card_number",
                    "group":"true",
                    "group.field":"product_id",
                    "group.ngroups":"true",
                    "group.limit":"10",
                    "start":"0",
                    # ! Consider NOT doing >= 1000 (You broke the fucking website :skull:)
                    "rows":"999",
                    "wt":"json"
                    }
            url = "https://data.abugames.com/solr/nodes/select"

            # * Send request
            r = _send_request('GET', url, params=params)

            # * Process response
            # * Check if empty.
            if r['grouped']['product_id']['groups'] == []:
                log.error(f'The set "{set}" does not work or has no data!')
                continue

            scripts.abu(r,writer)
            
    imported_data.close()

# CardKingdom
def scrape_ck():
    # * Locate the sets, first.
    sets = create_and_define_sets('ck')

    with open('./data/ck/script.csv', 'w', newline='') as imported_data:
        writer = csv.writer(imported_data, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(cardBuylistInfo)
        log.info('Opening the file ./data/ck/script.csv ...')
    
    # * Set Cookies, Headers, etc.
        scripts.ck_cookies_header()

    # * Begin loop
    # * For every set in the set_file..

        for set in sets:
            page = 1
            r = scripts.ck_request_data(set, page)
            s = scripts.ck_parse_data(r, writer)
            # * Sleep here, because I have to do this slowly or the site might get angry at me :(
            sleep(1.5)
            # * If there is more pages, go run this again.
            # ? Because I have to load the page and parse the data first, this needs to be like this (I think)
            while scripts.ck_next(s) is True:
                page += 1
                r = scripts.ck_request_data(set, page)
                s = scripts.ck_parse_data(r, writer)
                sleep(1.5)

    imported_data.close()
    scripts.ck_close()

# CoolStuffInc
def scrape_csi():
    sets = create_and_define_sets('csi')

    with open('./data/csi/script.csv', 'w', newline='') as imported_data:
        writer = csv.writer(imported_data, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(cardBuylistInfo)
        log.info('Opening the file ./data/csi/script.csv ...')

    # * Begin loop
    # * For every set in the set_file...

        for set in sets:
            # * Prepare request
            set = set.strip('\n')
            params = f"ajaxtype=selectProductSetName2&ajaxdata={quote(set)}&gamename=mtg"
            headers = {
                "cookie": "cid=cid6344b0690ff865.72132599",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "null",
                "Connection": "keep-alive",
                "Cookie": "cid=cid6340a351448462.00161898; bl_cid=blcid6340a352a168e9.58896560; PHPSESSID=86ea263492c0b6c4b095271c16e5e01d; grid=0",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1"
            }
            url = "https://www.coolstuffinc.com/ajax_buylist.php"

            # * Send request
            r = _send_request('POST', url, data=params, headers=headers)

            # * Parse response, pass response, writer, and set name
            scripts.csi(r, writer, set)
    imported_data.close()

# scrape_csi()
scrape_ck()
# for site in sites_to_scrape:
#     log.info(f'Running scrape for {site} ...')
#     if site == 'abu':
#         scrape_abu()
#     elif site == 'csi':
#         scrape_csi()
#     # ...
# log.info("Parsed all of the items!") # ? mmmm filler info, replace with something good maybe