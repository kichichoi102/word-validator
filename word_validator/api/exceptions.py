class BadRequest(Exception):
    """Will be raised when the input of the request is wrong."""


class EntityNotFound(Exception):
    """Will be thrown if a resource could not be found."""


class FileNotFound(EntityNotFound):
    """Is raised when ever a file is expected but a directory is addressed."""


class FileSizeExceeded(BadRequest):
    """Will be raised if the user tries to store a file larger than the
    defined file size limit."""


class FileTypeNotSupported(BadRequest):
    """Will be raised if the user tries to store a file with a
    file type that is not supported."""
