"""This module contains the Trie class which is the data structure
to represent the dictionary of valid (scrabble) words."""

__all__ = ["Trie"]

from .trie_node import TrieNode
from .word_parser import WordParser


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
    def initialize_trie(file_path: str) -> "Trie":
        Trie._try_open_file(file_path)
        word_parser = WordParser(file_path)
        word_parser.parse_words()
        trie = Trie()
        for word in word_parser.words:
            trie.insert(word)
        return trie

    @staticmethod
    def _try_open_file(file_path: str) -> None:
        try:
            with open(file_path, "r") as file:
                file.readline()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error opening file: {e}")
