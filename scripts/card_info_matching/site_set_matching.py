import json
import os
from scripts.misc.settings import SITES_TO_SCRAPE

for site_names in SITES_TO_SCRAPE:

    with open(f'data/{site_names}/set_name.txt', 'r') as set_name_file:
        set_names = set_name_file.readlines()
        set_name_file.close()

    sets_info_location = f'data/set_information/sets_info.json'        


    # ! If sets_info.json is an empty file, it will return an empty file!
    if not os.path.exists(sets_info_location):
        open(sets_info_location, 'w').write('{}')
    
    with open(sets_info_location) as sets_create:
        set_create_stuff = json.load(sets_create)
        sets_create.close()

    with open(sets_info_location, 'w') as sets_create_2:

            set_create_stuff[site_names] = {}
            sets_create_2.write(json.dumps(set_create_stuff))

    with open(sets_info_location) as file:
        file_data:dict = json.load(file)
        file.close()

    for sets in set_names:
        sets = sets.rstrip('\n')
        set_name_on_site = {
            "normal": f"{sets}",
            "tokens": f"{sets}"
        }

        file_data[site_names][f"{sets}"] = set_name_on_site

        with open(sets_info_location, 'w') as file:
            file.write(json.dumps(file_data, indent=4))




