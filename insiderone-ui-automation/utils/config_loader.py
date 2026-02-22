"""Load configuration from config.json. URLs and environment settings only."""
import json
import os

_CONFIG = None
_CONFIG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config")


def get_config():
    """Load and return config dict (cached)."""
    global _CONFIG
    if _CONFIG is None:
        path = os.path.join(_CONFIG_DIR, "config.json")
        with open(path, encoding="utf-8") as f:
            _CONFIG = json.load(f)
    return _CONFIG


def get_base_url():
    return get_config()["base_url"]


def get_qa_careers_url():
    return get_config()["qa_careers_url"]


def get_browser():
    """Browser for tests: 'chrome' or 'firefox' (default from config)."""
    return get_config().get("browser", "chrome").lower()
