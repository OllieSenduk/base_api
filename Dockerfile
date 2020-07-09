FROM python:3.7-apline
MAINTAINER Ichi Studios

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

run mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
User user