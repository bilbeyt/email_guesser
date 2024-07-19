FROM python:3.12-slim

COPY . /backend
WORKDIR /backend

RUN pip install poetry
RUN apt-get update && apt-get install -y postgresql-client-15 make
RUN poetry config virtualenvs.create false
RUN poetry --no-ansi install --with dev --no-root
RUN make lint
ENV PYTHONPATH=.
CMD python app/main.py