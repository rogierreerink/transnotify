from scanner.scanner import Scanner
from scanner.result import Result

from typing import List
from threading import Thread


class Scan(Thread):
    """
    Perform a scan.
    """
    results: List[Result] = None

    def __init__(self, filepath: str, scanner: Scanner) -> None:
        """
        Initialize the scan.
        """
        super().__init__()
        self.filepath = filepath
        self.scanner = scanner

    def run(self) -> None:
        """
        Run the scan and store its results.
        """
        self.results = self.scanner.scan(self.filepath)
