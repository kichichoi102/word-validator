from contextlib import asynccontextmanager
from typing import AsyncIterator
import logging
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from word_validator.api import search_router, setup_error_handlers
from word_validator.config import Config
from word_validator.dependencies import initialize_trie

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    app.state.config = Config()
    logging.info(app.state.config.dictionary_file_path)
    app.state.trie = initialize_trie(app.state.config.dictionary_file_path)
    logging.info(app.state.trie)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(search_router)
setup_error_handlers(app)


@app.get("/", include_in_schema=False)
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    import uvicorn

    config = app.state.config
    uvicorn.run(app, host=config.host, port=config.port)
