"""
Count the occurrences of all words in a text
and output them in CSV format.
"""

import re
import argparse
import string
from collections import Counter

import utilities as util

def clean_word(word):
    word = word.strip(string.punctuation)
    word = word.translate(str.maketrans('', '', string.punctuation))
    word = word.translate(str.maketrans({'\u2018': "", '\u2019': "", '\u201C': "", '\u201D': "", '\u2014': "", '\uFEFF': "", '\u2026': "", '\u00A3': ""}))
    word = re.sub("^\\d","X",word) 
    return word

def count_words(reader):
    """Count the occurrence of each word in a string."""
    text = reader.read()
    chunks = text.split()
#    npunc = [word.strip(string.punctuation) for word in chunks]
    npunc = [clean_word(word) for word in chunks]
    word_list = [word.lower() for word in npunc if word]
    word_counts = Counter(word_list)
    return word_counts


def main(args):
    """Run the command line program."""
    word_counts = count_words(args.infile)
    util.collection_to_csv(word_counts, num=args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    parser.add_argument('-n', '--num',
                        type=int, default=None,
                        help='Output n most frequent words')
    args = parser.parse_args()
    main(args)
