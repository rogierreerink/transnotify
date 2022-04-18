from posixpath import basename
from shutil import copy, copytree
from os import path


class Fileman:
    """
    Perform file operations, such as copy and move.
    """

    @staticmethod
    def copy(source: str, destination: str):
        """
        Copy a file or directory.
        """
        if path.isfile(source):
            copy(source, destination)
        else:
            copytree(source, path.join(
                destination, basename(source)))
