ARG python_version
ARG app_version

FROM python:${python_version}

LABEL version=${app_version}

LABEL maintainer Francis J. Garcia <contacto@francisjgarcia.es>

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN ln -fs /usr/share/zoneinfo/Europe/Madrid /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

WORKDIR /usr/src/app

COPY ../app .

RUN pip install -r requirements.txt

CMD [ "python", "-u", "app.py" ]
