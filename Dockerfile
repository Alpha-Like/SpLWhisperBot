FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install requirements.txt

COPY . /app

CMD ["python3", "yashu.py"]
