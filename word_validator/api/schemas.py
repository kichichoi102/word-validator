from pydantic import BaseModel


class SearchResponse(BaseModel):
    found: bool
