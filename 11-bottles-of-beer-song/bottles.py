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
        parser.error(f'--step "{args.step}" must be between 1 and the numbers of bottles "{args.num}"')

    return args


num_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'four', 5: 'five'}


# --------------------------------------------------
def get_bottles(num, reverse, step):
    """Get the actual and next bottle"""

    if reverse:
        return num, num+step, num+step
    else:
        return num, num-step, num-step


# --------------------------------------------------
def verse(bottle, next_bottle, text):
    """Sing a verse"""

    verse_1 = "of beer on the wall,"
    verse_2 = "of beer,\nTake one down, pass it around,"

    if bottle > 1:
        print(f'{num_dict.get(bottle) if text else bottle} bottles {verse_1}')
        print(f'{num_dict.get(bottle) if text else bottle} bottles {verse_2}')
        if next_bottle > 1:
            print(f'{num_dict.get(next_bottle) if text else next_bottle} bottles of beer on the wall!\n')
        elif next_bottle == 1:
            print(f'{num_dict.get(next_bottle) if text else next_bottle} bottle of beer on the wall!\n')
        else:
            print('No more bottles of beer on the wall!')
    else:
        print(f'{num_dict.get(bottle) if text else bottle} bottle {verse_1}')
        print(f'{num_dict.get(bottle) if text else bottle} bottle {verse_2}')
        if next_bottle > 1:
            print(f'{num_dict.get(next_bottle) if text else next_bottle} bottles of beer on the wall!\n')
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
        num = bottles[2]
        i += args.step


# --------------------------------------------------
if __name__ == '__main__':
    main()
