FROM python:3.12-alpine
WORKDIR /code
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN poetry install
COPY . .
