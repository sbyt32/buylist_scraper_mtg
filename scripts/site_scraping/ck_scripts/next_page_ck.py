import logging
log = logging.getLogger()
def next_page(searching):
    log.debug('Checking if page has more results on another page')
    log.debug(searching)
    if searching is not None:
        # * Continue searching
        log.info('Going to the next page...')
        return True
    else:
        # * Stop Searching
        log.info('Set completed, going to the next set...')
        return False