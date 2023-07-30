import os
from datetime import datetime

BASE_DIR = os.path.abspath("../")
APP_LOG_FILE_PATH = os.path.join(BASE_DIR, "logs/")

if not os.path.exists(APP_LOG_FILE_PATH):
    os.makedirs(APP_LOG_FILE_PATH)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        "console": {
            "()": "colorlog.ColoredFormatter",
            "format": '{asctime} {levelname} {funcName} {message}',
            "style": '{',
            "log_colors": {
                "DEBUG": "blue",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        }
    },
    'loggers': {
        'normal': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
