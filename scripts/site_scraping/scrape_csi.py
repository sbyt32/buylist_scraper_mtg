import scripts
import scripts.misc.settings as settings
import scripts.site_scraping.csi_scripts
import csv
import logging
from urllib.parse import quote

log = logging.getLogger()

def scrape_csi():
    sets = scripts.misc_create_define_sets('csi')

    with open('./data/csi/script.csv', 'w', newline='') as imported_data:
        writer = csv.writer(imported_data, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(settings.CARD_BUYLIST_INFO)
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
            data = scripts._send_request('POST', url, data=params, headers=headers)
            # * Store the Headers and Cookies, if needed
            # * Parse response, pass response, writer, and set name
            scripts.site_scraping.csi_scripts.csi_store_cards(data,writer,set)
    imported_data.close()