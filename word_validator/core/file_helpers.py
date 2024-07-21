import aiofiles
from fastapi import Request, UploadFile

from word_validator.api.exceptions import (
    EntityNotFound,
    FileSizeExceeded,
    FileTypeNotSupported,
)

SUPPORTED_FILE_TYPES = ["txt", "csv", "xlsx", "xls"]
CHUNK_SIZE = 1024 * 100  # 100 KB


def validate_file_extension(file_name: str | None) -> str:
    if not file_name or file_name == "":
        raise EntityNotFound("File not found")
    file_extension = file_name.split(".")[-1]
    if file_extension not in SUPPORTED_FILE_TYPES:
        raise FileTypeNotSupported(f"File type {file_extension} is not supported")

    return file_extension


async def validate_file_size(file: UploadFile, request: Request) -> None:
    file_size = 0

    async with aiofiles.open(file.file.fileno(), mode="rb") as f:
        while True:
            chunk = await f.read(CHUNK_SIZE)
            if not chunk:
                break
            file_size += len(chunk)
            if file_size >= request.app.state.config.max_file_size:
                raise FileSizeExceeded(
                    f"File size exceeded. Maximum file size is {request.app.state.config.max_file_size} bytes"
                )
