FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -qqy update

COPY ./requirements.txt /BBC_crach/
RUN pip install -r /BBC_crach/requirements.txt

COPY . /BBC_crach
WORKDIR /BBC_crach
# run entrypoint.sh

