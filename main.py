import cache
import log

import argparse
import pathlib


if __name__ == '__main__':
    """
    Execute the main program.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', metavar='completed',  # required=True,
                        help='Path to the completed downloads.',
                        type=argparse.FileType(pathlib.Path))

    parser.add_argument('-m', metavar='movies',  # required=True,
                        help='Destination path for movies.',
                        type=argparse.FileType(pathlib.Path))

    parser.add_argument('-s', metavar='series',  # required=True,
                        help='Destination path for tv series.',
                        type=argparse.FileType(pathlib.Path))

    parser.add_argument('-o', metavar='owner',  # required=True,
                        help='Specify the owner of the moved items.',
                        type=argparse.FileType(pathlib.Path))

    parser.add_argument('--logs', metavar='logs', required=True,
                        help='Specify the log directory.',
                        type=pathlib.Path)

    parser.add_argument('--cache', metavar='cache', required=True,
                        help='Specify the cache directory.',
                        type=pathlib.Path)

    args = vars(parser.parse_args())
    print(args)

    c = cache.Cache(args['cache'])
    l = log.Log(args['logs'])
