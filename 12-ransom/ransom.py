#!/usr/bin/python
"""
Author : Alfredo Vilagut Garcia <alfredovilagutgarcia@gmail.com>
Date   : 14/07/2022
Purpose: Ransom Note
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = read_file(args.text)

    return args


# --------------------------------------------------
def read_file(file):
    in_fh = open(file)
    content = in_fh.read().rstrip()
    in_fh.close()
    return content


# --------------------------------------------------
def choose(char):
    """Randomly choose an upper or lowercase letter to return"""

    return random.choice([char.lower(), char.upper()])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    print(''.join(choose(char) for char in args.text))
    # print(''.join(map(choose, args.text)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
