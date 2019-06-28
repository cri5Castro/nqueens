FROM python:3.6

WORKDIR /src

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
COPY ./src /src/