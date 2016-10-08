""" When we want to create a package that also has a CLI
Then it is usually a good idea to separate the logic into it's own file: __main__
"""
from quickpip import print_version
from quickpip import run


def get_args_parser():
    import argparse
    from argparse import RawTextHelpFormatter
    desc = 'Here we explain what the tool `quickpip` does.'
    p = argparse.ArgumentParser(description=desc, formatter_class=RawTextHelpFormatter)
    p.add_argument('--version', '-v', action='version', version=print_version())
    subparsers = p.add_subparsers(dest="command")
    subparsers.add_parser('run')
    return p


def main():
    parser = get_args_parser()
    args = parser.parse_args()
    if args.command == "run":
        run()
    else:
        parser.print_help()
        parser.exit(1)

if __name__ == "__main__":
    main()
