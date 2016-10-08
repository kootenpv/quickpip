from .utils import get_quickpip_path
from .compat import get_input


def run(number=None):
    print("I might store some data here: {} (not really)".format(get_quickpip_path()))
    if number is None:
        while True:
            try:
                number = int(get_input("Might I get your number? "))
                break
            except ValueError:
                print("A number please")
    print("I got {} as input.".format(number))
    result = number * 2
    print("I will return your number {} multiplied by 2 now ({})".format(number, result))
    return result
