from scanner.scanner import Scanner
from analyzer.analysis import Analysis
from analyzer.scan import Scan

from threading import Thread


class Analyzer:
    """
    Analyze files for their contents and type.
    """

    def __init__(self) -> None:
        """
        Initialize the analyzer.
        """
        self.scanners = set()

    def registerScanner(self, scanner: Scanner) -> None:
        """
        Register a scanner.
        """
        self.scanners.add(scanner)

    def analyze(self, filepath: str) -> Analysis:
        """
        Analyze a file/directory.
        """
        scans = list()
        for scanner in self.scanners:
            scan = Scan(filepath, scanner)
            scans.append(scan)
            scan.start()

        for scan in scans:
            scan.join()

        # This is the hard part, selecting which result is the most relevant
        # and maybe check if any of the results are even relevant at all. Just
        # return the first result from the first scan for now.
        result = scans[0].results[0]

        return Analysis(filepath, result)
