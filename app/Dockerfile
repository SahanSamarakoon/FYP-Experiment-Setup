FROM python:3.9-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends libatlas-base-dev ffmpeg libsm6 libxext6 gcc python3-opencv

RUN  apt-get clean && \
        rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN python -m pip install pip --upgrade && pip install --index-url=https://www.piwheels.org/simple -r requirements.txt 
RUN pip install tflite_runtime-2.11.0-cp39-cp39-manylinux2014_armv7l.whl
RUN pip install tflite_support-0.4.3-cp39-cp39-manylinux2014_armv7l.whl

CMD [ "python3", "./post2.py"]