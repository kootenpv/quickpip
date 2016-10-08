""""In this module we can define functions that will be imported in multiple modules"""
import os


def get_quickpip_path(path="~/.quickpip"):
    """
    Absolutely useless at the moment. Though it might indicate
    a nice place to store app neccessary files
    """
    return os.path.expanduser(path)
