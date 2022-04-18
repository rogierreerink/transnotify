from scanner.result import Result
from scanner.type import Type
from datetime import datetime


class Movie(Result):
    """
    A Movie result.
    """
    title: str = None
    date: datetime = None

    def __init__(self) -> None:
        """
        Initialize the Movie result.
        """
        super(Type.MOVIE)
