# syntax=docker/dockerfile:1

FROM python:3.8
ENV FLASK_APP=main.py
WORKDIR /app

COPY requirements.txt requirements.txt
COPY peduel_first_patrol_ver2.waypoints peduel_first_patrol_ver2.waypoints
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "main", "--connect", "192.168.65.2:14552", "--mission_file", "peduel_first_patrol_ver2.waypoints"]