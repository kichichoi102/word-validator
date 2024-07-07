"""This package contains the API service"""

__all__ = [
    "BadRequest",
    "EntityNotFound",
    "FileNotFound",
    "FileSizeExceeded",
    "FileTypeNotSupported",
    "SearchRequest",
    "SearchResponse",
    "search_router",
    "setup_error_handlers",
]

from .exception_handler import setup_error_handlers
from .exceptions import (
    BadRequest,
    EntityNotFound,
    FileNotFound,
    FileSizeExceeded,
    FileTypeNotSupported,
)
from .schemas import SearchRequest, SearchResponse
from .search_api import search_router
