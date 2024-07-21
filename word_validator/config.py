from pydantic import BaseModel


class Config(BaseModel):
    """
    Configuration class for the application.
    """

    host: str = "127.0.0.1"
    port: int = 8000
    dictionary_file_path: str = "word_validator/data/storage/scrabble_words.txt"
    max_file_size: int = 1024000  # 1000 KB
