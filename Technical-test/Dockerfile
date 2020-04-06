FROM python:3

MAINTAINER Bouhaci "thinhinae.bouhaci@gmail.com"

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD . /app

RUN export FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]