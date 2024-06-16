FROM ubuntu:latest


RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN apt-get install python3-venv -y

RUN apt-get install python3-flask -y
RUN apt-get install python3-requests -y
RUN apt-get install python3-psycopg2 -y
COPY ./src .

#RUN python3 main.py


EXPOSE 5000
