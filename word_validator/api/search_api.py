from fastapi import APIRouter, Depends

from word_validator.api.schemas import SearchRequest, SearchResponse
from word_validator.core import Trie

search_router = APIRouter()


@search_router.post("/search/", response_model=SearchResponse)
async def search_word(
    request: SearchRequest, trie: Trie = Depends(Trie.initialize_trie)
) -> SearchResponse:
    found = trie.search_word(trie.root, request.word)
    return SearchResponse(found=found)
