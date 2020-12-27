import configparser
from gevent import os


def get_con(title, key):
    """

    :param title:
    :param key:
    :return:
    """
    config = configparser.ConfigParser()
    os.path.da