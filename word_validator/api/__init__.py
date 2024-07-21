"""This package contains the API service"""

__all__ = [
    "BadRequest",
    "EntityNotFound",
    "FileNotFound",
    "FileSizeExceeded",
    "FileTypeNotSupported",
    "SearchResponse",
    "search_router",
    "setup_error_handlers",
    "TEMP_DIRECTORY",
]

from .exception_handler import setup_error_handlers
from .exceptions import (
    BadRequest,
    EntityNotFound,
    FileNotFound,
    FileSizeExceeded,
    FileTypeNotSupported,
)
from .schemas import SearchResponse
from .search_api import TEMP_DIRECTORY, search_router
