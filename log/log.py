from enum import Enum
from datetime import datetime, date
import os


class Level(Enum):
    """
    Severity levels.
    """
    DEBUG = 1
    WARNING = 2
    ERROR = 3


class Log:
    """
    Provides an interface to the log files.
    """

    def __init__(self, path: str) -> None:
        """
        Initialize the log directory.
        """
        stats = os.stat(path)
        uid = os.getuid()
        gid = os.getgid()

        if stats.st_uid != uid or stats.st_gid != gid:
            raise Exception(
                '\'{}\' must be owned by the current process.'.format(path))

        self.path = path

    def write(self, level: Level, message: str) -> None:
        """
        Write a new entry to the log.
        """
        # Remove line breaks, so that every line written is an entry.
        message = ''.join(message.splitlines())
        if len(message) == 0:
            return

        path = str(date.today()) + '.log'
        path = os.path.join(self.path, path)
        with open(path, 'a', encoding='utf-8') as f:
            f.write(str(datetime.now()) +
                    ': ' + str(level) + ' ' + message + '\n')
