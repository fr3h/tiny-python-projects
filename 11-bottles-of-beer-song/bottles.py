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

    parser.add_argument('-s',
                        '--step',
                        help='Allows the user to skip numbers',
                        metavar='int',
                        type=int,
                        default=1)

    parser.add_argument('-r',
                        '--reverse',
                        help='Reverse the order of the verses',
                        action='store_true')

    parser.add_argument('-t',
                        '--text',
                        help='Replace the Arabic numbers (1,2,3) with text (one, two, three)',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    if args.step < 1 or args.step > args.num:
        parser.error(f'--step "{args.step}" must be between 1 and the numbers of bottles --num "{args.num}"')

    return args


num_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'four', 5: 'five'}


# --------------------------------------------------
def get_bottles(num, reverse, step):
    """Get the actual and next bottle"""

    if reverse:
        return num, num+step
    else:
        return num, num-step


# --------------------------------------------------
def verse(num_bottle, num_next_bottle, text):
    """Sing a verse"""

    bottle = "bottles" if num_bottle != 1 else "bottle"
    next_bottle = "bottles" if num_next_bottle != 1 else "bottle"

    print(f'{num_dict.get(num_bottle) if text else num_bottle} {bottle} of beer on the wall,')
    print(f'{num_dict.get(num_bottle) if text else num_bottle} {bottle} of beer,\nTake one down, pass it around,')
    if num_next_bottle >= 1:
        print(f'{num_dict.get(num_next_bottle) if text else num_next_bottle} {next_bottle} of beer on the wall!\n')
    else:
        print('No more bottles of beer on the wall!')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    num = 1 if args.reverse else args.num
    i = 0

    while i < args.num:
        bottles = get_bottles(num, args.reverse, args.step)
        verse(bottles[0], bottles[1], args.text)
        num = bottles[1]
        i += args.step


# --------------------------------------------------
if __name__ == '__main__':
    main()
