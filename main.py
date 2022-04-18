from cache.cache import Cache
from fileman.fileman import Fileman
from log.log import Log, Level
from torrents.torrents import Torrents
from scanner.scanners.opensubtitles import OpenSubtitles
from analyzer.analyzer import Analyzer
from scanner.type import Type
from globals import setGlobal, getGlobal

import argparse
import pathlib
import os


def parseArgs() -> dict:
    """
    Parse command line arguments.
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

    setGlobal('completed_dir', args['c'])
    setGlobal('movies_dir', args['m'])
    setGlobal('series_dir', args['s'])
    setGlobal('cache', Cache(args['cache']))
    setGlobal('log', Log(args['logs']))


def execute() -> None:
    """
    Run the main program.
    """
    analyzer = Analyzer()
    analyzer.registerScanner(OpenSubtitles)

    torrents = Torrents()
    for filename in torrents.listNewlyCompleted():
        filepath = os.path.join(getGlobal('completed_dir'), filename)

        analysis = analyzer.analyze(filepath)
        if analysis.result.t == Type.MOVIE:
            Fileman.copy(filepath, getGlobal('movies_dir'))
            torrents.markHandled(filename)
            getGlobal('log').write(
                Level.DEBUG, f'\'{filename}\' copied to movies directory.')

        elif analysis.result.t == Type.SERIES:
            Fileman.copy(filepath, getGlobal('series_dir'))
            torrents.markHandled(filename)
            getGlobal('log').write(
                Level.DEBUG, f'\'{filename}\' copied to series directory.')

        else:
            getGlobal('log').write(
                Level.DEBUG, f'\'{filename}\' unhandled (unknown type).')


if __name__ == '__main__':
    """
    Execute the program.
    """
    initialize()
    execute()
