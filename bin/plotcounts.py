"""Plot word counts."""

import argparse
import pandas as pd

USAGE = "plotcounts.py [-h] csv [--outfile filename]"
def main(args):
    """Run the program."""
    df = pd.read_csv(args.infile, header=None, names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False, method='max')
    df['inverse_rank'] = 1 / df['rank']
    scatplot = df.plot.scatter(x='word_frequency', y='inverse_rank', figsize=[12, 6], grid=True)
    fig = scatplot.get_figure()
    fig.savefig(args.outfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Word count csv')
    parser.add_argument('-o', '--outfile', type=str,default='plotcounts.png', help='Output file name')
    parser.add_argument('--xlim', type=float, nargs=2,metavar=('XMIN','XMAX'), default=None, help='X axis bound')   
    args = parser.parse_args()
    main(args)
