from fastapi import FastAPI

from word_validator.api.search_api import search_router

app = FastAPI()

app.include_router(search_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
