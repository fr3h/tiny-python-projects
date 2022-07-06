#!/usr/bin/python
"""
Author : Alfredo Vilagut Garcia <alfredovilagutgarcia@gmail.com>
Date   : 28/06/2022
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sort',
                        action='store_true',
                        help='Sort the items (Default: False)')

    parser.add_argument('-c',
                        '--comma',
                        action='store_true',
                        help='Use Oxford comma (Default: True)')

    parser.add_argument('-cs',
                        '--separator',
                        help='Character that separates items of the list',
                        metavar='separator',
                        type=str,
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def make_picnic_list(items, sort, delete_comma, separator):
    """Design the string with the items of the picnic list"""

    if sort:
        items.sort()

    if len(items) == 1:
        return items[0]

    if len(items) == 2:
        return items[0] + ' and ' + items[1]

    bringing = f'{separator} '.join(items[:-1])

    if delete_comma:
        return bringing + ' and ' + items[-1]
    else:
        return bringing + f'{separator} and ' + items[-1]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print('You are bringing ' + make_picnic_list(args.items, args.sort, args.comma, args.separator) + '.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
