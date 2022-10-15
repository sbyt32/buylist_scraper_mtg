import logging
import logging
log = logging.getLogger()

def request_data(set:str, page:int, session):
    set = set.replace(" - ", " ").replace(" ", "-").lower().rstrip('\n')
    log.debug(f'Grabbing the set: {set}')
    queryString = {
        "filter[sort]":"name_asc",
        "filter[search]":"mtg_advanced",
        "filter[edition]":f"{set}",
        "filter[foils]":"1",
        "filter[singles]":"1",
        "page":f"{page}"
    }

    log.debug(f'Sending request.get to https://www.cardkingdom.com/purchasing/mtg_singles with params:\n{queryString}')
    r = session.get('https://www.cardkingdom.com/purchasing/mtg_singles', params=queryString)

    # ? I have to clear this because I need to be able to make sure this cookie doesn't get huge
    session.cookies.clear('www.cardkingdom.com', '/', 'sigt')
    
    return r