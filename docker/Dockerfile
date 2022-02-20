FROM python:3.9.7-buster

WORKDIR /application

COPY ./requirements.txt /application/requirements.txt

RUN pip install -r requirements.txt

CMD python3 app.py