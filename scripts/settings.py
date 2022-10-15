import logging
import arrow

SITES_TO_SCRAPE = [
    'abu',  # ABUGames.com
    'csi',  # CoolStuffInc.com
    'ck'    # CardKingdom.com
    # ...
]

CARD_BUYLIST_INFO = [
    "name",     # Name
    "card_num"  # Collector Number (if supported, ABU Specific)
    "set",      # Set
    "foil",     # Foil Property
    "usd",      # Buylist Price, in USD
    "credit"    # Buylist Price, in store credit (if supported)
]


local = arrow.utcnow().to('US/Pacific')
# print(local.format('MMM-DD-YY').lower())

BASIC_FORMAT =   "%(asctime)s | %(levelname)-8s | %(filename)-20s | %(lineno)-8s | %(message)s"
logging.basicConfig(filename=f'logs/{local.format("MMM_DD_YY").lower()}.log',format=BASIC_FORMAT)