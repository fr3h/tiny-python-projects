#!/usr/bin/python
"""
Author : Alfredo Vilagut Garcia <alfredovilagutgarcia@gmail.com>
Date   : 15/07/2022
Purpose: Twelve days of Christmas
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='day',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if 1 > args.num or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def verse(day):
    """Create a verse"""

    ordinal = {
        1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth',
        7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth'
    }

    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,'
    ]

    lines = [
        f'On the {ordinal[day]} day of Christmas,',
        'My true love gave to me,'
    ]

    lines.extend(reversed(gifts[:day]))

    if day > 1:
        lines[-1] = 'And ' + lines[-1].lower()

    return '\n'.join(lines)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    verses = [verse(day) for day in range(1, args.num + 1)]
    print('\n\n'.join(verses), file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
