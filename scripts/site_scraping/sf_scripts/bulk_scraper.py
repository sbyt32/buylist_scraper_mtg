import json
import os
import requests
import scripts
import logging

log = logging.getLogger()

def bulk_scrape():
    bulk_data_all = scripts._send_request('GET', 'https://api.scryfall.com/bulk-data')
    bulk_data_default = scripts._send_request('GET',bulk_data_all['data'][2]['download_uri'])
    with open('data/scryfall/scryfall_bulk.json', 'w') as scryfall_bulk:
        scryfall_bulk.write(json.dumps(bulk_data_default, indent=2))

    