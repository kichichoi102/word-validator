import os
from pathlib import Path

from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK

from word_validator.core import Trie, validate_file_extension
from word_validator.dependencies import get_trie_from_app, initialize_trie

from .exceptions import BadRequest
from .schemas import SearchResponse

STORAGE_DIRECTORY = "word_validator/data/storage/"
TEMP_DIRECTORY = "word_validator/data/tmp/"

search_router = APIRouter()


@search_router.get("/search/", response_model=SearchResponse)
async def search_word(
    word: str, trie: Trie = Depends(get_trie_from_app)
) -> SearchResponse:
    return SearchResponse(found=trie.search_word(trie.root, word))


@search_router.put("/update-source-file")
async def update_file_path(
    request: Request,
    file_path: str = Query(
        ...,
        description="Select a file",
        enum=os.listdir(STORAGE_DIRECTORY),
    ),
) -> JSONResponse:
    validate_file_extension(file_path)
    return _handle_file_and_update_trie(file_path, request)


def _handle_file_and_update_trie(file_path: str, request: Request) -> JSONResponse:
    app_state = request.app.state
    storage_file_path = os.path.join(STORAGE_DIRECTORY, file_path)
    try:
        # Validate that the file path is a valid file in the storage directory
        Path(storage_file_path).resolve(strict=True)
        initialize_trie.cache_clear()
        new_trie = initialize_trie(storage_file_path)
        app_state.config.dictionary_file_path = storage_file_path
        app_state.trie = new_trie
    except Exception as e:
        initialize_trie(app_state.config.dictionary_file_path)
        raise BadRequest(f"Error initializing trie: {e}")

    return JSONResponse(
        status_code=HTTP_200_OK,
        content=f"Trie reinitialized successfully with file: {file_path}",
    )
