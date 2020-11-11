FROM python:3.8-alpine

COPY ./envtesting.py /envtest/envtesting.py

WORKDIR /envtest

RUN pip install flask

RUN apk add --update nodejs nodejs-npm

CMD ["python", "envtesting.py"]
