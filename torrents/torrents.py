from cache.connector import Connector
from log.log import Level
from globals import getGlobal

from typing import List
import os


class Torrents:
    """
    An interface to the torrent directories.
    """

    def __init__(self) -> None:
        """
        Initialize the torrents API.
        """
        self.completedTorrentsCache = Connector(
            getGlobal('cache'), 'completed_torrents')

    def __list(self, path) -> List[str]:
        """
        """
        return os.listdir(path)

    def listNewlyCompleted(self) -> List[str]:
        """
        Retrieve a list of the torrents that have completed since the last call
        to this method. Updates the completed torrents cache with the current
        list of completed torrents.
        """
        alreadyCompleted = self.completedTorrentsCache.retrieve()
        currentCompleted = self.__list(getGlobal('completed_dir'))
        newlyCompleted = [
            x for x in currentCompleted if not x in alreadyCompleted]

        getGlobal('log').write(
            Level.DEBUG, f'\'{len(newlyCompleted)}\' new torrents found.')

        return newlyCompleted

    def markHandled(self, filename: str) -> None:
        """
        Mark a torrent as handled, so that it won't show up on the next call
        to `listNewlyCompleted`.
        """
        self.completedTorrentsCache.append([filename])
