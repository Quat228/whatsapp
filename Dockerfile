FROM python:3.11.1-alpine3.17

WORKDIR /usr/src/whatsapp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY main.py ./

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
