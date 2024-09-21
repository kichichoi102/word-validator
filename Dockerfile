FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi
EXPOSE 8000

ENTRYPOINT ["poetry", "run", "uvicorn", "word_validator.main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]