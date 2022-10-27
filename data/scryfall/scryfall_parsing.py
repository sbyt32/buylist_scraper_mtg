import json
import csv


with open('./sample/scryfall/scryfall_bulk.json', encoding="utf8") as scryfall_bulk:
    r = json.load(scryfall_bulk)
    scryfall_bulk.close()


with open('data/scryfall/all_card_database.csv', 'w', encoding='utf8', newline='') as all_cards:
    writer = csv.writer(all_cards, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['name', 'card_num', 'set', 'set_full', 'style'])
    for x in r:
        if 'paper'  in x['games']:
            # declarer for card styles
            card_style = ''

            # * Card Name
            card_name:str = x['name']
            # Collector Number
            card_num:str = x['collector_number']
            #  Set
            card_set:str = x['set']
            # Full Set Name
            card_set_full:str = x['set_name']

            if card_num.endswith('p'):
                card_style = 'pw-stamp'
            elif card_num.endswith('s'):
                card_style = 'prerelease'

            # card_num:int = re.sub('[★ps]', '', card_num)

            if 'promo_types' in x:
                if 'boosterfun' in x['promo_types']:
                    if x['border_color'] == 'borderless':
                        card_style = 'borderless'
                    
                    elif 'showcase' in x['promo_types']:
                        card_style = 'showcase'

                    elif 'galaxyfoil' in x['promo_types']:
                        card_style = 'galaxy_foil'

                    elif x['frame'] == '1997':
                        card_style = 'retro'

                    elif x['full_art'] == True:
                        card_style = 'full_art'

                    elif 'extendedart' in x['frame_effects']:
                        card_style = 'extended'

            writer.writerow([card_name, card_num, card_set, card_set_full ,card_style])
    all_cards.close()


# cardBuylistInfo = [
#     "name",     # Name
#     "card_num"  # Collector Number
#     "set",      # Set
#     "foil",     # Foil Property
#     "usd",      # Buylist Price, in USD
#     "credit"    # Buylist Price, in store credit (if supported)
# ]

