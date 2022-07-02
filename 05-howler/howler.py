#!/usr/bin/python
"""
Author : Alfredo Vilagut Garcia <alfredovilagutgarcia@gmail.com>
Date   : today
Purpose: Howler (upper-cases input)
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('--ee',
                        action='store_true',
                        help='Set output to lowercase (Default: False)')

    return parser.parse_args()


# --------------------------------------------------
def read_file(file):
    in_fh = open(file)
    content = in_fh.read().rstrip()
    in_fh.close()
    return content


# --------------------------------------------------
def write_file(file, text, lc):
    out_fh = open(file, 'wt')
    if lc:
        out_fh.write(text.lower())
    else:
        out_fh.write(text.upper())
    out_fh.close()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    lc = args.ee
    if os.path.isfile(text):
        text = read_file(text)

    if args.outfile:
        write_file(args.outfile, text, lc)
    elif lc:
        print(text.lower())
    else:
        print(text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
