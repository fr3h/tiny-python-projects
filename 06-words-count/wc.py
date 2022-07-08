#!/usr/bin/python
"""
Author : Alfredo Vilagut Garcia <alfredovilagutgarcia@gmail.com>
Date   : 05/07/2022
Purpose: Python version of the word count program
"""

import argparse


# --------------------------------------------------
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    parser.add_argument('-l',
                        action='store_true',
                        help='Show column lines (default: false)')

    parser.add_argument('-w',
                        action='store_true',
                        help='Show column words (default: false)')

    parser.add_argument('-b',
                        action='store_true',
                        help='Show column bytes (default: false)')

    return parser.parse_args()


# --------------------------------------------------
def print_resume(args, num_lines, num_words, num_bytes, name):
    if args.l or args.w or args.b:
        if args.l:
            print(f'{num_lines:8}', end='')
        if args.w:
            print(f'{num_words:8}', end='')
        if args.b:
            print(f'{num_bytes:8}', end='')
        print(f' {name}')
    else:
        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {name}')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines, total_words, total_bytes = 0, 0, 0

    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0

        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)

        print_resume(args, num_lines, num_words, num_bytes, fh.name)

        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes

    if len(args.file) > 1:
        print_resume(args, total_lines, total_words, total_bytes, 'total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
