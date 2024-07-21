from functools import lru_cache

from fastapi import Request

from word_validator.core.trie import Trie


@lru_cache(maxsize=1)
def initialize_trie(file_path: str) -> Trie:
    return Trie.initialize_trie(file_path)


def get_trie_from_app(request: Request) -> Trie:
    if not request.app.state.trie:
        trie: Trie = initialize_trie("word_validator/data/storage/scrabble_words.txt")
    else:
        trie: Trie = request.app.state.trie
    return trie
