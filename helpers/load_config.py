import configparser

CONFIG_FILE = "config.ini"


def load_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    return config
