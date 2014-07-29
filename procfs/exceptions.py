"""procfs exceptions"""


class BaseException(Exception):
    """Base exception"""


class PathNotFoundError(BaseException):
    """The path does not exist"""


class PathNotADirectoryError(BaseException):
    """The path is not a directory"""


class PathNotAFileError(BaseException):
    """The path is not a file"""


class ProcessException(BaseException):
    """Exceptions raised by process handling code"""


class UnknownProcessError(ProcessException):
    """The process does not exist"""


class NoParentProcessError(ProcessException):
    """The process has no parent process"""
