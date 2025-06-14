import json

from . import config


def load_data():
    if config.DATA_FILE.exists():
        with open(config.DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    if not config.DATA_FILE.exists():
         config.DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(config.DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
