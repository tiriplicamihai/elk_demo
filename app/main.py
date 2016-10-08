import logging
from logging.config import dictConfig
from random import choice, randint
import time

logger = logging.getLogger()

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file_handler': {
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/app.log',
            'formatter': 'standard',
            'maxBytes': 1024,
        }
    },
    'loggers': {
        '': {
            'handlers': ['file_handler'],
            'level': 'INFO',
            'propagate': True
        },
    }
}


def main():
    count = 30000

    ENDPOINTS = ["/posts", '/user', '/like', '/comment']
    METHODS_AND_RESPONSES = [
        ("GET", [200, 401, 500, 404]),
        ("POST", [201, 400, 500]),
        ("DELETE", [204, 401, 500])
    ]

    USER_IDS = [12345, 2456, 12556]


    while count > 0:
        endpoint = choice(ENDPOINTS)
        method, responses = choice(METHODS_AND_RESPONSES)
        response = choice(responses)
        request_time = randint(100, 1200)
        user_id = choice(USER_IDS)
        logger.info('USER: %d, ENDPOINT: %s, METHOD: %s, RC: %d, RT: %d',
                     user_id, endpoint, method, response, request_time)
        count -= 1

        time.sleep(randint(1, 5))

def setup_logging():
    dictConfig(LOGGING_CONFIG)

if __name__ == '__main__':
    setup_logging()
    main()
