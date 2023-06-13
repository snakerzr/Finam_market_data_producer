FROM python:3.9

WORKDIR /app

COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml

RUN pip install --upgrade pip && pip install poetry && poetry install

COPY ./FinamPy ./FinamPy
COPY ./src/ ./src/
COPY main.py main.py

CMD ["poetry", "run", "python", "main.py"]