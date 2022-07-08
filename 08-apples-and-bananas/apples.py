#!/usr/bin/python
"""
Author : Alfredo Vilagut Garcia <alfredovilagutgarcia@gmail.com>
Date   : 08/07/2022
Purpose: Replace the vowels
"""

import argparse


# --------------------------------------------------
import os


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute (default: a)',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    return parser.parse_args()


# --------------------------------------------------
def read_file(file):
    in_fh = open(file)
    content = in_fh.read().rstrip()
    in_fh.close()
    return content


# --------------------------------------------------
def replace_vowels(text, vowel):
    dictionary = {'a': vowel, 'e': vowel, 'i': vowel, 'o': vowel, 'u': vowel,
                  'A': vowel.upper(), 'E': vowel.upper(), 'I': vowel.upper(), 'O': vowel.upper(), 'U': vowel.upper()}
    text = text.translate(text.maketrans(dictionary))
    return text


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    if os.path.isfile(text):
        text = read_file(text)
    text = replace_vowels(text, args.vowel)
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
