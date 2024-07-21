from functools import lru_cache
import logging

from fastapi import Request

from word_validator.core.trie import Trie

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@lru_cache(maxsize=1)
def initialize_trie(file_path: str) -> Trie:
    return Trie.initialize_trie(file_path)


def get_trie_from_app(request: Request) -> Trie:
    logging.info(request.app.state.config.dictionary_file_path)
    trie: Trie = request.app.state.trie
    return trie
