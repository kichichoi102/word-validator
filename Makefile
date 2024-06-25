default: format

all:
	make format
	make ruff
	make mypy
	make pytest
	make coverage

format:
	poetry run ruff check word_validator --fix-only
	poetry run black .
	poetry run isort . --profile=black

pytest:
	poetry run coverage run --source=word_validator -m pytest .

coverage:
	poetry run coverage html -d tests/coverage_report
	poetry run coverage report --fail-under=100

mypy:
	poetry run mypy word_validator

ruff:
	poetry run ruff check word_validator	

test:
	make pytest
	make coverage

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

ci-check:
	make format
	make ruff
	make mypy
	make pytest
	make coverage

cd:
	make requirements