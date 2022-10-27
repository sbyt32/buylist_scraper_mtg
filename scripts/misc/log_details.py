import arrow
import logging
import logging.config
local = arrow.utcnow().to('US/Pacific')

LOGGER_NAME = 'Ponder' # ? Filler name
BASIC_FORMAT =   "%(asctime)s | %(levelname)-8s | %(filename)-20s | %(message)s"
CONSOLE_FORMAT = "%(asctime)s | %(levelname)-8s | %(filename)-20s | %(message)s"
FILE_FORMAT =    "%(asctime)s | %(levelname)-8s | %(filename)-20s | %(message)s"
ERROR_FORMAT =   "%(asctime)s | %(levelname)-8s | %(pathname)-20s | %(lineno)-8s | %(message)s"


ERROR_FORMAT_COOKIE = "%(asctime)s | %(levelname)-8s | %(message)s | "

log_file_info   = f"logs/{local.format('MMM_DD_YY').lower()}.log"
log_file_debug  = f"logs/debug/{local.format('MMM_DD_YY').lower()}.log"
log_file_error  = f"logs/error/{local.format('MMM_DD_YY_hh_mm_a').lower()}.log"


def log_setup():
    log_config = {
        'name': LOGGER_NAME,
        "version": 1,
        'formatters': {
            'console_format': {
                'format': CONSOLE_FORMAT
            },
            'file_format': {
                'format': FILE_FORMAT
            },
            'file_format_error': {
                'format': ERROR_FORMAT
            },
            'file_format_error_cookie':{
                'format': ERROR_FORMAT_COOKIE
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': logging.INFO,
                'formatter': 'console_format',
            },
            'file_info': {
                'class': 'logging.FileHandler',
                'level': logging.INFO,
                'formatter': 'file_format',
                'filename': log_file_info,
            },
            'file_debug': {
                'class': 'logging.FileHandler',
                'level': logging.DEBUG,
                'formatter': 'file_format',
                'filename': log_file_debug,
            },
            'file_error': {
                'class': 'logging.FileHandler',
                'level': logging.ERROR,
                'formatter': 'file_format_error',
                'filename': log_file_error,
            },
            'file_error_cookie': {
                'class': 'logging.FileHandler',
                'level': logging.ERROR,
                'formatter': 'file_format_error_cookie',
                'filename': log_file_error,

            }
        },
        'root': {
            'level': logging.DEBUG,
            'propogate': True,
            'handlers': [
                'console',
                'file_info',
                'file_debug',
                'file_error'
            ]
        },
        'loggers': {
            LOGGER_NAME: {
                'level': logging.INFO,
                'propogate': True,
                'handlers': [
                    'console',
                    'file_info',
                    'file_debug',
                    'file_error'
                ],
            },
            'Preordain': {
                'level': logging.DEBUG,
                'propogate': False,
                'handlers': [
                    'console',
                    'file_info',
                    'file_debug',
                    'file_error_cookie'
                ],
            }
        }
    }

    logging.config.dictConfig(log_config)
    # logging.getLogger()
#     logging
# logging.getLogger(LOGGER_NAME)
# logging.basicConfig(filename=f'logs/{local.format("MMM_DD_YY").lower()}.log',format=BASIC_FORMAT)

# log = logging.getLogger(LOGGER_NAME)

# log.debug('log level debug')
# log.info('log level info')
# log.warning('log level warning')
# log.error('log level error')


# in another file
# log_other = logging.getLogger()
# same config as `log`
# local.format('MMM_DD_YY')