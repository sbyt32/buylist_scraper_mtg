import json

from scripts.misc.settings import SITES_TO_SCRAPE


def main():
    sets_info_location = f'data/set_information/sets_info.json'
    file_data = {}

    for site_name in SITES_TO_SCRAPE:
        file_data[site_name] = {}

        with open(f'data/{site_name}/set_name.txt', 'r') as set_name_file:
            set_names = set_name_file.readlines()

        for set_name in set_names:
            set_name = set_name.rstrip('\n')

            file_data[site_name][set_name] = {
                "normal": set_name,
                "tokens": set_name
            }

    with open(sets_info_location, 'w') as file:
        file.write(json.dumps(file_data, indent=4))


if __name__ == '__main__':
    main()
