"""This module contains the Trie class which is the data structure
to represent the dictionary of valid (scrabble) words."""

__all__ = ["Trie"]

from functools import lru_cache

from word_validator.core.trie_node import TrieNode
from word_validator.core.word_parser import WordParser


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            char = char.lower()
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_word(self, node: TrieNode, word: str) -> bool:
        for char in word:
            char = char.lower()
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    @staticmethod
    @lru_cache(maxsize=1)
    def initialize_trie(file_path: str = "word_validator/data/words.txt") -> "Trie":
        word_parser = WordParser(file_path)
        word_parser.parse_words()
        trie = Trie()
        for word in word_parser.words:
            trie.insert(word)
        return trie
