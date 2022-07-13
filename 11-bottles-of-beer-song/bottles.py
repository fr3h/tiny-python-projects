#!/usr/bin/python
"""
Author : Alfredo Vilagut Garcia <alfredovilagutgarcia@gmail.com>
Date   : 13/07/2022
Purpose: Bottles of beer song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def verse(num):
    """Sing a verse"""
    verse_1 = "of beer on the wall,"
    verse_2 = "of beer,\nTake one down, pass it around,"
    if num != 1:
        print(f'{num} bottles {verse_1}')
        print(f'{num} bottles {verse_2}')
        if num != 2:
            print(f'{num - 1} bottles of beer on the wall!\n')
        else:
            print(f'{num - 1} bottle of beer on the wall!\n')
    else:
        print(f'{num} bottle {verse_1}')
        print(f'{num} bottle {verse_2}')
        print('No more bottles of beer on the wall!')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for bottle in range(args.num, 0, -1):
        verse(bottle)


# --------------------------------------------------
if __name__ == '__main__':
    main()
