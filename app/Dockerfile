FROM python:3.6.8-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /DAGSTER_HOME

RUN apt-get update && apt-get install --no-install-recommends -y python3-dev gcc curl

COPY requirements.txt /app/requirements.txt
COPY dagster.yaml /DAGSTER_HOME/dagster.yaml

RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt --upgrade

COPY . /app

WORKDIR /app
CMD ["dagit", "-h", "0.0.0.0", "-p", "3000", "-w", "workspace.yaml"]
