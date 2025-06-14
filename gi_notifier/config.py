from logging import getLogger
from logging.config import dictConfig
from pathlib import Path

BOTTOKEN = ""
TIMEZONE = "Asia/Kolkata"
HOURLIST = [iter for iter in range(24) if iter % 4 == 0]
DATA_FILE = Path("/tmp/gi-notifier/bot_user_data.json")  #noqa: S108

logrconf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(message)s",
            "datefmt": "[%Y-%m-%d %I:%M:%S %z]",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
}

dictConfig(logrconf)

logger = getLogger(__name__)
