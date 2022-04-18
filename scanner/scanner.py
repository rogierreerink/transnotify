from scanner.result import Result
from abc import ABCMeta, abstractmethod
from typing import List


class Scanner(metaclass=ABCMeta):
    """
    An abstracter scanner base class.
    """

    @abstractmethod
    def scan(filepath: str) -> List[Result]:
        """
        Return the most relevant scan results.
        """
        pass
