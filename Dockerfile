FROM python:3.8.1

ADD * /

RUN apt-get install curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN poetry install
RUN poetry shell
