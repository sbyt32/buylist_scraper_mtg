import requests
import logging
import json
import scripts
logging.basicConfig()
log = logging.getLogger()

def _send_request(method:str, url:str, **kwargs) -> dict:
    """
    Catch all wrapper for sending web request and interpreting as json
    """

    log.info(f"Sending request to {url} with args {kwargs}")
    r = requests.request(method, url, **kwargs)
    # basic error checking
    if not r.ok:
        log.error(f"Request had error! HTTP {r.status_code}, dumping headers and cookies if debugging.")
        scripts.data_store_headers_cookies(r, url)

    # Try to decode response
    data = {}
    try:
        data = json.loads(r.text)
    except json.JSONDecodeError as e:
        log.exception(f"Failed to decode response as json, was there an error in request?: {e}")
    return data