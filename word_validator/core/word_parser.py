import csv

import openpyxl


class WordParser:
    def __init__(self, file_path: str = "word_validator/data/words.txt") -> None:
        file_type = self._validate_file_type(file_path)

        self.file_path = file_path
        self.file_type = file_type
        self.words = []

    def parse_words(self) -> None:
        match self.file_type:
            case "txt":
                with open(self.file_path, "r") as file:
                    self.words = [line.strip() for line in file.readlines()]
            case "csv":
                with open(self.file_path, newline="") as csvfile:
                    self.words = [row[0] for row in csv.reader(csvfile, delimiter=",")]
            case "xlsx" | "xls":
                wb = openpyxl.load_workbook(self.file_path)
                sheet = wb.active
                self.words = [row[0] for row in sheet.iter_rows(values_only=True)]

    def _validate_file_type(self, file_path: str) -> str:
        try:
            file_type = file_path.split(".")[-1]
            match file_type:
                case "txt" | "csv" | "xlsx" | "xls":
                    return file_type
                case _:
                    raise ValueError(f"file_type '{file_type}' is not supported")
        except (IndexError, ValueError):
            raise ValueError("Invalid file_path. file_path must have a file extension")
