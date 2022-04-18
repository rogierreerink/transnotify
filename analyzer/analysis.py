from scanner.result import Result

from os import stat_result


class Analysis:
    """
    The result of an analysis.
    """

    def __init__(self, filepath: str, result: Result):
        """
        Initialize the analysis.
        """
        self.filepath = filepath
        self.result = result
