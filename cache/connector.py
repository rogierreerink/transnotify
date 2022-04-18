from cache.cache import Cache
from typing import List


class Connector:
    """
    Connect to a Cache backend.
    """

    def __init__(self, cache: Cache, name: str):
        """
        Initialize the connector.
        """
        self.cache = cache
        self.name = name

    def append(self, data: List[str]) -> None:
        """
        Append new entries to the cache.
        """
        return self.cache.append(self.name, data)

    def replace(self, data: List[str]) -> None:
        """
        Replace the contents of the cache.
        """
        return self.cache.replace(self.name, data)

    def retrieve(self) -> List[str]:
        """
        Retrieve all entries from the cache.
        """
        return self.cache.retrieve(self.name)
