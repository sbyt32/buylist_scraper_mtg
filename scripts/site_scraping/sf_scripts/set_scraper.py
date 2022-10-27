import scripts
from operator import itemgetter

def parse_sets(set_name):
    with open('data/set_information/sets_to_exclude.txt') as sets_to_exclude_file:
        sets_to_exclude = sets_to_exclude_file.read().splitlines()
        sets_to_exclude_file.close()
    if set_name in sets_to_exclude:
        return
    else:
        return set_name

def set_name_scraper():
    r = scripts._send_request('GET', 'https://api.scryfall.com/sets')['data']
    r = sorted(r, key=itemgetter('name'))

    with open('data/scryfall/sets_to_fetch.txt', 'w', encoding='utf8') as set_names:
        for set in r:
            if set['digital'] == False:
                if parse_sets(set['name']) == set['name']:
                    set_names.write(set['name']+'\n')
        set_names.close()