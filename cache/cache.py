from typing import List
import os


class Cache:
    """
    """

    def __init__(self, path: str) -> None:
        """
        Initialize the cache directory.
        """
        stats = os.stat(path)
        uid = os.getuid()
        gid = os.getgid()

        if stats.st_uid != uid or stats.st_gid != gid:
            raise Exception(
                '\'{}\' must be owned by the current process.'.format(path))

        self.path = path

    def __write(self, name: str, data: List[str], mode: str):
        """
        Write to the cache.
        """
        path = os.path.join(self.path, name + '.cache')
        with open(path, mode, encoding='utf-8') as f:
            for entry in data:

                # Remove line breaks, so that every line written is an entry.
                entry = ''.join(entry.splitlines())
                if len(entry) > 0:
                    f.write(entry + '\n')

    def __read(self, name: str) -> List[str]:
        """
        Retrieve all entries from the cache.
        """
        try:
            path = os.path.join(self.path, name + '.cache')
            with open(path, 'r', encoding='utf-8') as f:
                return [entry[:-1] for entry in f.readlines()]

        except FileNotFoundError:
            return list()

    def append(self, name: str, data: List[str]) -> None:
        """
        Append new entries to the cache.
        """
        self.__write(name, data, 'a')

    def replace(self, name: str, data: List[str]) -> None:
        """
        Replace the contents of the cache.
        """
        self.__write(name, data, 'w')

    def retrieve(self, name: str) -> List[str]:
        """
        Retrieve all entries from the cache.
        """
        return self.__read(name)
