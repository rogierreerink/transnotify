from cache.connector import Connector
from log.log import Level
from globals import getGlobal

from typing import List
import os


class Torrents:
    """
    An interface to the torrent directories.
    """

    def __init__(
            self,
            completedTorrentsCache: Connector,
            completedTorrentsPath: str) -> None:
        """
        Initialize the torrents API.
        """
        self.completedTorrentsCache = completedTorrentsCache
        self.completedTorrentsPath = completedTorrentsPath

    def __list(self, path) -> List[str]:
        """
        """
        return os.listdir(path)

    def listNewCompleted(self) -> List[str]:
        """
        Retrieve a list of the torrents that have completed since the last call
        to this method. Updates the completed torrents cache with the current
        list of completed torrents.
        """
        alreadyCompleted = self.completedTorrentsCache.retrieve()
        currentCompleted = self.__list(self.completedTorrentsPath)
        newlyCompleted = [
            x for x in currentCompleted if not x in alreadyCompleted]
        self.completedTorrentsCache.replace(currentCompleted)

        getGlobal('log').write(
            Level.DEBUG, f'\'{len(newlyCompleted)}\' new torrents found.')

        return newlyCompleted
