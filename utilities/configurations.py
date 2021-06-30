import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

"""
def get_password():
    return "some password"


def get_username():
    return "some username"
"""