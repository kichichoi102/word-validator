"""This module contains the TrieNode class, which is used to build a trie data structure
to represent the dictionary of valid (scrabble) words."""

__all__ = ["TrieNode"]

from collections import defaultdict
from typing import DefaultDict


class TrieNode:
    def __init__(self):
        self.children: DefaultDict[str, TrieNode] = defaultdict(TrieNode)
        self.is_end_of_word: bool = False
