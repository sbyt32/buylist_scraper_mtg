import csv
import logging
import scripts
import scripts.misc.settings as settings
log = logging.getLogger()


def scrape_abu():
    # *Locate the sets, first. 
    sets = scripts.misc_create_define_sets('abu')

    with open('data/abu/script.csv', 'w', newline='') as imported_data:
        writer = csv.writer(imported_data, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(settings.CARD_BUYLIST_INFO)
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
            data = scripts._send_request('GET', url, params=params)
            # * Process response
            # * Check if empty.
            if data['grouped']['product_id']['groups'] == []:
                log.error(f'The set "{set}" does not work or has no data!')
                continue
            break
            # scripts.abu(r,writer)
            # scripts.abu_store_data(data, writer)
            
    imported_data.close()