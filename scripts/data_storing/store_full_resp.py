import arrow
import json
import logging
from urllib.parse import quote

log = logging.getLogger()
local = arrow.utcnow().to('US/Pacific')
local.format("MMM_DD_YY_HH_mm_ss").lower()

def store_response(r:dict, site:str, file:str):
    log.debug('Dumping response!')
    with open(f'sample/{site}/{local.format("MMM_DD_YY_HH_mm_ss").lower()}_{file}.{file}', 'w', encoding='utf8') as store_data:
        json.dump(r, store_data, ensure_ascii=False, indent=4)
        store_data.close()