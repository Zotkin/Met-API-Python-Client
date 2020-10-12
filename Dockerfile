FROM python:3.8.1

ADD * /

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
RUN pip install -e .
