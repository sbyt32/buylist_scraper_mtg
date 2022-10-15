import os
import logging
log = logging.getLogger()

def create_and_define_sets(site):
    # * Create directory to hold data if not exist
    if not os.path.exists(f'data/{site}'):
        log.warning(f'Creating directory for {site}...')
        os.makedirs(f'data/{site}')
    # * Check if the set_name_{site}.txt exists, which contains the way the site organizes their cards.
    try:
        log.debug(f'Checking data/{site}/set_name.txt exists')
        setList = open(f'data/{site}/set_name.txt')
    except FileNotFoundError:
        # TODO: Create script that makes the directories? Adapt from older script.
        log.error(f'Directory "data/{site}/set_name.txt" does not exist! Create the file first by running this other script.')
        # ? Maybe check that, if above does not work, break something?
    else:
        log.info(f'Opening set folder for {site}...')
        # * Get the list of sets and close the file, then return it.
        sets = setList.readlines()
        setList.close()
        return sets[:5]
