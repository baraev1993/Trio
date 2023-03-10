FROM matthewfeickert/docker-python3-ubuntu:latest

ENV PYTHONUNBUFFERED True

WORKDIR /

COPY . .

USER root

RUN apt-get update 
RUN apt-get install -y apt-utils

RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install gunicorn
RUN pip install -r req.txt

ENV SECRET_KEY==p$cx6wu-uu#b_2=d5s)-k5tqechu5aswy@kgepo+tar(hox_u
ENV DB_USER=postgres
ENV DB_PASSWORD=lu4d7ZJ3gQWkAe6xcE3u
ENV DB_HOST=containers-us-west-75.railway.app
ENV DB_PORT=6118
ENV DB_NAME=railway
ENV SMTP_EMAIL=baraev1993@gmail.com
ENV SMTP_PASSWORD=nhbqkroqxkaycdfv
ENV PORT=8000

RUN python3 manage.py migrate
RUN python3 manage.py collectstatic

CMD gunicorn --bind 0.0.0.0:8000 config.wsgi:application
