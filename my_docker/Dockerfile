FROM python:3

ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --upgrade pip
    pip3 install pipenv

RUN pip install pandas
    pip install sklearn
    pip install seaborn
    