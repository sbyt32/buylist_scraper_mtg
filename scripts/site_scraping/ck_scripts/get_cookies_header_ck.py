
import logging
log = logging.getLogger()

headers = { 
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
}

cookies = {
    "limit": "100",
    "sortBy": "name_asc"
}

def get_cookies_header(session):
    r = session.get('https://www.cardkingdom.com/purchasing/mtg_singles', headers=headers, cookies=cookies)
    if not r.ok: # ? This may need to be changed based on if the error gives back something involving bad (robot) user-agent
        log.error(f"Request had error! HTTP {r.status_code}") 
    session.headers.update(headers)
    session.cookies.update(cookies)
    return r