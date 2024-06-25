# Word Validator

## Introduction
This project is a small stepping stone to eventually migate away from the service I'm using in my main project, which requires lots of word validations. It doesn't make sense for me to use the current solution to validate 100s - 1000s of words since the service I'm currently using has rate limiting, and I'd rather save the limited resources to fetch relationships between words. Furthermore, this is an easily scalable microservice.

Searching for words in a trie is O(n) where n is the length of the word, as opposed to O(n^2) for a linear search or O(n log n) for a binary search.
For reference: https://miro.medium.com/v2/resize:fit:1400/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg

## Usage
- install poetry -> poetry run python word_validator/main.py
- or just word_validator/main.py
just learn poetry you're doing yourself a disservice by continuing to stick with pip

## TODO
- add github actions for ci
- fix mypy
- Fix csv+xlsx import
- fix hard coded paths
- add option to select text file or multiple files
- db might be overkill, but think of a way to efficiently store trie data
- Add tests + coverage
- add route to do multiple words (convenience not efficiency) 
- host (probs on vercel)
- Dockerize

## Sources:
- [Trie Wikipedia](https://en.wikipedia.org/wiki/Trie)
- [Scrabble Words](https://github.com/raun/Scrabble/blob/master/words.txt)
- [Algorithm Inspiration](https://www.cs.cmu.edu/afs/cs/academic/class/15451-s06/www/lectures/scrabble.pdf)
