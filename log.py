import os
import enum
import datetime


class Level(enum.Enum):
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

    def __init__(self, path):
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

    def write(self, level: Level, message: str):
        """
        Write a new entry to the log.
        """
        message = ''.join(message.splitlines())
        if len(message) == 0:
            return

        path = str(datetime.date.today()) + '.log'
        path = os.path.join(self.path, path)

        with open(path, 'a') as f:
            f.write(str(datetime.datetime.now()) +
                    ': ' + str(level) + ' ' + message + '\n')
