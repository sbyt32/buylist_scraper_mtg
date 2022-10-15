from scripts.scrape_abu import store_data as abu
from scripts.scrape_csi import store_data as csi
# ? Can this be done more efficently?
from scripts.scrape_ck import get_cookies_header as ck_cookies_header
from scripts.scrape_ck import request_data as ck_request_data
from scripts.scrape_ck import parse_cards as ck_parse_data
from scripts.scrape_ck import next_page as ck_next
from scripts.scrape_ck import collapse_requests as ck_close

# TODO: Add the ability to cache as a separate script
# ? Headers, Cookies, and the .json / file itself.
# from scripts.data_storing.store_headers import test