from pathlib import Path

BASE_DIR = Path(__name__).parent


LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "bot.log"

DT_FORMAT = "%d.%m.%Y %H:%M:%S"
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default_formatter": {"format": LOG_FORMAT, "datefmt": DT_FORMAT}
    },
    "handlers": {
        "stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "default_formatter",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default_formatter",
            "filename": LOG_FILE,
            "maxBytes": 10**6,
            "backupCount": 5,
        },
    },
    "loggers": {
        "bot": {
            "handlers": ["stream_handler", "file"],
            "level": "INFO",
            "propagate": True,
        }
    },
}
