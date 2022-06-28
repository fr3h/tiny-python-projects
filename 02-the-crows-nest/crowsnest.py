#!/usr/bin/python
"""
Author : Alfredo Vilagut Garcia <alfredovilagutgarcia@gmail.com>
Date   : 27/06/2022
Purpose: Crow's Nest -- choose the correct article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    parser.add_argument('-s',
                        '--side',
                        help='Choose the side of the boat',
                        metavar='side',
                        type=str,
                        default='larboard')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = args.side
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    article = article if word[0].islower() else article.capitalize()
    print(f'Ahoy, Captain, {article} {word} off the {side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()