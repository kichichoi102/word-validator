import csv

import openpyxl

from word_validator.api.exceptions import BadRequest, FileNotFound

from .file_helpers import validate_file_extension


class WordParser:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.file_type = validate_file_extension(file_path)
        self.words: list[str] = []

    def parse_words(self) -> None:
        try:
            match self.file_type:
                case "txt":
                    with open(self.file_path, "r") as file:
                        self.words = [line.strip() for line in file.readlines()]
                case "csv":
                    with open(self.file_path, newline="") as csvfile:
                        self.words = [
                            row[0] for row in csv.reader(csvfile, delimiter=",")
                        ]
                case "xlsx" | "xls":
                    wb = openpyxl.load_workbook(self.file_path)
                    sheet = wb.active
                    if sheet is not None:
                        self.words = [
                            str(row[0]) for row in sheet.iter_rows(values_only=True)
                        ]
                    else:
                        raise BadRequest("Sheet not found in the workbook.")
        except FileNotFoundError:
            raise FileNotFound(f"File with path: {self.file_path} was not found.")
