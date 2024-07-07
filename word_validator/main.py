from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from word_validator.api import search_router, setup_error_handlers

app = FastAPI()

app.include_router(search_router)
setup_error_handlers(app)


@app.get("/", include_in_schema=False)
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
