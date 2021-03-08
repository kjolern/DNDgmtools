FROM python:3.9

WORKDIR /DNDgmtools

COPY . /DNDgmtools

RUN apt install git

CMD ["python3", "main.py"]