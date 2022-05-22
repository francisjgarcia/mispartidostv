FROM python:3.10-slim-bullseye

LABEL org.opencontainers.image.source="https://github.com/francisjgarcia/mispartidostv"
LABEL org.opencontainers.image.description "Obtiene los próximos partidos de fútbol que se televisarán"
LABEL maintainer Francis J. Garcia <contacto@francisjgarcia.es>

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app

COPY app .

RUN pip install -r requirements.txt

CMD [ "python", "-u", "app.py" ]
