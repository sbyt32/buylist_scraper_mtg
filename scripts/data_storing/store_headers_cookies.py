import arrow
import logging
log = logging.getLogger('Preordain')
local = arrow.utcnow().to('US/Pacific')

# DATA_STORE = [
#     'headers',  # * Storing the headers from the request is important, CK cares heavily about that stuff.
#     'cookies'   # * Some sites, like CK care about cookies. 
# ]

def store_headers_cookies(r, site:str):
    file_name = f'logs/error/{local.format("MMM_DD_YY_HH_mm_ss").lower()}_headers_cookies.txt'

    if logging.DEBUG == log.root.level:

        log.debug(f'Dumping headers and cookies to {file_name}')
        log.error(f'{site:4} | {file_name:20}')

        with open(file_name, 'w') as store_data:

            store_data.write('Headers\n')
            for x in r.headers.items():
                store_data.write(' '.join(str(s) for s in x) + '\n')

            store_data.write('\nCookies\n')
            for x in r.cookies.items():
                store_data.write(' '.join(str(s) for s in x) + '\n')

        store_data.close()