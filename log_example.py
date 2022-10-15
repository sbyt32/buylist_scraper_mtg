import logging
import arrow
local = arrow.utcnow().to('US/Pacific')
# print(local.format('MMM-DD-YY').lower())
# from attrs import define

# @define
# class logFormat:
BASIC_FORMAT =   "%(asctime)s | %(levelname)-8s | %(filename)-20s | %(lineno)-8s | %(message)s"
logging.basicConfig(filename=f'logs/{local.format("MMM_DD_YY").lower()}.log',format=BASIC_FORMAT)

log = logging.getLogger()

# log.debug('log level debug')
# log.info('log level info')
# log.warning('log level warning')
# log.error('log level error')


# in another file
# log_other = logging.getLogger()
# same config as `log`
# local.format('MMM_DD_YY')