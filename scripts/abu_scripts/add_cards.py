import logging

def store_data(abu_data, writer):
    # Process response

    for cardInfo in abu_data['grouped']['product_id']['groups']:
        # This grabs the section that each card has it's buylisting and identification.

        cardInfo = cardInfo['doclist']['docs'][0]
        # ? If the card is foil, use the same format as coolstuffinc
        if 'Foil' in cardInfo['card_style']:
            foil = "yes"
        else:
            foil = "no"
        # ? Some older sets don't have card_numbers, but scryfall does. We can transform this data later, maybe?
        try:
            card_num = cardInfo['card_number']
        except KeyError:
            card_num = ""

        # This should be a csv.writer.
        writer.writerow([cardInfo['simple_title'], card_num, cardInfo['magic_edition_sort'], foil, cardInfo['buy_price'], cardInfo['trade_price']])