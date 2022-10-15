import json


with open('./sample/scryfall/scryfall_bulk.json', encoding="utf8") as scryfallCards:
    r = json.load(scryfallCards)
    for x in r[:10]:
        print(x['name'])


# cardBuylistInfo = [
#     "name",     # Name
#     "card_num"  # Collector Number
#     "set",      # Set
#     "foil",     # Foil Property
#     "usd",      # Buylist Price, in USD
#     "credit"    # Buylist Price, in store credit (if supported)
# ]