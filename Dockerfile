FROM python:3.8.2-buster
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt