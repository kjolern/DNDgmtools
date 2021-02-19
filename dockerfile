#FROM python:3.8-slim-buster
FROM python:3.8-slim-buster

WORKDIR /DNDgmtools

COPY . /DNDgmtools

CMD ["python3", "./main.py"]