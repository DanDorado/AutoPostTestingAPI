FROM python:3.8-alpine

COPY /DummyAPI/DummyAPI.py /DummyAPI/DummyAPI.py

WORKDIR /DummyAPI

RUN pip install flask

RUN apk add --update nodejs nodejs-npm

CMD ["python", "DummyAPI.py"]