from scanner.result import Result
from scanner.type import Type
from datetime import datetime


class Series(Result):
    """
    A TV Series result.
    """
    title: str = None
    season: int = None
    episode: int = None

    def __init__(self) -> None:
        """
        Initialize the TV Series result.
        """
        super(Type.SERIES)

    def __str__(self) -> str:
        """
        Get the results string representation.
        """
        return 'Title: ' + self.title \
            + 'Season: ' + self.season \
            + 'Episode: ' + self.episode
