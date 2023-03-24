FROM arm32v7/python:3.9-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
        libatlas-base-dev

RUN  apt-get clean && \
        rm -rf /var/lib/apt/lists/*

RUN apt update && apt install -y libatlas-base-dev

RUN python3 -m pip install tflite-runtime

WORKDIR /app
COPY . .

RUN sh setup.sh

RUN python3 post2.py