FROM python:3.8
RUN pip install --upgrade pip
RUN apt-get update && apt-get upgrade -y
COPY . /app
RUN pip install scrapy
RUN pip install pytest
RUN pip install pymongo
WORKDIR /app
