FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt update && apt install -y gcc make

RUN python -m pip install --upgrade pip

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
