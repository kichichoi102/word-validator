from contextlib import asynccontextmanager
from typing import AsyncIterator
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from word_validator.api import search_router, setup_error_handlers
from word_validator.config import Config
from word_validator.dependencies import initialize_trie

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    app.state.config = Config()
    app.state.trie = initialize_trie(app.state.config.dictionary_file_path)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(search_router)
setup_error_handlers(app)


@app.get("/", include_in_schema=False)
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    import uvicorn
    app.state.config = Config()
    app.state.trie = initialize_trie(app.state.config.dictionary_file_path)
    config = app.state.config
    uvicorn.run(app, host=config.host, port=config.port)
