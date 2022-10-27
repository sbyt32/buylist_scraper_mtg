import requests
from scripts.data_storing.store_full_resp import store_response
from bs4 import BeautifulSoup

headers = { 
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
}

# # TODO: The error here is that it halts on a loading screen
def set_scrape():
    r = requests.get('https://abugames.com/buylist/singles', headers=headers)
    with open('sample_2.html', 'w', encoding='utf8') as testing:
        testing.write(r.text)
    # store_response(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    set_name = soup.select('div.filter-field:nth-child(3) span:nth-child(odd)')

    with open('data_2/abu.txt', 'w', encoding='utf8') as testing:
        for sets in set_name:
            testing.write(sets+'\n')


# def set_scrape():
#     session = requests.Session()
#     session.get('https://abugames.com/', headers=headers)
#     session.headers.update(headers)
#     r = session.get('https://abugames.com/buylist/singles')
#     with open('sample_2.html', 'w', encoding='utf8') as testing:
#         testing.write(r.text)