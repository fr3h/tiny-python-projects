#!/usr/bin/python
"""
Author : Alfredo Vilagut Garcia <alfredovilagutgarcia@gmail.com>
Date   : 06/07/2022
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)',
                        type=str)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def store_lines(file):
    """Store the lines from a file"""
    lines_dict = dict()
    for line in file:
        lines_dict[line[0].upper()] = line.rstrip()
    return lines_dict


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    lines_dict = store_lines(args.file)
    for letter in args.letter:
        if letter.upper() in lines_dict:
            print(lines_dict.get(letter.upper()), end='')
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
