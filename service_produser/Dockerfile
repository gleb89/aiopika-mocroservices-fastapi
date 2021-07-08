FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn aio-pika
