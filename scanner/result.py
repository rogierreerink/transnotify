from scanner.type import Type
from abc import ABCMeta


class Result(metaclass=ABCMeta):
    """
    A scan result.
    """
    t: Type = None

    def __init__(self, t: Type) -> None:
        """
        Specify the result type.
        """
        self.t = t
