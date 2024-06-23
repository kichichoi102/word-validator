from pydantic import BaseModel


class SearchRequest(BaseModel):
    word: str


class SearchResponse(BaseModel):
    found: bool
