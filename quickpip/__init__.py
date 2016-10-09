""" You can kind of see this as the scope of `quickpip` when you 'import quickpip'
The following functions become available:
quickpip.__project__
quickpip.__version__
quickpip.run
quickpip.print_version
"""
import sys

__project__ = "quickpip"
__version__ = "0.0.4"

from .quickpip import run


def print_version():
    """ Convenient function for printing the version of the package """
    sv = sys.version_info
    py_version = "{}.{}.{}".format(sv.major, sv.minor, sv.micro)
    version_parts = __version__.split(".")
    s = "{} version: [{}], Python {}".format(__project__, __version__, py_version)
    s += "\nMajor version: {}  (breaking changes)".format(version_parts[0])
    s += "\nMinor version: {}  (extra feature)".format(version_parts[1])
    s += "\nMicro version: {} (commit count)".format(version_parts[2])
    return s
