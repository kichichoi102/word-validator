from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_413_REQUEST_ENTITY_TOO_LARGE,
    HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from .exceptions import (
    BadRequest,
    EntityNotFound,
    FileNotFound,
    FileSizeExceeded,
    FileTypeNotSupported,
)


def setup_error_handlers(app: FastAPI) -> None:
    async def _handle_exception(
        request: Request, exc: Exception, status_code: int
    ) -> Response:
        return await http_exception_handler(
            request=request,
            exc=HTTPException(
                status_code=status_code,
                detail=str(exc),
            ),
        )

    @app.exception_handler(BadRequest)
    async def bad_request_handler(request: Request, exc: BadRequest) -> Response:
        return await _handle_exception(
            request=request, exc=exc, status_code=HTTP_400_BAD_REQUEST
        )

    @app.exception_handler(EntityNotFound)
    async def entity_not_found_handler(
        request: Request, exc: EntityNotFound
    ) -> Response:
        return await _handle_exception(
            request=request, exc=exc, status_code=HTTP_404_NOT_FOUND
        )

    @app.exception_handler(FileNotFound)
    async def file_not_found_handler(request: Request, exc: FileNotFound) -> Response:
        return await _handle_exception(
            request=request, exc=exc, status_code=HTTP_404_NOT_FOUND
        )

    @app.exception_handler(FileSizeExceeded)
    async def file_size_exceeded_handler(
        request: Request, exc: FileSizeExceeded
    ) -> Response:
        return await _handle_exception(
            request=request, exc=exc, status_code=HTTP_413_REQUEST_ENTITY_TOO_LARGE
        )

    @app.exception_handler(FileTypeNotSupported)
    async def file_type_not_supported_handler(
        request: Request, exc: FileTypeNotSupported
    ) -> Response:
        return await _handle_exception(
            request=request, exc=exc, status_code=HTTP_415_UNSUPPORTED_MEDIA_TYPE
        )

    @app.exception_handler(HTTP_500_INTERNAL_SERVER_ERROR)
    async def general_exception_handler(request: Request, exc: Exception) -> Response:
        response = JSONResponse(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, content={"details": str(exc)}
        )
        return response
