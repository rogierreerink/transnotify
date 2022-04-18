from cache.cache import Cache
from log.log import Log, Level
from torrents.torrents import Torrents
from scanner.scanners.opensubtitles import OpenSubtitles
from globals import setGlobal, getGlobal

import argparse
import pathlib


def parseArgs() -> dict:
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', metavar='completed', required=True,
                        help='Path to the completed downloads.',
                        type=pathlib.Path)

    parser.add_argument('-m', metavar='movies', required=True,
                        help='Destination path for movies.',
                        type=pathlib.Path)

    parser.add_argument('-s', metavar='series', required=True,
                        help='Destination path for tv series.',
                        type=pathlib.Path)

    parser.add_argument('-o', metavar='owner',  # required=True,
                        help='Specify the owner of the moved items.',
                        type=pathlib.Path)

    parser.add_argument('--logs', metavar='logs', required=True,
                        help='Specify the log directory.',
                        type=pathlib.Path)

    parser.add_argument('--cache', metavar='cache', required=True,
                        help='Specify the cache directory.',
                        type=pathlib.Path)

    return vars(parser.parse_args())


def initialize() -> None:
    """
    Initialize globals.
    """
    args = parseArgs()

    setGlobal('cache', Cache(args['cache']))
    setGlobal('log', Log(args['logs']))
    setGlobal('completed_dir', args['c'])

    getGlobal('log').write(
        Level.DEBUG, 'Progam initialized.')


if __name__ == '__main__':
    """
    Execute the program.
    """
    initialize()

    torrents = Torrents()
    print(torrents.listNewCompleted())

    scanner = OpenSubtitles()
    print([x.title for x in scanner.scan(
        'The.Adam.Project.2022.1080p.NF.WEB-DL.DDP5.1.Atmos.HEVC-CMRG[TGx]')])
    print([x.title for x in scanner.scan(
        'Young.Sheldon.S05E17.1080p.WEB.h264-GOSSIP[eztv.re].mkv')])
