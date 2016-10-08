""" This file is for Python 2/3 compatability. We can now import "get_input" """
try:
    get_input = raw_input
except NameError:
    get_input = input
