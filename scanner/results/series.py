from scanner.result import Result
from scanner.type import Type
from datetime import datetime


class Series(Result):
    """
    A TV Series result.
    """
    title: str = None
    series: str = None
    season: int = None
    episode: int = None
    date: datetime = None

    def __init__(self) -> None:
        """
        Initialize the TV Series result.
        """
        super(Type.SERIES)
