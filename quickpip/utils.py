import os


def get_quickpip_path(path="~/.quickpip"):
    return os.path.expanduser(path)
