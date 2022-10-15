import requests
import logging
import json

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
        log.error(f"Request had error! HTTP {r.status_code}")

    # Try to decode response
    data = {}
    try:
        data = json.loads(r.text)
    except json.JSONDecodeError as e:
        log.exception("Failed to decode response as json, was there an error in request?: {e}")

    return data


headers = {
    'user-agent': 'Mozilla 5.0/Chrome'  # Simple anti bot bypass
}
# cookies = CookeiJar(...)
# r = _send_request('GET', 'https://httpbin.org/get', headers=headers, cookies=cookies)
# print(r)

requests.se

    